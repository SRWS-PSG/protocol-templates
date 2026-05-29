"""Render a protocol master Markdown to Google Docs with embedded comments.

Pipeline:
  1. Read the language-specific master (e.g. protocol_template...ja.md).
  2. Pandoc md -> docx (uses references.bib + vancouver.csl).
  3. Read comments.yaml; inject anchored Word comments into the docx
     (via tools/docx_comments.py).
  4. Drive API: upload the comment-laden docx with
     mimeType=application/vnd.google-apps.document so Google auto-converts
     it to a Doc. Word comments are translated into anchored Doc comments
     during conversion -- this avoids Drive's undocumented and unreliable
     anchor-JSON format for Docs.

First-time setup:
  1. pip install -r tools/requirements.txt
  2. Create an OAuth Desktop client at
       https://console.cloud.google.com/apis/credentials
     (Enable Drive API + Docs API for the project first.)
  3. Download the client secret JSON and save it to
       tools/.gcp/credentials.json
  4. Run `python tools/build_gdoc.py --lang ja` -- a browser window opens for
     the OAuth consent. The refresh token is cached at tools/.gcp/token.json.

Usage:
  python tools/build_gdoc.py --lang ja
  python tools/build_gdoc.py --lang en --folder-id <Drive folder id>
  python tools/build_gdoc.py --lang ja --dry-run     # build docx only, skip upload
  python tools/build_gdoc.py --lang ja --share-with someone@example.com
  python tools/build_gdoc.py --lang ja --new         # force new Doc (ignore saved ID)
  python tools/build_gdoc.py --lang ja --doc-id <id> # overwrite a specific Doc

By default, the document ID returned by the first upload is cached in
tools/.gcp/upload_state.json keyed by language, and subsequent runs
overwrite the same Doc (preserving its URL/ID). Use --new to force a
fresh document, or --doc-id to target an explicit existing Doc.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

sys.path.insert(0, str(Path(__file__).resolve().parent))
from docx_comments import inject_comments


ROOT = Path(__file__).resolve().parents[1]

# Per-template metadata. Each template has its own directory under templates/,
# its own references.bib, its own comments.yaml, and a master-file naming
# convention configured here. Do NOT consolidate across templates: each must
# stand alone so changes to one never silently affect another.
TEMPLATES: dict[str, dict[str, str]] = {
    "intervention-review": {
        "subdir": "intervention-review",
        "master_stem": "protocol_template_for_intervention_review",
    },
    "scoping-review": {
        "subdir": "scoping-review",
        "master_stem": "protocol_template_for_scoping_review",
    },
    "dta-review": {
        "subdir": "dta-review",
        "master_stem": "protocol_template_for_dta_review",
    },
}


def _template_paths(template: str) -> dict[str, Path]:
    if template not in TEMPLATES:
        raise SystemExit(
            f"unknown template {template!r}; choose from {sorted(TEMPLATES)}"
        )
    cfg = TEMPLATES[template]
    tdir = ROOT / "templates" / cfg["subdir"]
    # The reference.docx defines the custom styles (Placeholder, Note,
    # NoteListParagraph) that color editing aids cyan. Some templates (e.g.
    # dta-review) don't ship their own and reuse intervention-review's, which
    # is patched by intervention-review/filters/_patch_reference_docx.py. Fall
    # back to it so build_gdoc.py matches build.ps1's shared-reference behavior.
    reference_docx = tdir / "filters" / "reference.docx"
    if not reference_docx.exists():
        reference_docx = (
            ROOT / "templates" / "intervention-review" / "filters" / "reference.docx"
        )
    return {
        "template_dir": tdir,
        "comments_yaml": tdir / "comments.yaml",
        "bib": tdir / "references.bib",
        "csl": tdir / "vancouver.csl",
        "build_dir": tdir / "build",
        "lua_filter": tdir / "filters" / "highlight.lua",
        "reference_docx": reference_docx,
        "master_stem": cfg["master_stem"],
    }

ENV_FILES = [ROOT / ".env", ROOT / "tools" / ".env"]


def load_env() -> None:
    """Lightweight KEY=VALUE loader for tools/.env and project .env.

    Existing process env wins; we only fill in missing keys.
    """
    for path in ENV_FILES:
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            os.environ.setdefault(key, val)

GCP_DIR = ROOT / "tools" / ".gcp"
CREDENTIALS_FILE = GCP_DIR / "credentials.json"
TOKEN_FILE = GCP_DIR / "token.json"
UPLOAD_STATE_FILE = GCP_DIR / "upload_state.json"

DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


def load_upload_state() -> dict:
    """Return mapping {key: documentId} of previously uploaded Docs.

    Keys are of the form "<template>:<lang>". Bare-lang keys ("ja"/"en") from
    the pre-multi-template version are migrated to "intervention-review:<lang>".
    """
    if not UPLOAD_STATE_FILE.exists():
        return {}
    try:
        state = json.loads(UPLOAD_STATE_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"  WARN could not read {UPLOAD_STATE_FILE}: {e}; ignoring")
        return {}
    for legacy in ("ja", "en"):
        if legacy in state and f"intervention-review:{legacy}" not in state:
            state[f"intervention-review:{legacy}"] = state.pop(legacy)
    return state


def save_upload_state(state: dict) -> None:
    GCP_DIR.mkdir(parents=True, exist_ok=True)
    UPLOAD_STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/documents",
]


# --------------------------------------------------------------------------- #
# Master + comment loading
# --------------------------------------------------------------------------- #


def master_path(paths: dict[str, Path], lang: str) -> Path:
    tdir = paths["template_dir"]
    stem = paths["master_stem"]
    if lang == "en":
        return tdir / f"{stem}.md"
    return tdir / f"{stem}.{lang}.md"


def load_comments(paths: dict[str, Path], lang: str) -> list[dict]:
    """Load comments applicable to the given language as plain dicts.

    Returns dicts with keys: id, anchor (str), body (str), occurrence (int).
    The body is a single Japanese string shared across languages; only the
    anchor text differs per master file.
    """
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install -r tools/requirements.txt")
    data = yaml.safe_load(paths["comments_yaml"].read_text(encoding="utf-8"))
    out: list[dict] = []
    for entry in data.get("comments", []):
        anchor = (entry.get("anchor") or {}).get(lang)
        body = entry.get("body")
        if not anchor or not body:
            continue
        out.append(
            {
                "id": entry["id"],
                "anchor": anchor,
                "body": body.rstrip(),
                "occurrence": int(entry.get("occurrence", 1)),
            }
        )
    return out


def build_docx(paths: dict[str, Path], src: Path, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc",
        str(src),
        "--from=markdown",
        "--to=docx",
        "--citeproc",
        f"--bibliography={paths['bib']}",
        f"--csl={paths['csl']}",
        f"--lua-filter={paths['lua_filter']}",
        f"--resource-path={paths['template_dir']}",
        "--standalone",
        "-o",
        str(out),
    ]
    if paths["reference_docx"].exists():
        cmd.insert(-2, f"--reference-doc={paths['reference_docx']}")
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)
    _retag_note_list_items(out)


def _retag_note_list_items(docx_path: Path) -> int:
    """Swap pStyle of list-item paragraphs inside Note blocks.

    Pandoc's docx writer overrides any Div custom-style with the built-in
    "Compact" style on list items, so the Lua filter alone can't give list
    paragraphs the cyan left border or keepNext. Instead, the Lua filter
    marks every run inside a Note (incl. list items) with the NoteInline
    character style. Here we rewrite any paragraph that:

      - has pStyle = "Compact", and
      - contains at least one run with rStyle = "NoteInline"

    to pStyle = "NoteListParagraph". That style (defined in reference.docx)
    is based on Compact, so list numbering / spacing survive, but it adds
    the left border and keepNext.

    Returns the number of paragraphs updated.
    """
    import shutil
    import zipfile

    DOC_PATH = "word/document.xml"
    PARA_RE = re.compile(r"<w:p\b[^>]*>.*?</w:p>", flags=re.DOTALL)
    PSTYLE_RE = re.compile(r'(<w:pStyle\s+w:val=")Compact(")')
    HAS_NOTEINLINE_RE = re.compile(r'<w:rStyle\s+w:val="NoteInline"')

    with zipfile.ZipFile(docx_path) as zin:
        members = [(item, zin.read(item.filename)) for item in zin.infolist()]

    count = 0

    def _swap(match: "re.Match[str]") -> str:
        nonlocal count
        para = match.group(0)
        if not HAS_NOTEINLINE_RE.search(para):
            return para
        new_para, n = PSTYLE_RE.subn(r"\1NoteListParagraph\2", para, count=1)
        if n:
            count += 1
        return new_para

    new_members: list[tuple[zipfile.ZipInfo, bytes]] = []
    for item, data in members:
        if item.filename == DOC_PATH:
            xml = data.decode("utf-8")
            xml = PARA_RE.sub(_swap, xml)
            data = xml.encode("utf-8")
        new_members.append((item, data))

    tmp = docx_path.with_suffix(".docx.tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, data in new_members:
            zout.writestr(item, data)
    shutil.move(tmp, docx_path)
    if count:
        print(f"  retagged {count} list paragraph(s) -> NoteListParagraph")
    return count


# --------------------------------------------------------------------------- #
# Google auth
# --------------------------------------------------------------------------- #


def get_credentials():
    """Resolve credentials in this order:

    1. Cached InstalledAppFlow token at tools/.gcp/token.json (refreshed if expired).
    2. OAuth Desktop client secret at tools/.gcp/credentials.json -> browser consent.
    3. Application Default Credentials (gcloud auth application-default login).

    For (3) to work, ADC must have been minted with the Drive.file + Docs scopes:
        gcloud auth application-default login \
            --scopes="https://www.googleapis.com/auth/drive.file,\
https://www.googleapis.com/auth/documents,\
https://www.googleapis.com/auth/cloud-platform"

    The narrower drive.file scope avoids Google's sensitive-scope verification
    block while still giving the script full control over files it creates.
    """
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
        if creds and creds.valid:
            return creds
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            TOKEN_FILE.write_text(creds.to_json())
            return creds

    if CREDENTIALS_FILE.exists():
        from google_auth_oauthlib.flow import InstalledAppFlow

        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
        creds = flow.run_local_server(port=0)
        GCP_DIR.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(creds.to_json())
        return creds

    try:
        import google.auth

        creds, _ = google.auth.default(scopes=SCOPES)
        return creds
    except Exception as e:
        raise RuntimeError(
            "No usable credentials. Either:\n"
            "  (a) gcloud auth application-default login \\\n"
            '        --scopes="https://www.googleapis.com/auth/drive.file,'
            "https://www.googleapis.com/auth/documents,"
            'https://www.googleapis.com/auth/cloud-platform"\n'
            "  (b) Place an OAuth Desktop client secret at " + str(CREDENTIALS_FILE) + "\n"
            f"Underlying error: {e}"
        ) from e


# --------------------------------------------------------------------------- #
# Drive operations
# --------------------------------------------------------------------------- #


def _build_drive(creds):
    from googleapiclient.discovery import build

    return build("drive", "v3", credentials=creds, cache_discovery=False)


def upload_to_drive(creds, docx: Path, name: str, folder_id: str | None) -> str:
    """Upload docx as a new Google Doc (auto-converted). Returns documentId."""
    import time

    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload

    drive = _build_drive(creds)
    body = {
        "name": name,
        "mimeType": "application/vnd.google-apps.document",
    }
    if folder_id:
        body["parents"] = [folder_id]

    last_err: Exception | None = None
    for attempt in range(1, 4):
        media = MediaFileUpload(str(docx), mimetype=DOCX_MIME, resumable=True)
        try:
            request = drive.files().create(body=body, media_body=media, fields="id")
            response = None
            while response is None:
                _, response = request.next_chunk()
            return response["id"]
        except HttpError as e:
            last_err = e
            if e.resp.status in (500, 502, 503, 504) and attempt < 3:
                wait = 2 ** attempt
                print(f"  upload attempt {attempt} failed ({e.resp.status}); retry in {wait}s")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"upload failed after retries: {last_err}")


def update_drive(creds, docx: Path, document_id: str, name: str | None) -> str:
    """Overwrite the content of an existing Google Doc with a new docx.

    Google reconverts the docx and replaces the Doc body; the file ID and
    URL stay the same. Returns documentId on success. Raises HttpError on
    failure (callers may fall back to create on 404).
    """
    import time

    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload

    drive = _build_drive(creds)
    body: dict = {"mimeType": "application/vnd.google-apps.document"}
    if name:
        body["name"] = name

    last_err: Exception | None = None
    for attempt in range(1, 4):
        media = MediaFileUpload(str(docx), mimetype=DOCX_MIME, resumable=True)
        try:
            request = drive.files().update(
                fileId=document_id,
                body=body,
                media_body=media,
                fields="id",
            )
            response = None
            while response is None:
                _, response = request.next_chunk()
            return response["id"]
        except HttpError as e:
            last_err = e
            if e.resp.status in (500, 502, 503, 504) and attempt < 3:
                wait = 2 ** attempt
                print(f"  update attempt {attempt} failed ({e.resp.status}); retry in {wait}s")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"update failed after retries: {last_err}")


def share_with(creds, document_id: str, email: str) -> None:
    drive = _build_drive(creds)
    drive.permissions().create(
        fileId=document_id,
        body={"type": "user", "role": "writer", "emailAddress": email},
        sendNotificationEmail=False,
        fields="id",
    ).execute()


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def main() -> int:
    load_env()
    p = argparse.ArgumentParser()
    p.add_argument(
        "--template",
        default="intervention-review",
        choices=sorted(TEMPLATES.keys()),
        help="Which protocol template under templates/ to build (default: intervention-review)",
    )
    p.add_argument("--lang", required=True, choices=["ja", "en"])
    p.add_argument(
        "--folder-id",
        default=os.environ.get("DRIVE_FOLDER_ID"),
        help="Drive folder to place the Doc in (defaults to $DRIVE_FOLDER_ID from .env)",
    )
    p.add_argument("--name", default=None, help="Doc title (defaults to filename)")
    p.add_argument("--share-with", default=None, help="Grant writer access to this email")
    p.add_argument("--dry-run", action="store_true", help="Build docx (with comments) only; skip upload")
    p.add_argument("--author", default="SRWS-PSG", help="Author shown in Word/Docs comments")
    p.add_argument(
        "--doc-id",
        default=None,
        help="Overwrite this specific existing Google Doc ID (overrides cached ID)",
    )
    p.add_argument(
        "--new",
        action="store_true",
        help="Force creating a new Doc and overwrite the cached ID for this lang",
    )
    p.add_argument(
        "--no-save-id",
        action="store_true",
        help="Do not write the resulting Doc ID to tools/.gcp/upload_state.json",
    )
    args = p.parse_args()

    paths = _template_paths(args.template)
    src = master_path(paths, args.lang)
    if not src.exists():
        print(f"missing master: {src}", file=sys.stderr)
        return 2

    build_dir = paths["build_dir"]
    plain_docx = build_dir / f"{src.stem}.docx"
    build_docx(paths, src, plain_docx)

    comments = load_comments(paths, args.lang)
    print(f"loaded {len(comments)} comment(s) for template={args.template} lang={args.lang}")

    annotated_docx = build_dir / f"{src.stem}.with-comments.docx"
    results = inject_comments(plain_docx, annotated_docx, comments, author=args.author)
    matched = sum(1 for _, m in results if m)
    unmatched = [spec["id"] for spec, m in results if not m]
    print(f"injected {matched}/{len(results)} comments into docx")
    for cid in unmatched:
        print(f"  WARN anchor not matched for {cid}")

    if args.dry_run:
        print(f"docx: {annotated_docx}")
        return 0

    creds = get_credentials()
    name = args.name or f"{src.stem} ({args.lang})"

    state = load_upload_state()
    state_key = f"{args.template}:{args.lang}"  # cached Doc per (template, language)

    target_id: str | None = None
    if args.doc_id:  # explicit --doc-id wins
        target_id = args.doc_id
    elif not args.new:
        target_id = state.get(state_key)

    document_id: str
    if target_id:
        print(f"updating existing Doc {target_id} ({name!r}) ...")
        try:
            document_id = update_drive(creds, annotated_docx, target_id, name=name)
        except Exception as e:
            # Fall back to create if the cached/explicit ID is gone (404)
            from googleapiclient.errors import HttpError

            is_missing = isinstance(e, HttpError) and getattr(e.resp, "status", None) in (404, 410)
            if not is_missing:
                raise
            print(f"  cached Doc {target_id} not found; creating a new one")
            document_id = upload_to_drive(creds, annotated_docx, name=name, folder_id=args.folder_id)
    else:
        print(f"uploading to Drive as {name!r} ...")
        document_id = upload_to_drive(creds, annotated_docx, name=name, folder_id=args.folder_id)

    print(f"uploaded: https://docs.google.com/document/d/{document_id}/edit")

    if not args.no_save_id and state.get(state_key) != document_id:
        state[state_key] = document_id
        save_upload_state(state)
        print(f"saved Doc ID for template={args.template} lang={args.lang} -> {UPLOAD_STATE_FILE}")

    if args.share_with:
        share_with(creds, document_id, args.share_with)
        print(f"shared with {args.share_with}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
