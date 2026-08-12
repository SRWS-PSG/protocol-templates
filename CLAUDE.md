# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository nature

This **is** a git repository. Remote: `origin` -> `https://github.com/SRWS-PSG/protocol-templates.git`. The local clone's folder name (`protocol-srwspsg`, or similar) does not match the GitHub repo name (`protocol-templates`): that's expected, not a sign the wrong repo was checked out.

It is a documentation-and-tooling repository, not an application: the deliverables are Markdown SR protocol templates, but there **is** real build/automation tooling around them (Pandoc builds, a Google Docs comment-injection pipeline, structural parity checks, a training-lesson sync). See "Build tooling" below.

## What this project is about

The repository publishes a family of Markdown-based **systematic review (SR) protocol templates**, maintained by SRWS-PSG, designed to be version-controlled (every change tracked), citable (Zenodo DOI per GitHub release), and reusable (fill in placeholders, render via Pandoc).

[plan.md](plan.md) is the internal planning document behind the original protocols.io -> GitHub/Zenodo migration strategy:

- protocols.io = where the *pre-v3* template lived and was versioned; superseded by this repo from v3.0.0 onward (kept live as a frozen archive so old citations keep resolving).
- GitHub + Zenodo = the current source of truth. Zenodo mints a DOI automatically on every GitHub release (see [CITATION.cff](CITATION.cff) for the always-latest concept DOI).
- A companion paper on MetaArXiv (Scholar-indexed) gives the templates a citable, Google-Scholar-discoverable write-up independent of the templates themselves; see [CHANGELOG.md](CHANGELOG.md) and [paper/manuscript.md](paper/manuscript.md).
- The plan references protocols.io policy, Google Scholar inclusion guidelines, and Zenodo's Google Scholar FAQ as already-vetted external sources; prefer those over guessing when policy questions come up.

The plan is written in Japanese with English field labels in "record fields" code blocks; match that style when editing it.

## Templates

Four templates live under `templates/`, each independent (own master Markdown, own `references.bib`, own `comments.yaml`: do not consolidate across templates, a change to one must never silently affect another):

| Template | Directory | JA master? | Reporting guideline |
|---|---|---|---|
| Intervention review | `templates/intervention-review/` | yes | PRISMA 2020 / PRISMA-P |
| Scoping review | `templates/scoping-review/` | yes | PRISMA-ScR, JBI five-stage framework |
| DTA (diagnostic test accuracy) review | `templates/dta-review/` | yes | PRISMA-DTA, QUADAS-3 |
| NMA (network meta-analysis) review | `templates/NMA/` | **no (English only)** | PRISMA-NMA, CINeMA |

Each template directory has: the master Markdown file(s) (`protocol_template_for_*.md`, plus `.ja.md` where a JA master exists), `references.bib`, `vancouver.csl`, `comments.yaml`, `filters/` (Pandoc Lua filter + CSS + optional `reference.docx`), and `build.ps1`.

## Build tooling

### Per-template Pandoc build (`templates/*/build.ps1`)

```powershell
pwsh ./templates/intervention-review/build.ps1              # docx + html, both langs
pwsh ./templates/intervention-review/build.ps1 -Target docx # a specific target (docx|html|pdf)
pwsh ./templates/intervention-review/build.ps1 -Lang ja      # a specific language
```

Output goes to `templates/*/build/`, which is gitignored. `dta-review` has no own `reference.docx`; it (and `build_gdoc.py`) fall back to `templates/intervention-review/filters/reference.docx`, patched by `templates/intervention-review/filters/_patch_reference_docx.py` to define the custom `Placeholder`/`Note`/`NoteListParagraph` styles.

### `tools/build_gdoc.py`: render + upload to Google Drive/Docs with comments

Pipeline: master Markdown -> Pandoc docx (with `references.bib` + `vancouver.csl`) -> inject anchored Word comments from `comments.yaml` (via `tools/docx_comments.py`) -> upload to Drive as `mimeType=application/vnd.google-apps.document` so Google auto-converts the Word comments into anchored Doc comments.

```powershell
python tools/build_gdoc.py --template intervention-review --lang ja
python tools/build_gdoc.py --template scoping-review --lang en --dry-run   # build docx only, skip upload
```

`--template` chooses one of `intervention-review | scoping-review | dta-review | nma-review` (default `intervention-review`); `--lang` is required (`ja|en`, `NMA` only has `en`). Needs `pip install -r tools/requirements.txt`, an OAuth Desktop client at `tools/.gcp/credentials.json` (gitignored, not in this repo), and per-template Drive folder IDs in `tools/.env` (gitignored). See the script's module docstring for the full first-time setup and the delete-and-recreate-vs-`--in-place` upload semantics.

If `tools/.gcp/token.json` predates a `SCOPES` change (e.g. the `spreadsheets.readonly` scope added for the training-lesson sync below), `get_credentials()` detects the stale token, renames it to `token.json.stale-<timestamp>`, and re-runs the browser consent flow rather than crashing with a raw `RefreshError`.

### `comments.yaml`: mentor comments anchored into the rendered Doc

Schema is documented in each `comments.yaml`'s own header comment (read it there for the authoritative, up-to-date version); the short version:

