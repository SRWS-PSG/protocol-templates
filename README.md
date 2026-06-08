# SRWS-PSG protocol templates

A collection of Markdown-based systematic review (SR) protocol templates, maintained by [SRWS-PSG](https://srws-psg.org/) (Scientific Research WorkS Peer Support Group).

Templates currently included:

- [`templates/intervention-review/`](templates/intervention-review/) — SR protocol for **intervention reviews** (the V.3 successor of the protocols.io V.2 template).
- [`templates/scoping-review/`](templates/scoping-review/) — protocol for **scoping reviews**, structured per the JBI five-stage methodology and the [Peters et al. 2022 best-practice checklist](https://doi.org/10.11124/JBIES-21-00242). Reporting follows [PRISMA-ScR](https://doi.org/10.7326/M18-0850).

(More template types — diagnostic test accuracy, qualitative evidence synthesis, etc. — will be added under `templates/` as separate sub-directories.)

The templates are designed to be:

- **Version-controlled** — every change is tracked, every release is permanent.
- **Citable** — each GitHub release gets a Zenodo DOI automatically.
- **Reusable** — fill in the `??????` placeholders with your own SR plan; render to docx / PDF / HTML via Pandoc.

## Citing this template

Use the DOI of the **release** you actually downloaded. The "concept DOI" below always resolves to the latest version.

- Concept DOI (always points to the latest release): [`10.5281/zenodo.20586625`](https://doi.org/10.5281/zenodo.20586625)
- Version DOIs are listed in [CHANGELOG.md](CHANGELOG.md) once minted.

For the rationale and design of each template, see the companion paper (Scholar-indexed) on MetaArXiv: Kataoka Y, So R, Banno M, Tsujimoto Y. *Increasing the transparency and reproducibility of systematic-review protocols: structure-enforced, version-controlled templates for intervention, scoping, and diagnostic test accuracy reviews.* MetaArXiv; 2026. DOI [`10.31222/osf.io/wj52n`](https://doi.org/10.31222/osf.io/wj52n).

> **Historical note (intervention-review template)**: Versions up to V.2 (2022-08-26) were published on protocols.io: <https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw> (DOI [10.17504/protocols.io.81wgbpb41vpk/v2](https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2)). From v3.0.0 onward this template is maintained here on GitHub.

## Quick start

```bash
git clone https://github.com/SRWS-PSG/protocol-templates
cd protocol-templates
pwsh ./templates/intervention-review/build.ps1 -Target docx     # or html, or pdf
# Scoping review template:
pwsh ./templates/scoping-review/build.ps1     -Target docx
```

Edit [templates/intervention-review/protocol_template_for_intervention_review.md](templates/intervention-review/protocol_template_for_intervention_review.md) or [templates/scoping-review/protocol_template_for_scoping_review.md](templates/scoping-review/protocol_template_for_scoping_review.md) and replace the `[English label / 日本語ラベル: ...]` placeholders with your own SR plan. Each template owns its own `references.bib` (Vancouver style via Pandoc + citeproc) — do not consolidate across templates.

## Repository layout

```
.
├── README.md                       # this file
├── LICENSE                         # CC BY 4.0
├── CHANGELOG.md                    # version history (covers all templates)
├── CITATION.cff                    # GitHub "Cite this repository" metadata
├── .zenodo.json                    # Zenodo deposit metadata
├── plan.md                         # internal publication plan (working doc)
├── CLAUDE.md                       # Claude Code working notes
├── resources/                      # historical reference (protocols.io V.2 PDF, original docx)
└── templates/
    ├── intervention-review/
    │   ├── protocol_template_for_intervention_review.md   # the template (source, EN)
    │   ├── protocol_template_for_intervention_review.ja.md # JA master
    │   ├── references.bib                                  # BibTeX (intervention-only)
    │   ├── comments.yaml                                   # mentoring comments injected to Google Doc
    │   ├── build.ps1                                       # Pandoc build script
    │   └── build/                                          # generated artifacts (gitignored)
    └── scoping-review/
        ├── protocol_template_for_scoping_review.md        # the template (source, EN)
        ├── protocol_template_for_scoping_review.ja.md     # JA master
        ├── references.bib                                  # BibTeX (scoping-only, INDEPENDENT)
        ├── comments.yaml                                   # mentoring comments injected to Google Doc
        ├── media/scoping_concept_focus.png                 # JBI Terminology-vs-Concept figure
        ├── build.ps1                                       # Pandoc build script
        └── build/                                          # generated artifacts (gitignored)
```

## Authors

- Yuki Kataoka
- Ryuhei So
- Masahiro Banno
- Yasushi Tsujimoto
- SRWS-PSG Mentors

## License

Released under the [Creative Commons Attribution 4.0 International License](LICENSE).
