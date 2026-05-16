# SRWS-PSG protocol templates

A collection of Markdown-based systematic review (SR) protocol templates, maintained by [SRWS-PSG](https://srws-psg.org/) (Scientific Research WorkS Peer Support Group).

Templates currently included:

- [`templates/intervention-review/`](templates/intervention-review/) — SR protocol for **intervention reviews** (the V.3 successor of the protocols.io V.2 template).

(More template types — scoping reviews, diagnostic test accuracy, etc. — will be added under `templates/` as separate sub-directories.)

The templates are designed to be:

- **Version-controlled** — every change is tracked, every release is permanent.
- **Citable** — each GitHub release gets a Zenodo DOI automatically.
- **Reusable** — fill in the `??????` placeholders with your own SR plan; render to docx / PDF / HTML via Pandoc.

## Citing this template

Use the DOI of the **release** you actually downloaded. The "concept DOI" below always resolves to the latest version.

- Concept DOI (always points to the latest release): `10.5281/zenodo.<TBD>` *(to be assigned at first Zenodo release)*
- Version DOIs are listed in [CHANGELOG.md](CHANGELOG.md) once minted.

For the rationale and design of each template, see the companion explanation article on Zenodo *(to be published as part of [Step 4 of the publication plan](plan.md))*.

> **Historical note (intervention-review template)**: Versions up to V.2 (2022-08-26) were published on protocols.io: <https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw> (DOI [10.17504/protocols.io.81wgbpb41vpk/v2](https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2)). From v3.0.0 onward this template is maintained here on GitHub.

## Quick start

```bash
git clone https://github.com/SRWS-PSG/protocol-templates
cd protocol-templates
pwsh ./templates/intervention-review/build.ps1 -Target docx     # or html, or pdf
```

Edit [templates/intervention-review/protocol_template_for_intervention_review.md](templates/intervention-review/protocol_template_for_intervention_review.md) and replace the `??????` placeholders with your own SR plan. Citations are managed in [templates/intervention-review/references.bib](templates/intervention-review/references.bib) (Vancouver style via Pandoc + citeproc).

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
    └── intervention-review/
        ├── protocol_template_for_intervention_review.md   # the template (source)
        ├── references.bib                                  # BibTeX for citations
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
