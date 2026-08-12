"""Sync resources/training_lessons.json from the SRWS-PSG Slack training
curriculum Google Sheet, and offline-verify that comments.yaml `lessons:`
references still resolve against the committed snapshot.

Source: Google Sheet 1CGMC7-vhoTX7qB5FZknlr3exvG2xSOVzE9V8WGuicus, first
worksheet, range A:M (columns lesson_key, category, serial, title, course_id,
subcourse_id, released, hidden, deliverable, body_source, url, material_url,
exported_at). Column N (`body`) is Slack-workspace-only lesson content and is
never fetched: the range is hard-coded to A:M for exactly that reason.

Usage:
  python tools/sync_training_lessons.py                    # fetch + write resources/training_lessons.json
  python tools/sync_training_lessons.py --check             # offline: verify snapshot vs. templates/*/comments.yaml
  python tools/sync_training_lessons.py --check --remote    # also fetch the live sheet and report drift
  python tools/sync_training_lessons.py --snapshot PATH ... # point any of the above at an alternate snapshot

First-time setup: shares tools/build_gdoc.py's OAuth plumbing (see that
script's module docstring) -- `get_credentials()` is imported from there
rather than reimplemented, and its SCOPES already includes
https://www.googleapis.com/auth/spreadsheets.readonly. If tools/.gcp/token.json
was minted before that scope was added, delete it and re-run to re-consent.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_gdoc import get_credentials, load_env  # noqa: E402  (path setup above)
from training_lessons import (  # noqa: E402
    ROOT,
    LessonResolutionError,
    iter_comments_yaml_paths,
    load_comment_entries,
    load_snapshot,
    parse_lessons,
    resolve_comment_lessons,
    resolve_snapshot_path,
)

SOURCE_SPREADSHEET_ID = "1CGMC7-vhoTX7qB5FZknlr3exvG2xSOVzE9V8WGuicus"
SOURCE_RANGE = "A:M"  # deliberately excludes column N (`body`) -- see module docstring

# The sheet's header row uses these exact column names; we look them up by
# name (not position) so a reordered sheet doesn't silently scramble fields.
REQUIRED_COLUMNS = ("lesson_key", "category", "serial", "title", "course_id", "released")
EXPORTED_AT_COLUMN = "exported_at"


# --------------------------------------------------------------------------- #
# Fetch + write
# --------------------------------------------------------------------------- #


def fetch_lessons(creds) -> dict:
    """Fetch A:M from the training curriculum sheet and shape it into the
    snapshot dict (see the module docstring for the schema this returns).
    """
    from googleapiclient.discovery import build

    sheets = build("sheets", "v4", credentials=creds, cache_discovery=False)
    resp = (
        sheets.spreadsheets()
        .values()
        .get(spreadsheetId=SOURCE_SPREADSHEET_ID, range=SOURCE_RANGE)
        .execute()
    )
    rows = resp.get("values", [])
    if not rows:
        raise RuntimeError(f"sheet {SOURCE_SPREADSHEET_ID!r} range {SOURCE_RANGE!r} returned no rows")

    header = [h.strip() for h in rows[0]]

    # SOURCE_RANGE is a fixed 13-column window (A:M) chosen specifically to
    # stop one column short of `body` (column N, Slack-workspace-only lesson
    # content that must never be fetched or committed -- see module
    # docstring). That guarantee holds only as long as the sheet's column
    # order doesn't shift; if a column upstream is ever deleted, `body` slides
    # from N into M and would be silently fetched. So this is checked, not
    # assumed: fail loudly if `body` shows up anywhere in the header, or if
    # the last column isn't the expected `exported_at`.
    if "body" in header:
        raise RuntimeError(
            f"sheet header includes a 'body' column within range {SOURCE_RANGE!r}: "
            f"{header}. The sheet layout changed (a column was likely deleted "
            "upstream, shifting `body` into this range) -- SOURCE_RANGE needs "
            "revisiting before this can be trusted not to fetch lesson bodies."
        )
    if not header or header[-1] != EXPORTED_AT_COLUMN:
        raise RuntimeError(
            f"sheet header's last column is {header[-1] if header else None!r}, "
            f"expected {EXPORTED_AT_COLUMN!r}: {header}. The sheet layout changed "
            f"-- SOURCE_RANGE needs revisiting before this can be trusted not to "
            "fetch a lesson body if a column is inserted upstream."
        )

    col_index = {name: i for i, name in enumerate(header)}
    missing = [c for c in REQUIRED_COLUMNS if c not in col_index]
    if missing:
        raise RuntimeError(
            f"sheet header is missing expected column(s) {missing}; found {header}"
        )

    def cell(row: list[str], name: str) -> str:
        i = col_index.get(name)
        if i is None or i >= len(row):
            return ""
        return row[i].strip()

    lessons: list[dict] = []
    exported_ats: list[str] = []
    for row in rows[1:]:
        if not any(c.strip() for c in row):
            continue  # blank spacer row
        lesson_key = cell(row, "lesson_key")
        if not lesson_key:
            continue
        exported_at = cell(row, EXPORTED_AT_COLUMN)
        if exported_at:
            exported_ats.append(exported_at)
        lessons.append(
            {
                "lesson_key": lesson_key,
                "serial": cell(row, "serial"),
                "title": cell(row, "title"),
                "category": cell(row, "category"),
                "course_id": cell(row, "course_id"),
                "released": cell(row, "released"),
            }
        )

    lessons.sort(key=lambda l: (l["serial"], l["lesson_key"]))
    return {
        "source_spreadsheet_id": SOURCE_SPREADSHEET_ID,
        "source_range": SOURCE_RANGE,
        "feed_exported_at": max(exported_ats) if exported_ats else "",
        "lessons": lessons,
    }


def write_snapshot(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# --check (offline)
# --------------------------------------------------------------------------- #


def check_offline(snapshot: str | Path | None) -> list[str]:
    """Verify every `lessons:` ref in every templates/*/comments.yaml resolves
    against the given (or default) snapshot. Returns a list of failure
    messages (empty if everything resolves).
    """
    lessons = parse_lessons(load_snapshot(snapshot))
    failures: list[str] = []
    for comments_path in iter_comments_yaml_paths():
        rel = comments_path.relative_to(ROOT)
        for entry in load_comment_entries(comments_path):
            refs = entry.get("lessons") or []
            if not refs:
                continue
            comment_id = f"{rel}#{entry.get('id', '<missing id>')}"
            try:
                resolve_comment_lessons(comment_id, refs, lessons)
            except LessonResolutionError as e:
                failures.append(str(e))
    return failures


# --------------------------------------------------------------------------- #
# --check --remote (drift report)
# --------------------------------------------------------------------------- #


def diff_snapshot(committed: dict, live: dict) -> list[str]:
    """Human-readable list of differences between the committed snapshot and
    a freshly fetched one. Empty means no drift.

    `lesson_key` embeds the title (`category|serial|title`), so a plain
    key-based diff can't see a title change directly: a retitled lesson has a
    *different* lesson_key in the live fetch, so it looks like one lesson
    disappearing and an unrelated one appearing. To recover that signal, keys
    present in only one side are re-paired by (serial, course_id) -- which a
    retitle alone doesn't change -- and collapsed into a single "title
    changed" line; only genuinely unmatched keys are reported as a plain
    removal/addition.
    """
    committed_by_key = {l["lesson_key"]: l for l in committed.get("lessons", [])}
    live_by_key = {l["lesson_key"]: l for l in live.get("lessons", [])}

    diffs: list[str] = []

    # Field-level diffs for lessons whose key didn't change at all.
    for key in sorted(set(committed_by_key) & set(live_by_key)):
        old, new = committed_by_key[key], live_by_key[key]
        for field in ("serial", "title", "category", "course_id", "released"):
            if old.get(field) != new.get(field):
                diffs.append(
                    f"lesson {key!r}: {field} changed {old.get(field)!r} -> {new.get(field)!r}"
                )

    removed_keys = set(committed_by_key) - set(live_by_key)
    added_keys = set(live_by_key) - set(committed_by_key)

    # Re-pair removed/added keys that share (serial, course_id): almost
    # certainly the same lesson, retitled, rather than an unrelated swap.
    removed_by_serial_course: dict[tuple[str, str], list[str]] = {}
    for key in removed_keys:
        old = committed_by_key[key]
        removed_by_serial_course.setdefault((old.get("serial"), old.get("course_id")), []).append(key)

    matched_removed: set[str] = set()
    matched_added: set[str] = set()
    for key in sorted(added_keys):
        new = live_by_key[key]
        bucket = removed_by_serial_course.get((new.get("serial"), new.get("course_id")))
        if not bucket:
            continue
        old_key = bucket.pop(0)
        old = committed_by_key[old_key]
        diffs.append(
            f"lesson {new.get('serial')} ({new.get('course_id')}): title changed "
            f"{old.get('title')!r} -> {new.get('title')!r}"
        )
        matched_removed.add(old_key)
        matched_added.add(key)

    for key in sorted(removed_keys - matched_removed):
        old = committed_by_key[key]
        diffs.append(
            f"lesson {key!r} (serial={old.get('serial')!r}) is in the committed "
            f"snapshot but no longer in the sheet"
        )
    for key in sorted(added_keys - matched_added):
        new = live_by_key[key]
        diffs.append(
            f"lesson {key!r} (serial={new.get('serial')!r}) is in the sheet but not "
            f"yet synced to the committed snapshot"
        )
    return diffs


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    p.add_argument(
        "--check",
        action="store_true",
        help="Offline: verify comments.yaml `lessons:` refs resolve against the snapshot. No network.",
    )
    p.add_argument(
        "--remote",
        action="store_true",
        help="With --check, also fetch the live sheet and report drift from the committed snapshot.",
    )
    p.add_argument(
        "--snapshot",
        default=None,
        help=(
            "Snapshot path to read (--check) or write (sync). Default: "
            "resources/training_lessons.json, or $TRAINING_LESSONS_SNAPSHOT."
        ),
    )
    args = p.parse_args()

    if args.remote and not args.check:
        print("--remote only applies together with --check", file=sys.stderr)
        return 2

    if args.check:
        try:
            failures = check_offline(args.snapshot)
        except FileNotFoundError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2

        snapshot_path = resolve_snapshot_path(args.snapshot)
        if failures:
            print(f"FAILED: {len(failures)} `lessons:` reference(s) did not resolve:\n")
            for f in failures:
                print(f"  - {f}")
            return 1
        print(f"OK: all `lessons:` references resolve against {snapshot_path}")

        if args.remote:
            load_env()
            creds = get_credentials()
            print(f"fetching {SOURCE_RANGE} from spreadsheet {SOURCE_SPREADSHEET_ID} for drift check ...")
            live = fetch_lessons(creds)
            committed = load_snapshot(args.snapshot)
            drift = diff_snapshot(committed, live)
            if drift:
                print(f"\nDRIFT: committed snapshot differs from the live sheet ({len(drift)} change(s)):\n")
                for d in drift:
                    print(f"  - {d}")
                return 1
            print("OK: committed snapshot matches the live sheet")
        return 0

    # Default action: fetch the sheet and write the snapshot.
    load_env()
    creds = get_credentials()
    print(f"fetching {SOURCE_RANGE} from spreadsheet {SOURCE_SPREADSHEET_ID} ...")
    data = fetch_lessons(creds)
    out_path = resolve_snapshot_path(args.snapshot)
    write_snapshot(data, out_path)
    print(f"wrote {len(data['lessons'])} lesson(s) -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
