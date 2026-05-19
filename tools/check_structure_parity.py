"""Structural parity check between the Japanese and English protocol masters.

Fails (exit 1) if the two files have diverged on any of:
  - heading level sequence
  - bilingual placeholder slots `[english / 日本語: ...]`
  - fenced code block count
  - citation key set `[@key]`
  - YAML frontmatter keys (excluding language-specific ones)
  - comment anchors in comments.yaml (must resolve in their target master)

Run:
  python tools/check_structure_parity.py templates/intervention-review/protocol_template_for_intervention_review.md \
                                         templates/intervention-review/protocol_template_for_intervention_review.ja.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
# Bilingual placeholder `[english label / 日本語ラベル: ...]`. The negative
# lookahead `(?!\()` excludes markdown links like `[url](url)` whose bracket
# text incidentally contains `/` and `:`.
PLACEHOLDER_RE = re.compile(r"\[([^\[\]\n]+?/[^\[\]\n]+?:[^\[\]\n]*?)\](?!\()")
FENCE_RE = re.compile(r"^```", re.MULTILINE)
CITATION_RE = re.compile(r"\[@([A-Za-z0-9_\-:]+(?:;\s*@[A-Za-z0-9_\-:]+)*)\]")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
LANG_ONLY_KEYS = {"lang", "title", "date"}


def strip_blockquotes(text: str) -> str:
    # Headings inside blockquotes (`> #`) are illustrative, not real sections.
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith(">"))


def parse_headings(text: str) -> list[int]:
    return [len(m.group(1)) for m in HEADING_RE.finditer(strip_blockquotes(text))]


def parse_placeholders(text: str) -> int:
    return len(PLACEHOLDER_RE.findall(text))


def parse_fence_count(text: str) -> int:
    return len(FENCE_RE.findall(text)) // 2


def parse_citations(text: str) -> set[str]:
    keys: set[str] = set()
    for m in CITATION_RE.finditer(text):
        for piece in m.group(1).split(";"):
            keys.add(piece.strip().lstrip("@"))
    return keys


def parse_frontmatter_keys(text: str) -> set[str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return set()
    keys: set[str] = set()
    for line in m.group(1).splitlines():
        if line and not line.startswith(" ") and not line.startswith("-") and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys - LANG_ONLY_KEYS


def diff_report(label: str, a, b) -> str | None:
    if a == b:
        return None
    return f"[{label}] mismatch:\n  en: {a!r}\n  ja: {b!r}"


def check_comment_anchors(en_text: str, ja_text: str, comments_path: Path) -> list[str]:
    if not comments_path.exists():
        return []
    try:
        import yaml  # local import so the parity check works without PyYAML
    except ImportError:
        return [f"[comment anchors] skipped: PyYAML not installed"]
    data = yaml.safe_load(comments_path.read_text(encoding="utf-8")) or {}
    failures: list[str] = []
    for c in data.get("comments", []):
        anchor = c.get("anchor") or {}
        occ = int(c.get("occurrence", 1))
        for lang_key, text in (("ja", ja_text), ("en", en_text)):
            a = anchor.get(lang_key)
            if not a:
                continue
            if text.count(a) < occ:
                failures.append(
                    f"[comment {c.get('id')!r}] anchor not found {occ}x in {lang_key}: {a!r}"
                )
    return failures


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    en_path, ja_path = Path(sys.argv[1]), Path(sys.argv[2])
    en, ja = en_path.read_text(encoding="utf-8"), ja_path.read_text(encoding="utf-8")

    failures: list[str] = []

    en_headings, ja_headings = parse_headings(en), parse_headings(ja)
    if (msg := diff_report("heading levels", en_headings, ja_headings)):
        failures.append(msg)

    en_ph, ja_ph = parse_placeholders(en), parse_placeholders(ja)
    if (msg := diff_report("placeholder count", en_ph, ja_ph)):
        failures.append(msg)

    en_fences, ja_fences = parse_fence_count(en), parse_fence_count(ja)
    if (msg := diff_report("code block count", en_fences, ja_fences)):
        failures.append(msg)

    en_cites, ja_cites = parse_citations(en), parse_citations(ja)
    only_en = en_cites - ja_cites
    only_ja = ja_cites - en_cites
    if only_en or only_ja:
        failures.append(
            f"[citation keys] mismatch:\n  only en: {sorted(only_en)}\n  only ja: {sorted(only_ja)}"
        )

    en_fm, ja_fm = parse_frontmatter_keys(en), parse_frontmatter_keys(ja)
    if (msg := diff_report("frontmatter keys", sorted(en_fm), sorted(ja_fm))):
        failures.append(msg)

    failures.extend(check_comment_anchors(en, ja, en_path.parent / "comments.yaml"))

    if failures:
        print("Structural parity check FAILED:\n")
        for f in failures:
            print(f)
            print()
        return 1

    print(
        f"OK: headings={len(en_headings)}, placeholders={en_ph}, "
        f"code_blocks={en_fences}, citations={len(en_cites)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
