"""Shared resolver for SRWS-PSG Slack training-lesson references.

Both tools/build_gdoc.py (comment rendering) and tools/sync_training_lessons.py
(snapshot sync + offline verification) need the same three things, so they
live here instead of being duplicated:

  1. Loading the training-lesson snapshot (resources/training_lessons.json,
     synced from the Slack training curriculum Google Sheet).
  2. Resolving a `lessons:` entry from comments.yaml to the matching lesson
     row(s), in one of three forms:
       - a serial prefix (segment-boundary match, see `_matches_prefix`):
         prefix "03_10" matches serial "03_10" itself and "03_10_2", but
         prefix "03_1" does NOT match serial "03_10" (no shared "_" boundary
         right after "03_1").
       - "=<serial>": exact serial equality, no prefix descent.
       - "key:<lesson_key>": exact `lesson_key` match, regardless of serial.
  3. Rendering the resolved, released-only lessons into the Japanese "related
     training" text block embedded in the rendered comment body (category +
     serial + title per lesson; never course_id, never the lesson body text).

`serial` is not unique in the sheet: a lesson can be re-recorded under a new
`lesson_key` (e.g. while its content is being revised) while keeping the old
serial, so a serial can have both a released and an unreleased row at once.
Resolution therefore filters each ref's matches down to `released == "yes"`
before rendering (see `resolve_comment_lessons`): an unreleased duplicate
never reaches a rendered comment, but a released sibling with the same serial
still resolves cleanly.

Snapshot path resolution order: an explicit path argument, then the
TRAINING_LESSONS_SNAPSHOT env var (mainly for pointing tests at a fixture
without touching the committed file), then the default
resources/training_lessons.json.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

try:
    import yaml
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]

SNAPSHOT_ENV_VAR = "TRAINING_LESSONS_SNAPSHOT"
DEFAULT_SNAPSHOT_PATH = ROOT / "resources" / "training_lessons.json"

# The per-row columns kept in the snapshot. Deliberately excludes the sheet's
# `exported_at` and `body` columns -- see tools/sync_training_lessons.py for why.
LESSON_ROW_FIELDS = ("lesson_key", "serial", "title", "category", "course_id", "released")

TRAINING_HEADER_JA = "関連するトレーニング（SRWS-PSG Slack の /training から受講できます）:"


@dataclass(frozen=True)
class Lesson:
    lesson_key: str
    serial: str
    title: str
    category: str
    course_id: str
    released: str

    def as_dict(self) -> dict[str, str]:
        return {field: getattr(self, field) for field in LESSON_ROW_FIELDS}


class LessonResolutionError(RuntimeError):
    """A `lessons:` entry in comments.yaml did not resolve cleanly.

    Raised for a ref (prefix, "=serial", or "key:lesson_key") that matches
    zero lessons at all, or that matches lessons but none of them are
    released yet. Meant to fail a build loudly rather than publish a link to
    an unreleased or nonexistent lesson.
    """


# --------------------------------------------------------------------------- #
# Snapshot loading
# --------------------------------------------------------------------------- #


def resolve_snapshot_path(override: str | Path | None = None) -> Path:
    """Resolve the snapshot path: explicit override > env var > default."""
    if override:
        return Path(override)
    env = os.environ.get(SNAPSHOT_ENV_VAR)
    if env:
        return Path(env)
    return DEFAULT_SNAPSHOT_PATH


def load_snapshot(path: str | Path | None = None) -> dict:
    """Load and parse the training-lesson snapshot JSON.

    Raises FileNotFoundError with a pointer to `sync_training_lessons.py` if
    the snapshot is missing, and ValueError if it isn't valid JSON.
    """
    p = resolve_snapshot_path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"training-lesson snapshot not found: {p}\n"
            "Run `python tools/sync_training_lessons.py` to fetch it, or set "
            f"${SNAPSHOT_ENV_VAR} / pass --snapshot to point at a fixture."
        )
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"invalid training-lesson snapshot at {p}: {e}") from e


def parse_lessons(snapshot: dict) -> list[Lesson]:
    """Turn a parsed snapshot dict's `lessons` array into Lesson records.

    Policy: every field is read with `.get(field, "")`, never `row[field]` --
    a hand-edited fixture or a future snapshot format change should degrade
    to an empty (and thus non-matching, non-"yes") field rather than a raw
    KeyError.
    """
    out: list[Lesson] = []
    for row in snapshot.get("lessons", []):
        out.append(
            Lesson(
                lesson_key=row.get("lesson_key", ""),
                serial=row.get("serial", ""),
                title=row.get("title", ""),
                category=row.get("category", ""),
                course_id=row.get("course_id", ""),
                released=row.get("released", ""),
            )
        )
    return out


def load_lessons(path: str | Path | None = None) -> list[Lesson]:
    """Convenience: load_snapshot() + parse_lessons() in one call."""
    return parse_lessons(load_snapshot(path))


# --------------------------------------------------------------------------- #
# Prefix resolution
# --------------------------------------------------------------------------- #


def _matches_prefix(serial: str, prefix: str) -> bool:
    """Segment-boundary match: `serial` == `prefix`, or starts with `prefix + "_"`.

    So prefix "03_1" does NOT match serial "03_10" (there is no "_" right
    after "03_1" in "03_10"), but prefix "03_10" DOES match serial "03_10"
    and "03_10_2".
    """
    return serial == prefix or serial.startswith(prefix + "_")


def resolve_lesson_ref(ref: str, lessons: Sequence[Lesson]) -> list[Lesson]:
    """Resolve one `lessons:` array element to the lessons it matches.

    Three ref forms, tried in this order:
      - "key:<lesson_key>": exact `lesson_key` match.
      - "=<serial>": exact `serial` equality, no prefix descent.
      - anything else: a serial prefix (segment-boundary match, see
        `_matches_prefix`).
    Returns matches sorted by (serial, lesson_key); may be empty. This
    includes unreleased matches -- filtering those out is
    `resolve_comment_lessons`'s job, not this function's, so that it can tell
    "zero lessons at all" apart from "matched, but none released".
    """
    if ref.startswith("key:"):
        key = ref[len("key:"):]
        matches = [lesson for lesson in lessons if lesson.lesson_key == key]
    elif ref.startswith("="):
        serial = ref[1:]
        matches = [lesson for lesson in lessons if lesson.serial == serial]
    else:
        matches = [lesson for lesson in lessons if _matches_prefix(lesson.serial, ref)]
    return sorted(matches, key=lambda lesson: (lesson.serial, lesson.lesson_key))


def resolve_comment_lessons(
    comment_id: str, refs: Sequence[str], lessons: Sequence[Lesson]
) -> list[Lesson]:
    """Resolve every `lessons:` ref of one comment entry to its lesson set.

    Each ref is resolved, then filtered down to `released == "yes"` matches
    -- `serial` is not unique in the sheet (a lesson can be re-recorded under
    a new lesson_key while keeping its old serial), so this filtering is what
    disambiguates a duplicated serial down to the intended, released lesson.

    Dedups by lesson_key across refs (the same lesson could in principle be
    reachable via two overlapping refs) and returns the result sorted by
    ascending serial, per the comment-body contract -- this is independent of
    the order `refs` were listed in comments.yaml, which is preserved there
    for provenance (e.g. multi-prefix entries migrated from a single legacy
    Facebook post).

    Raises LessonResolutionError, naming `comment_id` and the offending ref,
    in two distinct cases:
      - the ref matched zero lessons at all (typo, or the lesson was removed
        from the curriculum).
      - the ref matched one or more lessons, but none of them are released
        yet (the common case for a duplicated serial: the released row is
        filtered in, the unreleased one filtered out; this fires only when
        *every* match for that ref is unreleased).
    """
    resolved: dict[str, Lesson] = {}
    for ref in refs:
        matches = resolve_lesson_ref(ref, lessons)
        if not matches:
            raise LessonResolutionError(
                f"comment {comment_id!r}: lessons ref {ref!r} resolved to 0 lessons"
            )
        released_matches = [lesson for lesson in matches if lesson.released == "yes"]
        if not released_matches:
            listing = ", ".join(
                f"{lesson.lesson_key!r} (serial={lesson.serial!r}, released={lesson.released!r})"
                for lesson in matches
            )
            raise LessonResolutionError(
                f"comment {comment_id!r}: lessons ref {ref!r} resolved to {len(matches)} "
                f"lesson(s), none of which are released yet: {listing}"
            )
        for lesson in released_matches:
            resolved[lesson.lesson_key] = lesson
    return sorted(resolved.values(), key=lambda lesson: (lesson.serial, lesson.lesson_key))


# --------------------------------------------------------------------------- #
# Comment body rendering
# --------------------------------------------------------------------------- #


def generate_lesson_block(lessons: Sequence[Lesson]) -> str:
    """Render the resolved lessons as the Japanese "related training" block.

    Deliberately renders only category + serial + title. The comment body is
    Japanese prose, so the Japanese course name (`category`, e.g. "SRWSプロト
    コル登録まで") reads better and matches what people see in Slack --
    `course_id` (an English slug, e.g. "sr-protocol") is kept in the snapshot
    for drift detection but never shown here. The lesson body text is never
    rendered either: these templates are published on protocols.io, and
    lesson bodies are for Slack workspace members only.
    """
    lines = [TRAINING_HEADER_JA]
    lines.extend(f"・[{lesson.category} {lesson.serial}] {lesson.title}" for lesson in lessons)
    return "\n".join(lines)


def render_comment_body(lessons: Sequence[Lesson], extra_body: str | None) -> str:
    """Combine the generated lesson block with optional hand-written body text.

    - lessons only -> the generated block.
    - lessons + extra_body -> generated block, blank line, then extra_body.
    (An entry with no lessons is not this function's concern; callers keep
    using `extra_body` verbatim in that case.)
    """
    block = generate_lesson_block(lessons)
    if extra_body and extra_body.strip():
        return f"{block}\n\n{extra_body.rstrip()}"
    return block


# --------------------------------------------------------------------------- #
# comments.yaml loading (used by sync_training_lessons.py's --check)
# --------------------------------------------------------------------------- #


def iter_comments_yaml_paths(root: Path = ROOT) -> list[Path]:
    """All templates/*/comments.yaml paths, sorted for deterministic output."""
    return sorted((root / "templates").glob("*/comments.yaml"))


def load_comment_entries(comments_yaml: Path) -> list[dict]:
    """Parse one comments.yaml file into its raw `comments:` list of dicts."""
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install -r tools/requirements.txt")
    data = yaml.safe_load(comments_yaml.read_text(encoding="utf-8")) or {}
    return data.get("comments", [])
