# Changelog

All notable changes to this protocol template are documented here.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) — for a documentation template that means: **major** = structural/citation-breaking changes; **minor** = new sections or guidance; **patch** = typo, citation, or formatting fixes.

## [Unreleased]

### Added

New `templates/NMA/` template (v1.0.0), **English only** (no JA master). Modernizes the legacy NMA protocol ([resources/legacy_protocol_template_for_NMA_review.docx](resources/legacy_protocol_template_for_NMA_review.docx), last updated 2022-02-27) into the v3 house style, derived from the intervention-review template and grafted with NMA-specific content.

- Reporting guideline: **PRISMA-NMA** ([Hutton et al. Ann Intern Med 2015;162(11):777-784](https://doi.org/10.7326/M14-2385)) added to Section 3.1 alongside PRISMA 2020 and PRISMA-P.
- New NMA sections: treatment network with decision/supplementary sets (3.2.3), network meta-analysis model and MetaInsight (3.11), transitivity assessment (3.12), inconsistency/coherence (3.13), and confidence rating via **CINeMA** with P-score/SUCRA ranking (Section 4).
- Bibliography: **independent** `templates/NMA/references.bib`; new NMA-only references `@hutton2015`, `@nikolakopoulou2020cinema`, `@owen2019metainsight`, `@rucker2015ranking`.
- Tooling: `tools/build_gdoc.py` now accepts `--template nma-review` (subdir `NMA`); rendered Google Docs upload to the NMA Drive folder via `DRIVE_FOLDER_ID_NMA_REVIEW`.

Training-lesson reference tooling, replacing the (private, stale) SRWS-PSG Facebook group as the destination for mentor "related training" links:

- `tools/training_lessons.py` (new): shared resolver, imported by both `build_gdoc.py` and the sync script below rather than duplicated. Loads `resources/training_lessons.json`, resolves a `comments.yaml` `lessons:` entry (a `serial` prefix, segment-boundary matched; `=<serial>` for an exact-serial match with no prefix descent; or `key:<lesson_key>` for an exact-key match) to lesson records, filters to `released == "yes"` (since `serial` is not unique in the sheet: a lesson can be re-recorded under a new `lesson_key` while keeping its old serial), and renders the Japanese "related training" comment-body block (category + serial + title per lesson, pointing to Slack `/training`; never `course_id`, never the lesson body text, which is Slack-workspace-only).
- `tools/sync_training_lessons.py` (new): fetches range `A:M` (never column N, `body`; the header is checked at fetch time and the fetch fails if `body` shows up in it or the last column isn't `exported_at`, so an upstream column deletion can't silently widen the fetch into lesson bodies) of the SRWS-PSG Slack training curriculum Google Sheet and writes `resources/training_lessons.json`. Reuses `build_gdoc.py`'s OAuth plumbing (`get_credentials`/`load_env`). `--check` offline-verifies every `comments.yaml` `lessons:` reference resolves to at least one released lesson (no network); `--check --remote` additionally fetches the live sheet and reports drift from the committed snapshot, including title changes (matched by `(serial, course_id)` since `lesson_key` embeds the title and so can't be diffed directly).
- `resources/training_lessons.json` (new, committed): the synced snapshot. `.gitignore`'s `resources/` rule narrowed to `resources/*` with `!resources/training_lessons.json`, since a wholesale directory ignore can't be selectively re-included.
- `tools/build_gdoc.py`'s `get_credentials()`: a `tools/.gcp/token.json` minted before `SCOPES` grew (see below) is now detected up front and treated as stale (renamed to `token.json.stale-<timestamp>`, then re-consented via the browser flow) instead of crashing with `RefreshError: Not all requested scopes were granted`.

### Changed

Companion paper (MetaArXiv preprint, DOI [10.31222/osf.io/wj52n](https://doi.org/10.31222/osf.io/wj52n)) revised to cover the NMA template:

- New **Section 7 "Network meta-analysis (NMA) review template"** added; subsequent sections renumbered (Usage 7→8, Versioning 8→9, Availability 9→10, Conclusion 10→11).
- Title, abstract, keywords, and Background/Development/Design sections updated from **three to four SR types** (the three migrated templates are still referred to as "three" where the migration history is described).
- Four NMA references added to the independent `paper/references.bib` (`@hutton2015`, `@nikolakopoulou2020cinema`, `@owen2019metainsight`, `@rucker2015ranking`); verified with citeguard (all `found`).
- Versioning policy (now Section 9) clarified: a preprint revision is triggered by a **major bump or the addition of a new template type**, not by routine minor/patch changes.
- Action required at release: deposit the revised PDF to MetaArXiv as a **new version under the same DOI** (`10.31222/osf.io/wj52n`); the DOI does not change across OSF preprint versions, so README/CITATION need no DOI edits.

All four `templates/*/comments.yaml` files: migrated every SRWS-PSG Facebook-group post reference (66 URLs total, across all four templates) to Slack training-lesson references, since the Facebook group is private and its posts are stale while training now lives on Slack (`/training`).

- New optional `lessons:` (array of training-lesson references: a `serial` prefix, `=<serial>` for an exact match, or `key:<lesson_key>`, e.g. `["03_07"]`) and `legacy_urls:` (the original Facebook URLs, kept for provenance, never rendered into the comment body) fields; full schema documented in each `comments.yaml`'s header comment block.
- `tools/build_gdoc.py`: `load_comments()` now resolves `lessons:` against `resources/training_lessons.json` and renders a "related training" block in place of the old Facebook links (generated first, then a blank line, then any hand-written `body:`, used by exactly one entry, dta-review's `c-inclusion-ref`). A ref that resolves to zero lessons, or whose matches are all unreleased, fails the build with an error naming the comment id and ref. New `--snapshot` flag to point at an alternate snapshot; `SCOPES` gained `https://www.googleapis.com/auth/spreadsheets.readonly`.
- The old inline mentoring-session codes (`03_04`, `14`, ...) that pre-v3 Docs anchored comments to directly are no longer anchors, but live on as `lessons:` refs matching the Slack training curriculum's `serial` column.
- dta-review's `c-rob-ref` remapped from the QUADAS-2 lessons (`10_02_02`/`10_02_03`, both unreleased in the live curriculum) to QUADAS-3/QUADAS-C (`10_02_08`/`10_02_07`), matching §3.6's QUADAS-3 methodology. `c-sof-ref` uses `=10_02_06` (exact-serial) rather than a `10_02_06` prefix, since the prefix would also pull in the sibling `10_02_06_02` guideline-authoring lesson, which doesn't belong on an SR protocol template.

Template version and date:

- The `version:` and `date:` keys are removed from the YAML frontmatter of all seven template masters. Builds derive them from `git describe --tags` and the HEAD commit date through the shared `tools/template_version.py` (used by every `templates/*/build.ps1` and by `tools/build_gdoc.py`). In source zips without git, `tools/VERSION` supplies them via `export-subst` (`.gitattributes`). `tools/check_no_hardcoded_version.py` fails if either key reappears.
- Per-template version numbers (scoping/DTA v2.0.0, NMA v1.0.0) are retired in favour of the single repository version, which matches the Zenodo version DOI.

## [3.2.0] – 2026-06-09

- Version DOI: `??????` _(minted automatically on Zenodo release; the always-latest concept DOI is recorded in [CITATION.cff](CITATION.cff))_

### Added

- Companion paper published on **MetaArXiv** (Scholar-indexed): Kataoka Y, So R, Banno M, Tsujimoto Y. *Increasing the transparency and reproducibility of systematic-review protocols: structure-enforced, version-controlled templates for intervention, scoping, and diagnostic test accuracy reviews.* MetaArXiv; 2026. DOI [10.31222/osf.io/wj52n](https://doi.org/10.31222/osf.io/wj52n).
- The companion paper DOI is now cited from the Section 3.1 self-reference of all three templates (EN + JA) as a managed citation (`@Kataoka2026-cj`, added to each template's independent `references.bib`), and recorded in [README.md](README.md) and [CITATION.cff](CITATION.cff) `identifiers`.

## [3.1.1] – 2026-06-08

### Changed

- Zenodo version DOIs minted at the v3.1.0 release filled in.

### Added

- OSF/MetaArXiv submission and manuscript files for the systematic review protocol templates.

## [3.1.0] – 2026-06-08

- Version DOI: `10.5281/zenodo.20586626` _(minted automatically on Zenodo release; the always-latest concept DOI is recorded in [CITATION.cff](CITATION.cff))_

### Added

New `templates/scoping-review/` template (v2.0.0). Mirrors the intervention-review build pipeline (Markdown + BibTeX + Pandoc + Google Docs upload with anchored comments) but is fully independent.

- Source: 2025-12-29 docx ([resources/2025-12-29スコーピングレビューのプロトコルテンプレ.docx](resources/2025-12-29スコーピングレビューのプロトコルテンプレ.docx)), restructured to match the intervention-review section ordering while preserving the JBI five-stage methodology.
- Reporting guideline: **PRISMA-ScR** [Tricco et al. Ann Intern Med 2018;169:467-473](https://doi.org/10.7326/M18-0850).
- Methodology: **JBI five-stage framework** ([Peters et al. JBI Evid Synth 2020;18(10):2119-2126](https://doi.org/10.11124/JBIES-20-00167); [JBI Manual Chapter 11](https://doi.org/10.46658/JBIMES-20-12); Arksey & O'Malley 2005; Levac et al. 2010).
- Protocol structure: **Peters et al. JBI Evid Synth 2022;20(4):953-968 Table 1** best-practice checklist ([DOI 10.11124/JBIES-21-00242](https://doi.org/10.11124/JBIES-21-00242)). Missing items (Registration, Author contributions, Amendments table, Funder role, Report characteristics, etc.) added to the source docx structure.
- Eligibility framework: **PCC** (Population / Concept / Context) instead of PICO; CONCEPT FOCUS illustration (terminology vs concept) retained from the source docx as a permanent template asset (`templates/scoping-review/media/scoping_concept_focus.png`).
- Bibliography: **independent** `templates/scoping-review/references.bib` (DOI-verified at write time). Does NOT share a bib with intervention-review; each template owns its citations to prevent silent cross-contamination.
- Tooling: `tools/build_gdoc.py` now takes `--template intervention-review|scoping-review`. Cached Doc IDs keyed as `<template>:<lang>` (legacy `ja`/`en` keys auto-migrated to `intervention-review:<lang>`).

New `templates/dta-review/` template (v2.0.0). Succeeds an unreleased SRWS-PSG DTA Google Docs template that referenced the Cochrane DTA Handbook v1.0 and QUADAS-2 only; rewritten in Markdown with an independent `references.bib`.

- Eligibility framework: **PIRT** (Participants / Index test / (Comparator) / Reference standard / Target condition) instead of PICO.
- Methodology: **Cochrane DTA Handbook v2.0 (July 2023)** ([10.1002/9781119756194](https://doi.org/10.1002/9781119756194)).
- Reporting guideline: **PRISMA-DTA** ([10.1001/jama.2017.19163](https://doi.org/10.1001/jama.2017.19163)) and its E&E document.
- Risk of bias: **QUADAS-3** (published Feb 2026), replacing QUADAS-2; `> Note:` blocks point comparative-accuracy reviews to QUADAS-C and AI index tests to QUADAS-AI.
- Synthesis: paired forest plots, SROC, bivariate and HSROC models via **MetaDTA** (browser-based; no R/Stata).

AI-use disclosure section ("Use of artificial intelligence in manuscript preparation") added to all three templates (EN + JA), with explicit guidance that AI must not be used to create or insert references.

## [3.0.0] – 2026-06-08

### Changed

Successor to protocols.io V.2 ([10.17504/protocols.io.81wgbpb41vpk/v2](https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2)). Maintenance has moved from protocols.io to GitHub + Zenodo. Major edits:

- Source format: docx → Markdown (Pandoc + BibTeX + Vancouver CSL).
- Author list aligned with [Kataoka et al. JMIR Med Educ 2025 (PMID:41263436)](https://pubmed.ncbi.nlm.nih.gov/41263436/): Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors.
- Abstract section replaced with the PRISMA 2020 abstract checklist (Item 2) as sub-section placeholders.
- Mentor side-notes (`[片岡4][片岡5][片岡6]` etc. that leaked into V.2 body text) converted to Pandoc footnotes.
- Inline footnote numbers (`[2]`, `[3]`) that had been mis-rendered as text are replaced by citeproc-managed numeric citations.
- Glaucoma + VEGF placeholder text in Introduction (left over from a demo SR) removed.
- Section 3.1 self-reference now points to the GitHub repository + Zenodo concept DOI, not a frozen protocols.io DOI.
- Cochrane Handbook reference updated from v6.0 (2019) to **v6.5 (Aug 2024)**.
- PRISMA 2020 statement ([Page MJ et al. BMJ 2021;372:n71](https://doi.org/10.1136/bmj.n71)) added to the bibliography; PRISMA-P 2015 retained for the protocol stage.
- Meta-analysis tooling changed from RevMan 5.4.2 to **PMA tools** (<https://yukifurukawa.jp/pmatools/>).
- Address/E-mail fields explicitly marked as "to be filled by the template user".
- Affiliations are no longer baked into the template metadata (they go stale).
- Keywords cleaned up (removed "procol template" typo from V.2).
- Abstract typo "This is a procol template." removed.

### Backward compatibility

- protocols.io V.2 ([DOI .../v2](https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2)) remains live as a frozen archive so that existing citations (notably [Okamura et al. 2026, Progress in Rehabilitation Medicine](https://doi.org/10.2490/prm.20260012)) stay resolvable. A one-line redirect note will be added to the V.2 description directing future users to this GitHub repository.

## [2.0.0] – 2022-08-26

Published on protocols.io: <https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw> (DOI [10.17504/protocols.io.81wgbpb41vpk/v2](https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2)). Initial widely-used version; cited by Okamura et al. 2026.

## [1.x] – earlier

Earlier protocols.io versions (DOI suffix `biqrkdv6` etc.). Pre-dates this changelog.
