#!/usr/bin/env python3
"""Fail if a template master hard-codes `version:` or `date:` in its YAML frontmatter.

The version and date shown in builds are derived from git tags by
tools/template_version.py, so they must not be written in the masters.

Usage:
  python tools/check_no_hardcoded_version.py

Exit status: 0 if no master has the keys, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
FORBIDDEN = re.compile(r"^(version|date)\s*:", re.M)


def main() -> int:
    masters = sorted(ROOT.glob("templates/*/protocol_template_*.md"))
    if not masters:
        print("error: no template masters found", file=sys.stderr)
        return 1
    bad = 0
    for path in masters:
        m = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        if not m:
            continue
        for key in sorted({k.group(1) for k in FORBIDDEN.finditer(m.group(1))}):
            print(f"{path.relative_to(ROOT)}: frontmatter contains '{key}:'")
            bad += 1
    if bad:
        print(
            "Remove them: version and date are derived from git tags at build time "
            "(tools/template_version.py).",
            file=sys.stderr,
        )
        return 1
    print(f"ok: {len(masters)} masters have no version/date in frontmatter")
    return 0


if __name__ == "__main__":
    sys.exit(main())
