---
title: "SRWS-PSG protocol templates for systematic, scoping, and diagnostic test accuracy reviews"
author:
  - Yuki Kataoka
  - Ryuhei So
  - Masahiro Banno
  - Yasushi Tsujimoto
  - SRWS-PSG Mentors
author-note: |
  Author affiliations are maintained as a single living roster at
  <https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit?usp=sharing>.
date: 2026-05-20
keywords:
  - systematic review
  - protocol template
  - intervention review
  - scoping review
  - diagnostic test accuracy
  - PRISMA 2020
  - PRISMA-ScR
  - PRISMA-DTA
  - Cochrane Handbook
  - QUADAS-3
  - SRWS-PSG
abstract: |
  Systematic-review (SR) teams need protocol templates that combine current
  reporting guidelines with practical scaffolding for mentoring. We describe
  the SRWS-PSG protocol templates: a Markdown-based, version-controlled
  collection covering three SR types[: ]intervention reviews (V.3, successor
  to a protocols.io V.2 template), scoping reviews (v2.0, structured around
  the JBI five-stage methodology and the Peters et al. 2022 best-practice
  checklist), and diagnostic test accuracy (DTA) reviews (v2.0, aligned with
  the Cochrane DTA Handbook v2.0 and QUADAS-3). Each template is reproducible
  (pandoc + BibTeX), citable (released on GitHub with version DOIs minted via
  Zenodo), and reusable (CC BY 4.0). Templates are maintained at
  <https://github.com/SRWS-PSG/protocol-templates>. This article describes
  the design principles and key methodological choices of each template and
  is the recommended citation for the templates as a methodology resource.
license: CC BY 4.0
repository: https://github.com/SRWS-PSG/protocol-templates
preprint-doi: 10.31222/osf.io/<TBD>
bibliography: references.bib
csl: vancouver.csl
link-citations: true
notes-after-punctuation: true
---
# 1. Background

Systematic-review (SR) protocols document the planned methods of a review
before data collection and analysis. Prospective registration improves
transparency, reduces the risk of post-hoc methodological changes that
introduce bias, and aids replication [@page2021prisma; @shamseer2015]. The
PRISMA-P 2015 statement specifies 17 essential reporting items for SR
protocols [@shamseer2015], and the Cochrane Handbook
[@higgins2024cochrane] remains the canonical methodological reference for
intervention reviews. Parallel reporting and methodology guidance exists for
scoping reviews (PRISMA-ScR [@tricco2018prismascr] and the JBI methodology
[@peters2020jbi; @peters2020jbimanual]) and for diagnostic test accuracy (DTA)
reviews (PRISMA-DTA [@mcinnes2018prismadta; @salameh2020prismadtaee] and the
Cochrane DTA Handbook v2.0 [@deeks2023dtahandbook]).

For SR teams new to protocol writing, blank document templates and
chapter-length guidance documents are a high barrier. The Scientific Research
WorkS Peer Support Group (SRWS-PSG) is a fully online, SR
mentoring community, operating since 2019 on a self-sustaining fee-funded
model, that supports health-care professionals through the full SR workflow from protocol development to manuscript preparation. [@kataoka2025jmir]. SRWS-PSG had previously maintained three protocol templates—for
intervention, scoping, and DTA reviews
[@kataoka2022protocolsio]. We migrated them to GitHub to (i) update the content to current methodological standards (e.g., QUADAS-3 [@whiting2026quadas3] for DTA reviews); (ii) make the templates citable through a stable reference; and (iii) enable granular, git-based version control.

This article describes the resulting templates—for intervention,
scoping, and diagnostic test accuracy reviews—released as a single
Markdown-based, version-controlled, CC BY-licensed collection on
GitHub. The templates are aligned with current methodological
references: Cochrane Handbook v6.5 (August 2024)
[@higgins2024cochrane] for intervention reviews; the Peters et al.
2022 scoping review best-practice checklist [@peters2022bestpractice] and JBI
methodology [@peters2020jbi; @peters2020jbimanual] for scoping
reviews; and the Cochrane DTA Handbook v2.0 [@deeks2023dtahandbook]
together with QUADAS-3 [@whiting2026quadas3] for DTA reviews.

# 2. Design principles

The three templates share a common technical and editorial backbone.

**Source format.** Each template is authored in Markdown with a BibTeX
bibliography. Output to docx, HTML, and PDF is generated with pandoc using a
Vancouver-style CSL. This keeps the source diffable, the bibliography
reusable, and the output suitable for both team review (docx with comments)
and final submission (PDF).

**Independent bibliographies.** Each template owns its own `references.bib`.
This prevents silent cross-contamination. An update to a citation in one template never changes citations in another.

**Placeholder convention.** Parameters that the SR team must fill in are
marked `[English label / 日本語ラベル: ...]`, signalling both the field and
its intent in both languages.

**Reporting-guideline alignment.** Each template's section structure is
designed so that completing it naturally produces a protocol that satisfies
the relevant reporting guideline.

**Versioning and license.** The repository follows semantic versioning, with
each GitHub release deposited to Zenodo and assigned a version DOI. All
templates are released under CC BY 4.0.

# 3. Intervention review template

The intervention review template [(V.3) succeeds the protocols.io V.2 deposit
[@kataoka2022protocolsio]; it has been restructured to Markdown and updated
to current intervention-review methodology.]

The framework is PICO (Population / Intervention / Comparator / Outcomes)
[@shamseer2015]. The protocol-stage reporting guideline is PRISMA-P 2015
[@shamseer2015]; the completed review is reported against PRISMA 2020
[@page2021prisma]. The Abstract section of the template is structured to
match the PRISMA 2020 abstract checklist (Item 2) [@page2021prisma].

