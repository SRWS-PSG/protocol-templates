# Changelog

All notable changes to this protocol template are documented here.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) — for a documentation template that means: **major** = structural/citation-breaking changes; **minor** = new sections or guidance; **patch** = typo, citation, or formatting fixes.

## [Unreleased]

### Changed (planned for v3.0.0)

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
