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
"""

from __future__ import annotations

import argparse
import os
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
TEMPLATE_DIR = ROOT / "templates" / "intervention-review"
COMMENTS_YAML = TEMPLATE_DIR / "comments.yaml"
BIB = TEMPLATE_DIR / "references.bib"
CSL = TEMPLATE_DIR / "vancouver.csl"
BUILD_DIR = TEMPLATE_DIR / "build"
LUA_FILTER = TEMPLATE_DIR / "filters" / "highlight.lua"
REFERENCE_DOCX = TEMPLATE_DIR / "filters" / "reference.docx"

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

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/documents",
]


# --------------------------------------------------------------------------- #
# Master + comment loading
# --------------------------------------------------------------------------- #


def master_path(lang: str) -> Path:
    if lang == "en":
        return TEMPLATE_DIR / "protocol_template_for_intervention_review.md"
    return TEMPLATE_DIR / f"protocol_template_for_intervention_review.{lang}.md"


def load_comments(lang: str) -> list[dict]:
    """Load comments applicable to the given language as plain dicts.

    Returns dicts with keys: id, anchor (str), body (str), occurrence (int).
    The body is a single Japanese string shared across languages; only the
    anchor text differs per master file.
    """
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install -r tools/requirements.txt")
    data = yaml.safe_load(COMMENTS_YAML.read_text(encoding="utf-8"))
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


def build_docx(src: Path, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc",
        str(src),
        "--from=markdown",
        "--to=docx",
        "--citeproc",
        f"--bibliography={BIB}",
        f"--csl={CSL}",
        f"--lua-filter={LUA_FILTER}",
        "--standalone",
        "-o",
        str(out),
    ]
    if REFERENCE_DOCX.exists():
        cmd.insert(-2, f"--reference-doc={REFERENCE_DOCX}")
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)


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
    """Upload docx as a Google Doc (auto-converted). Returns documentId."""
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
        media = MediaFileUpload(
            str(docx),
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            resumable=True,
        )
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
    args = p.parse_args()

    src = master_path(args.lang)
    if not src.exists():
        print(f"missing master: {src}", file=sys.stderr)
        return 2

    plain_docx = BUILD_DIR / f"{src.stem}.docx"
    build_docx(src, plain_docx)

    comments = load_comments(args.lang)
    print(f"loaded {len(comments)} comment(s) for lang={args.lang}")

    annotated_docx = BUILD_DIR / f"{src.stem}.with-comments.docx"
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
    print(f"uploading to Drive as {name!r} ...")
    document_id = upload_to_drive(creds, annotated_docx, name=name, folder_id=args.folder_id)
    print(f"uploaded: https://docs.google.com/document/d/{document_id}/edit")

    if args.share_with:
        share_with(creds, document_id, args.share_with)
        print(f"shared with {args.share_with}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
