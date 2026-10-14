#!/usr/bin/env python3
"""Single source of truth for the version and date shown in rendered templates.

The version is derived from git tags (each GitHub release is a tag and a
Zenodo version DOI); nothing is written into the template YAML.

Lookup order:
  1. git checkout: ``git describe --tags --always --dirty`` and the committer
     date of HEAD (``git log -1 --format=%cs``).
  2. Source archive (GitHub/Zenodo zip): ``tools/VERSION``, whose
     ``$Format:...$`` placeholders are substituted by ``git archive`` through
     the ``export-subst`` attribute in ``.gitattributes``.
  3. Otherwise version ``unknown`` and a warning on stderr; never an error.

CLI (used by templates/*/build.ps1):
  python tools/template_version.py version   # e.g. v3.1.1-17-gc9e3e17
  python tools/template_version.py date      # e.g. 2026-09-14
  python tools/template_version.py title-date  # e.g. 2026-09-14 (v3.1.1-17-gc9e3e17)

Python callers: ``from template_version import pandoc_metadata_args``.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = Path(__file__).resolve().parent / "VERSION"


def _git(*args: str) -> str | None:
    try:
        res = subprocess.run(
            ["git", "-C", str(REPO_ROOT), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, ValueError):
        return None
    out = res.stdout.strip()
    if res.returncode != 0 or not out:
        return None
    return out


def _from_git() -> tuple[str, str] | None:
    # A source zip unpacked inside some other repository must not pick up that
    # repository's tags: only trust git when this repo is the work-tree root.
    top = _git("rev-parse", "--show-toplevel")
    if not top or Path(top).resolve() != REPO_ROOT:
        return None
    version = _git("describe", "--tags", "--always", "--dirty")
    date = _git("log", "-1", "--format=%cs")
    if version and date:
        return version, date
    return None


def _from_version_file() -> tuple[str, str] | None:
    try:
        lines = [
            ln.strip()
            for ln in VERSION_FILE.read_text(encoding="utf-8").splitlines()
            if ln.strip()
        ]
    except OSError:
        return None
    if len(lines) < 2 or any("$Format:" in ln for ln in lines[:2]):
        return None
    return lines[0], lines[1]


def get_version_metadata() -> dict[str, str]:
    """Return ``{"version": ..., "date": ...}``; version is ``unknown`` if neither source works."""
    found = _from_git() or _from_version_file()
    if found:
        return {"version": found[0], "date": found[1]}
    print(
        "warning: could not determine the template version (not a git checkout "
        "and tools/VERSION was not substituted); using 'unknown'.",
        file=sys.stderr,
    )
    return {"version": "unknown", "date": ""}


def title_date(meta: dict[str, str]) -> str:
    """Text for the title-block date line, which also carries the version."""
    if meta["date"]:
        return f"{meta['date']} ({meta['version']})"
    return meta["version"]


def pandoc_metadata_args() -> list[str]:
    """Pandoc ``-M`` arguments carrying the derived version and date."""
    meta = get_version_metadata()
    return ["-M", f"version={meta['version']}", "-M", f"date={title_date(meta)}"]


def main(argv: list[str]) -> int:
    field = argv[1] if len(argv) > 1 else "version"
    meta = get_version_metadata()
    if field == "version":
        print(meta["version"])
    elif field == "date":
        print(meta["date"])
    elif field == "title-date":
        print(title_date(meta))
    else:
        print("usage: template_version.py [version|date|title-date]", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
