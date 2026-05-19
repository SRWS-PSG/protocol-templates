"""Render a protocol master Markdown to Google Docs and attach comments.

Pipeline:
  1. Read the language-specific master (e.g. protocol_template...ja.md).
  2. Read comments.yaml and select the matching language anchor.
  3. Pandoc md -> docx (uses references.bib + vancouver.csl).
  4. Drive API: upload docx with mimeType=application/vnd.google-apps.document
     so it is auto-converted to a Google Doc.
  5. Docs API: locate each anchor string in the rendered body, get its
     startIndex/endIndex, and call drive.comments.create to attach.

First-time setup:
  1. pip install -r tools/requirements.txt
  2. Create an OAuth Desktop client at
       https://console.cloud.google.com/apis/credentials
     (Enable Drive API + Docs API for the project first.)
  3. Download the client secret JSON and save it to
       tools/.gcp/credentials.json
  4. Run `python tools/build_gdoc.py --lang ja` — a browser window opens for
     the OAuth consent. The refresh token is cached at tools/.gcp/token.json.

Usage:
  python tools/build_gdoc.py --lang ja
  python tools/build_gdoc.py --lang en --folder-id <Drive folder id>
  python tools/build_gdoc.py --lang ja --dry-run     # build docx only, skip upload
  python tools/build_gdoc.py --lang ja --share-with someone@example.com
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml  # PyYAML
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates" / "intervention-review"
COMMENTS_YAML = TEMPLATE_DIR / "comments.yaml"
BIB = TEMPLATE_DIR / "references.bib"
CSL = TEMPLATE_DIR / "vancouver.csl"
BUILD_DIR = TEMPLATE_DIR / "build"

GCP_DIR = ROOT / "tools" / ".gcp"
CREDENTIALS_FILE = GCP_DIR / "credentials.json"
TOKEN_FILE = GCP_DIR / "token.json"

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]


@dataclass
class CommentSpec:
    id: str
    anchor: str
    body: str
    occurrence: int = 1


# --------------------------------------------------------------------------- #
# Master + comment loading
# --------------------------------------------------------------------------- #


def master_path(lang: str) -> Path:
    if lang == "en":
        return TEMPLATE_DIR / "protocol_template_for_intervention_review.md"
    return TEMPLATE_DIR / f"protocol_template_for_intervention_review.{lang}.md"


def load_comments(lang: str) -> list[CommentSpec]:
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install -r tools/requirements.txt")
    data = yaml.safe_load(COMMENTS_YAML.read_text(encoding="utf-8"))
    specs: list[CommentSpec] = []
    for entry in data.get("comments", []):
        anchor = (entry.get("anchor") or {}).get(lang)
        body = entry.get("body")
        if not anchor or not body:
            continue
        specs.append(
            CommentSpec(
                id=entry["id"],
                anchor=anchor,
                body=body.rstrip(),
                occurrence=int(entry.get("occurrence", 1)),
            )
        )
    return specs


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
        "--standalone",
        "-o",
        str(out),
    ]
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)


# --------------------------------------------------------------------------- #
# Google auth
# --------------------------------------------------------------------------- #


def get_credentials():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if not CREDENTIALS_FILE.exists():
            raise FileNotFoundError(
                f"OAuth client secret not found at {CREDENTIALS_FILE}.\n"
                "  1. Enable Drive API and Docs API at https://console.cloud.google.com/apis/library\n"
                "  2. Create an OAuth 2.0 Desktop client at https://console.cloud.google.com/apis/credentials\n"
                "  3. Download the JSON and save it as the path above."
            )
        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
        creds = flow.run_local_server(port=0)
    GCP_DIR.mkdir(parents=True, exist_ok=True)
    TOKEN_FILE.write_text(creds.to_json())
    return creds


# --------------------------------------------------------------------------- #
# Drive + Docs operations
# --------------------------------------------------------------------------- #


def _build_services(creds):
    from googleapiclient.discovery import build

    drive = build("drive", "v3", credentials=creds, cache_discovery=False)
    docs = build("docs", "v1", credentials=creds, cache_discovery=False)
    return drive, docs


def upload_to_drive(creds, docx: Path, name: str, folder_id: str | None) -> str:
    """Upload docx as a Google Doc (auto-converted). Returns documentId."""
    from googleapiclient.http import MediaFileUpload

    drive, _ = _build_services(creds)
    media = MediaFileUpload(
        str(docx),
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        resumable=False,
    )
    body = {
        "name": name,
        "mimeType": "application/vnd.google-apps.document",
    }
    if folder_id:
        body["parents"] = [folder_id]
    f = drive.files().create(body=body, media_body=media, fields="id").execute()
    return f["id"]


def _iter_text_runs(doc: dict):
    """Yield (startIndex, content) for every textRun in the document body."""

    def walk(elements):
        for el in elements:
            if "paragraph" in el:
                for pe in el["paragraph"].get("elements", []):
                    tr = pe.get("textRun")
                    if tr and "content" in tr and "startIndex" in pe:
                        yield pe["startIndex"], tr["content"]
            elif "table" in el:
                for row in el["table"].get("tableRows", []):
                    for cell in row.get("tableCells", []):
                        yield from walk(cell.get("content", []))

    yield from walk(doc.get("body", {}).get("content", []))


def find_anchor_ranges(
    creds, document_id: str, comments: list[CommentSpec]
) -> list[tuple[CommentSpec, int, int]]:
    """For each comment, locate its anchor in the live Doc and return doc-index ranges."""
    _, docs = _build_services(creds)
    doc = docs.documents().get(documentId=document_id).execute()

    # Build a flat string + a parallel array mapping str-position -> doc-startIndex.
    chunks: list[str] = []
    pos_to_doc: list[int] = []
    for start_idx, content in _iter_text_runs(doc):
        chunks.append(content)
        pos_to_doc.extend(range(start_idx, start_idx + len(content)))
    full_text = "".join(chunks)

    out: list[tuple[CommentSpec, int, int]] = []
    for spec in comments:
        idx = -1
        for _ in range(spec.occurrence):
            idx = full_text.find(spec.anchor, idx + 1)
            if idx < 0:
                break
        if idx < 0:
            print(f"  WARN anchor not found in Doc for {spec.id}: {spec.anchor!r}")
            continue
        end_pos = idx + len(spec.anchor) - 1
        if end_pos >= len(pos_to_doc):
            print(f"  WARN anchor end out of range for {spec.id}")
            continue
        out.append((spec, pos_to_doc[idx], pos_to_doc[end_pos] + 1))
    return out


def _get_head_revision(drive, document_id: str) -> str:
    revs = drive.revisions().list(fileId=document_id, fields="revisions(id)").execute()
    items = revs.get("revisions", [])
    if not items:
        raise RuntimeError("no revisions found for document")
    return items[-1]["id"]


def create_comments(
    creds, document_id: str, ranges: list[tuple[CommentSpec, int, int]]
) -> int:
    """Create anchored comments via the Drive comments API."""
    from googleapiclient.errors import HttpError

    drive, _ = _build_services(creds)
    revision_id = _get_head_revision(drive, document_id)
    created = 0
    for spec, start, end in ranges:
        anchor_json = json.dumps(
            {"r": revision_id, "a": [{"txt": {"o": start, "l": end - start}}]},
            ensure_ascii=False,
        )
        try:
            drive.comments().create(
                fileId=document_id,
                body={"content": spec.body, "anchor": anchor_json},
                fields="id",
            ).execute()
            created += 1
        except HttpError as e:
            print(f"  WARN anchored create failed for {spec.id}: {e}")
            # Fallback: unanchored comment with the anchor text quoted in the body.
            try:
                drive.comments().create(
                    fileId=document_id,
                    body={"content": f"[anchor: {spec.anchor!r}]\n\n{spec.body}"},
                    fields="id",
                ).execute()
                created += 1
            except HttpError as e2:
                print(f"    fallback also failed: {e2}")
    return created


def share_with(creds, document_id: str, email: str) -> None:
    drive, _ = _build_services(creds)
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
    p = argparse.ArgumentParser()
    p.add_argument("--lang", required=True, choices=["ja", "en"])
    p.add_argument("--folder-id", default=None, help="Drive folder to place the Doc in")
    p.add_argument("--name", default=None, help="Doc title (defaults to filename)")
    p.add_argument("--share-with", default=None, help="Grant writer access to this email")
    p.add_argument("--dry-run", action="store_true", help="Build docx only; skip upload + comments")
    args = p.parse_args()

    src = master_path(args.lang)
    if not src.exists():
        print(f"missing master: {src}", file=sys.stderr)
        return 2

    docx = BUILD_DIR / f"{src.stem}.docx"
    build_docx(src, docx)

    comments = load_comments(args.lang)
    print(f"loaded {len(comments)} comment(s) for lang={args.lang}")

    if args.dry_run:
        print(f"docx: {docx}")
        print("dry-run: skipping Drive upload and comment placement")
        return 0

    creds = get_credentials()
    name = args.name or f"{src.stem} ({args.lang})"
    print(f"uploading to Drive as {name!r} ...")
    document_id = upload_to_drive(creds, docx, name=name, folder_id=args.folder_id)
    print(f"uploaded: https://docs.google.com/document/d/{document_id}/edit")

    ranges = find_anchor_ranges(creds, document_id, comments)
    print(f"resolved {len(ranges)}/{len(comments)} anchor ranges")

    n = create_comments(creds, document_id, ranges)
    print(f"created {n} comment(s)")

    if args.share_with:
        share_with(creds, document_id, args.share_with)
        print(f"shared with {args.share_with}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