The methodological reference is the Cochrane Handbook for Systematic Reviews
of Interventions, version 6.5 (August 2024) [@higgins2024cochrane]. Risk of
bias for randomized trials uses RoB 2 [@sterne2019rob2]; non-randomized
studies use ROBINS-I or an equivalent tool.

For pairwise meta-analysis, the template recommends PMA tools
[@furukawa_pmatools], a browser-based pairwise meta-analysis web
application that requires no R or Stata installation.

# 4. Scoping review template

The scoping review template (v2.0) succeeds an unreleased SRWS-PSG Google
Docs scoping review template.

The eligibility framework is PCC (Population / Concept / Context)
[@peters2022bestpractice]. The reporting guideline is PRISMA-ScR
[@tricco2018prismascr]. The conduct methodology is the JBI five-stage
framework [@peters2020jbi; @peters2020jbimanual], building on the original
Arksey & O'Malley framework [@arksey2005scoping] and Levac et al.'s
methodological refinements [@levac2010scoping]. The protocol structure is
partially aligned with the Peters et al. 2022 best-practice 17-item checklist
[@peters2022bestpractice].

Stage 5 of the JBI methodology is qualitative synthesis and visualization,
so risk-of-bias assessment, meta-bias, and GRADE rating are flagged as
optional. A `> Note:` block at the relevant section guides users on when to
include them. Registration is to the Open Science Framework (OSF), because
PROSPERO does not accept scoping reviews. A charting form example (Author /
Year / Country / Population / Concept / Context / Methodology / Key
findings), based on Peters 2022 Table 2 [@peters2022bestpractice], is
provided in Appendix 6.

# 5. Diagnostic test accuracy (DTA) review template

The DTA review template (v2.0) succeeds an unreleased  SRWS-PSG DTA Google Docs template that referenced the Cochrane DTA Handbook v1.0 and QUADAS-2 only; it has been rewritten in Markdown and
updated to current DTA-review methodology.

The eligibility framework is PIRT [(Participants, Index test, [Comparator],
Reference standard, Target condition)] [@deeks2023dtahandbook ch. 4], not
PICO. The methodological reference is the Cochrane Handbook for
Systematic Reviews of Diagnostic Test Accuracy, version 2.0 (July 2023)
[@deeks2023dtahandbook]. Reporting is to PRISMA-DTA [@mcinnes2018prismadta]
and its Explanation & Elaboration document [@salameh2020prismadtaee].

Risk of bias is assessed with QUADAS-3 [@whiting2026quadas3], published in
February 2026 and replacing QUADAS-2 as the default tool. The template
includes a `> Note:` block at the relevant section directing users of
comparative-accuracy reviews to QUADAS-C [@yang2021quadasc] and users of
AI-centred index tests to QUADAS-AI (currently in development
[@guni2024quadasai]).

For synthesis, the template specifies forest plots of paired
sensitivity/specificity, summary ROC (SROC) curves, the bivariate model
[@reitsma2005bivariate] when threshold heterogeneity is small, the HSROC
model [@rutter2001hsroc] when it is large, and descriptive synthesis when
the number of studies is below four. The recommended software is MetaDTA
[@patel2021metadta], a browser-based Shiny application from the University
of Leicester CRSU that fits bivariate models and produces forest plots and
SROCs without requiring an R or Stata installation. The Cochrane DTA
Handbook v2 lists MetaDTA among its recommended tools
[@deeks2023dtahandbook].

# 6. Usage and citation

The templates live at [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates). To
use:

1. Clone the repository or download a release zip.
2. Choose the appropriate template subdirectory
   (`templates/intervention-review/`, `templates/scoping-review/`, or
   `templates/dta-review/`).
3. Edit `protocol_template_for_<type>.md` (English) or its `.ja.md`
   counterpart (Japanese) in any Markdown editor; replace each
   `[English label / 日本語ラベル: ...]` placeholder with your own SR plan.
4. Build the docx, HTML, or PDF output with
   `pwsh ./templates/<type>/build.ps1 -Target docx` (requires pandoc).

For citation, two DOIs apply. **To cite the template version you used**,
cite the Zenodo version DOI of the GitHub release you downloaded (listed in
`CHANGELOG.md` of the repository). The Zenodo concept DOI, which always
resolves to the latest release, is suitable for general references to "the
SRWS-PSG protocol templates" when no specific version is needed. **To cite
the design and methodological rationale of the templates**, cite this
article (MetaArXiv preprint DOI `10.31222/osf.io/<TBD>`); this preprint is
the recommended Google-Scholar-discoverable citation for the template family
as a methodology resource.

# 7. Versioning policy

The repository follows Semantic Versioning 2.0. This preprint is updated
only when the template repository undergoes a major bump.

# 8. Availability and license

- Source repository: [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates)
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Zenodo concept DOI (always latest release): `10.5281/zenodo.<TBD>`
- This article (MetaArXiv preprint): `10.31222/osf.io/<TBD>`
- Predecessor intervention-review template (protocols.io V.2, frozen):
  `10.17504/protocols.io.81wgbpb41vpk/v2` [@kataoka2022protocolsio]

# Author contributions

Contributions are described using the CRediT (Contributor Roles Taxonomy).
**Yuki Kataoka**: Conceptualization; Methodology; Writing – original draft;
Project administration. **Ryuhei So, Masahiro Banno, Yasushi Tsujimoto, and
SRWS-PSG Mentors**: Conceptualization (ideas and scope of each template);
Validation (trial use of the templates during SRWS-PSG mentoring sessions);
Writing – review & editing. All authors read and approved the final
manuscript.

# Conflicts of interest

The authors declare no conflicts of interest related to this work.

# Funding

This work received no external funding. SRWS-PSG operates as a peer-support
community for SR methodology mentoring.

# References
