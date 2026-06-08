# Changelog

All notable changes to this protocol template are documented here.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) — for a documentation template that means: **major** = structural/citation-breaking changes; **minor** = new sections or guidance; **patch** = typo, citation, or formatting fixes.

## [Unreleased]

_Nothing yet._

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
