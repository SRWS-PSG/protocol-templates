"""Upload the companion paper (paper/manuscript) to Google Drive as a Doc.

The 3 protocol templates are published to a shared Drive folder via
build_gdoc.py. This script does the same for the companion article so
co-authors can review it alongside the templates: it builds the docx via
paper/build.ps1, then uploads it as a Google Doc into the SAME folder
(DRIVE_FOLDER_ID), inheriting that folder's sharing.

Unlike the templates, the paper has no comments.yaml, so no comments are
injected -- it is a plain manuscript for review.

Default behavior mirrors build_gdoc.py: delete-and-recreate. A fresh Doc is
created in the folder (inheriting folder sharing) and the previously uploaded
Doc (cached in tools/.gcp/upload_state.json under "paper:<lang>") is trashed,
so the file never accumulates stale copies. Share the FOLDER, not per-file
links, because the ID/URL changes each run.

Usage:
  python tools/upload_paper.py                       # build (if needed) + upload en
  python tools/upload_paper.py --lang ja             # upload the JA mirror if present
  python tools/upload_paper.py --no-build            # use existing paper/build/*.docx
  python tools/upload_paper.py --share-with a@b.com  # also grant writer to an email
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_gdoc as bg

ROOT = Path(__file__).resolve().parents[1]
PAPER_DIR = ROOT / "paper"


def build_docx(lang: str) -> Path:
    base = "manuscript" if lang == "en" else f"manuscript.{lang}"
    out = PAPER_DIR / "build" / f"{base}.docx"
    script = PAPER_DIR / "build.ps1"
    cmd = ["pwsh", "-NoProfile", "-File", str(script), "-Target", "docx", "-Lang", lang]
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)
    if not out.exists():
        raise SystemExit(f"expected docx not produced: {out}")
    return out


def main() -> int:
    bg.load_env()
    p = argparse.ArgumentParser()
    p.add_argument("--lang", default="en", choices=["en", "ja"])
    p.add_argument("--folder-id", default=os.environ.get("DRIVE_FOLDER_ID"))
    p.add_argument("--name", default=None, help="Doc title (defaults to a descriptive name)")
    p.add_argument("--share-with", default=None, help="Grant writer access to this email")
    p.add_argument("--no-build", action="store_true", help="Use existing paper/build/*.docx")
    p.add_argument("--dry-run", action="store_true", help="Build only; skip upload")
    args = p.parse_args()

    base = "manuscript" if args.lang == "en" else f"manuscript.{args.lang}"
    docx = PAPER_DIR / "build" / f"{base}.docx"
    if not args.no_build:
        docx = build_docx(args.lang)
    elif not docx.exists():
        print(f"missing docx (drop --no-build to build it): {docx}", file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"docx: {docx}")
        return 0

    if not args.folder_id:
        print(
            "upload requires a folder so the Doc inherits folder sharing; set "
            "--folder-id or DRIVE_FOLDER_ID in tools/.env",
            file=sys.stderr,
        )
        return 2

    name = args.name or "SRWS-PSG protocol templates -- companion article (manuscript)"
    if args.lang != "en":
        name += f" ({args.lang})"

    creds = bg.get_credentials()
    state = bg.load_upload_state()
    state_key = f"paper:{args.lang}"
    old_id = state.get(state_key)

    print(f"creating a fresh Doc {name!r} in folder {args.folder_id} ...")
    document_id = bg.upload_to_drive(creds, docx, name=name, folder_id=args.folder_id)

    if old_id and old_id != document_id:
        try:
            bg.trash_drive(creds, old_id)
            print(f"  trashed old Doc {old_id} (recoverable from Trash ~30 days)")
        except Exception as e:
            print(f"  WARN could not trash old Doc {old_id}: {e}")

    if args.share_with:
        bg.share_with(creds, document_id, args.share_with)
        print(f"  shared with {args.share_with} (writer)")

    state[state_key] = document_id
    bg.save_upload_state(state)

    print(f"Doc ID: {document_id}")
    print(f"URL:    https://docs.google.com/document/d/{document_id}/edit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