- `anchor.ja` / `anchor.en`: verbatim text the comment attaches to in each master.
- `body:` hand-written Japanese comment text. Optional if `lessons:` is present.
- `lessons:` (optional) array of training-lesson references, resolved against `resources/training_lessons.json` at build time and rendered as a "related training" block (category + serial + title per lesson, Slack `/training` pointer, never `course_id`, never lesson body text). Each element is one of three forms: a **serial prefix** (segment-boundary match: prefix `P` matches serial `P` or anything starting with `P + "_"`, so `03_1` does not match `03_10`), `=<serial>` (exact serial equality, no prefix descent, for when a prefix would also pull in an unwanted sub-lesson), or `key:<lesson_key>` (exact `lesson_key` match). Resolution filters matches to `released == "yes"` first, since `serial` is not unique in the sheet (a lesson can be re-recorded under a new `lesson_key` while keeping its old serial); a ref that resolves to zero lessons, or whose matches are all unreleased, **fails the build** (`build_gdoc.py`) with a message naming the comment id and the offending ref.
- `legacy_urls:` (optional) original SRWS-PSG Facebook-group post URLs a comment's `lessons:` were migrated from. Provenance only; never rendered.

These `lessons:` refs are the modern equivalent of the old inline mentoring-session codes (`03_04`, `14`, ...) that the pre-v3 Doc anchored comments to directly: those codes now live on as `lessons:` prefixes matching the Slack training curriculum's `serial` column, instead of as anchor text.

### `resources/training_lessons.json`: synced training-curriculum snapshot

A snapshot of the SRWS-PSG Slack training curriculum Google Sheet (columns `lesson_key, category, serial, title, course_id, ..., released, ...`; only columns A:M are ever fetched, since column N, `body`, is Slack-workspace-only content and must never leave the sheet, enforced in `sync_training_lessons.py`'s `fetch_lessons` by failing loudly if the fetched header ever contains `body` or doesn't end in `exported_at`). `resources/` is gitignored wholesale *except* this one file (`resources/*` + `!resources/training_lessons.json` in `.gitignore`): it must be committed for `comments.yaml` `lessons:` references to be resolvable without live credentials.

`tools/sync_training_lessons.py`:

```powershell
python tools/sync_training_lessons.py                    # fetch A:M, write resources/training_lessons.json
python tools/sync_training_lessons.py --check             # offline: verify every comments.yaml `lessons:` ref resolves + is released. No network.
python tools/sync_training_lessons.py --check --remote    # also fetch the live sheet and report drift from the committed snapshot
```

Shares OAuth plumbing with `build_gdoc.py` (imports `get_credentials`/`load_env` from it rather than reimplementing). The shared resolver (snapshot loading, ref resolution, comment-body generation) lives in `tools/training_lessons.py` and is imported by both scripts: do not duplicate that logic.

Run `sync_training_lessons.py --check` (or the structure parity check, which also validates comment anchors) after editing any `comments.yaml`.

### `tools/check_structure_parity.py`: JA/EN structural parity

```powershell
python tools/check_structure_parity.py templates/intervention-review/protocol_template_for_intervention_review.md templates/intervention-review/protocol_template_for_intervention_review.ja.md
```

Takes the EN and JA master paths as positional args and fails (exit 1) if they've diverged on heading-level sequence, bilingual placeholder count, fenced-code-block count, citation key set, frontmatter keys, or comment-anchor resolution (via the sibling `comments.yaml`). Only applies to templates with a JA master (not `NMA`).

Known baseline failure, not to be "fixed" incidentally: `dta-review`'s check currently fails on citation key `salameh2020prismadtaee` (present in EN, not JA). Pre-existing; leave it unless specifically asked to fix it. `intervention-review` and `scoping-review` must stay green.

### Other `tools/` scripts

- `tools/docx_comments.py`: low-level docx comment injection (anchor matching + OOXML surgery), imported by `build_gdoc.py`.
- `tools/upload_paper.py`: uploads the companion paper (`paper/manuscript.md` etc.) similarly to Drive.
- `tools/citation-checker/`: git submodule (`https://github.com/SRWS-PSG/citation-checker.git`) used to verify bibliography DOIs.
- `tools/requirements.txt`: Python deps for all of the above (`google-api-python-client`, `google-auth*`, `pyyaml`).

## Working in this repo

- Each template stands alone: master Markdown + `references.bib` + `comments.yaml` are independent per template. Never let an edit to one silently change another.
- Prose in `comments.yaml` schema docs and in this file is a mix of English structure/English schema-doc prose (matching current practice) with Japanese comment *bodies* (the actual mentor-to-author text): match whichever convention the surrounding text already uses; do not convert one to the other.
- No em dashes in this repo's prose, Japanese or English (standing preference): use commas, colons, or parentheses instead.
- Do not add a "search period: inception to YYYY-MM-DD" placeholder to a protocol template: protocol registration precedes the search, so the end date isn't known yet.
- Do not add appendices mapping PRISMA/QUADAS/etc. checklist items to template sections: the template structure already enforces them.
- `resources/` holds historical/reference material (legacy docx sources, extracted legacy comments) and is gitignored except for `resources/training_lessons.json` (see above). Don't assume everything under `resources/` is tracked; check `.gitignore` before assuming a new file there will be committed.
- `tools/.gcp/` (OAuth credentials + cached token) and `tools/.env` / `.env` (Drive folder IDs) are gitignored and not present in a fresh checkout; scripts that need them fail with a clear message pointing at first-time setup rather than a raw stack trace.
