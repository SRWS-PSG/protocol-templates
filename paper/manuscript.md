---
title: "Increasing the transparency and reproducibility of systematic-review protocols: structure-enforced, version-controlled templates for intervention, scoping, and diagnostic test accuracy reviews"
author:
  - "Yuki Kataoka^1,2,3,4,5,6^, MD, MPH, DrPH"
  - "Ryuhei So^1,7,8^, MD, MPH, DrPH"
  - "Masahiro Banno^1,9^, MD, PhD"
  - "Yasushi Tsujimoto^1,10,11^, MD, MPH, DrPH"
  - "SRWS-PSG Mentors^1^"
date: 2026-06-05
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
  - reproducibility
  - research transparency
abstract: |
  Blank-document templates and chapter-length methodology handbooks are a high
  barrier for systematic-review (SR) teams new to protocol writing. We describe
  the SRWS-PSG protocol templates, designed so that completing the section
  structure itself produces a protocol compliant with the relevant reporting
  guideline. The Markdown-based, version-controlled collection covers three SR
  types: intervention reviews, scoping reviews (structured around the JBI
  five-stage methodology and the Peters et al. 2022 best-practice checklist),
  and diagnostic test accuracy (DTA) reviews (aligned with the Cochrane DTA
  Handbook v2.0 and QUADAS-3). Each template is reproducible (pandoc + BibTeX),
  citable (released on GitHub with version DOIs minted via Zenodo), and reusable
  (CC BY 4.0). Templates are maintained at
  <https://github.com/SRWS-PSG/protocol-templates>. We report the design
  principles, the methodological choices made for each review type, and the
  process by which the templates were developed.
license: CC BY 4.0
repository: https://github.com/SRWS-PSG/protocol-templates
preprint-doi: 10.31222/osf.io/<TBD>
bibliography: references.bib
csl: vancouver.csl
link-citations: true
notes-after-punctuation: true
---
**Affiliations:**

1 Scientific Research WorkS Peer Support Group, Osaka, Japan\
2 Center for Postgraduate Clinical Training and Career Development, Nagoya University Hospital, Aichi, Japan\
3 Center for Medical Education, Graduate School of Medicine, Nagoya University, Aichi, Japan\
4 Department of Internal Medicine, Kyoto Min-iren Asukai Hospital, Kyoto, Japan\
5 Department of Healthcare Epidemiology, Kyoto University Graduate School of Medicine/School of Public Health, Kyoto, Japan\
6 Department of International and Community Oral Health, Tohoku University Graduate School of Dentistry, Miyagi, Japan\
7 Department of Psychiatry, Okayama Psychiatric Medical Center, Okayama, Japan\
8 CureApp, Inc., Tokyo, Japan\
9 Department of Psychiatry and Neurology, Seichiryo Hospital, Nagoya, Japan\
10 Oku Internal Medicine Clinic, Osaka, Japan\
11 Department of Health Promotion and Human Behavior, Kyoto University Graduate School of Medicine/School of Public Health, Kyoto, Japan

**Corresponding author:** Yuki Kataoka, Scientific Research WorkS Peer Support
Group, Osaka, Japan. Email: youkiti@gmail.com; ORCID: 0000-0001-7982-5213

The full membership of the SRWS-PSG Mentors group author is listed in Appendix S1.

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
WorkS Peer Support Group (SRWS-PSG) is a fully online, SR mentoring
community, operating since 2019 on a self-sustaining fee-funded model, that
supports health-care professionals through the full SR workflow from
protocol development to manuscript preparation [@kataoka2025jmir]. SRWS-PSG
had previously maintained three protocol templates—for intervention,
scoping, and DTA reviews [@kataoka2022protocolsio]. We migrated them to
GitHub to (i) update the content to current methodological standards (e.g.,
QUADAS-3 [@whiting2026quadas3] for DTA reviews); (ii) make the templates
citable through a stable reference; and (iii) enable granular, git-based
version control.

In this article we report the design principles, the methodological choices
made for each review type, and the process by which the templates were
developed, so that the approach can be evaluated, reused, and adapted by other
SR teams.

# 2. Development process

The three templates have distinct starting points. The intervention-review
template began from the SRWS-PSG protocols.io V.2 deposit
[@kataoka2022protocolsio]; the scoping- and DTA-review templates began from
unreleased SRWS-PSG Google Docs drafts used internally during mentoring. Across
all three, we collected informal usability feedback from trainees who had used
the predecessor templates during mentoring, and used it to decide which
sections needed clearer scaffolding.

Methodological updating proceeded by advancing each predecessor's
already-adopted references to their current versions, rather than re-selecting
frameworks from scratch: the Cochrane Handbook for intervention reviews from
v6.0 (2019) to v6.5 (2024) [@higgins2024cochrane], the Cochrane DTA Handbook
from v1.0 to v2.0 [@deeks2023dtahandbook], and the DTA risk-of-bias tool from
QUADAS-2 to QUADAS-3 [@whiting2026quadas3]. Reporting guidelines and tools that
postdated a predecessor were added where relevant.

Drafting followed the SRWS-PSG mentoring authorship convention: the first
author prepared each draft, which the remaining mentor authors reviewed and
revised. Systematic piloting of the templates with mentees, and incorporation
of that feedback, is planned for subsequent versions and will be reported when
those versions are released.

# 3. Design principles

The three templates share a common technical and editorial backbone.

**Source format.** Each template is authored in Markdown with a BibTeX
bibliography. Output to docx, HTML, and PDF is generated with pandoc using a
Vancouver-style CSL. This keeps the source diffable, the bibliography
reusable, and the output suitable for both team review (docx with comments)
and final submission (PDF).

**Independent bibliographies.** Each template owns its own `references.bib`.
This prevents silent cross-contamination — an update to a citation in one
template never changes citations in another.

**Placeholder convention.** Parameters that the SR team must fill in are
marked `[English label / 日本語ラベル: ...]`, signalling both the field and
its intent in both languages. Search-period placeholders such as "inception
to YYYY-MM-DD" are intentionally omitted, because protocol registration
precedes the search and the end date is not yet known.

**Reporting-guideline alignment.** Each template's section structure is
designed so that completing it naturally produces a protocol that satisfies
the relevant reporting guideline. A separate self-check appendix mapping
PRISMA / PRISMA-ScR / PRISMA-DTA items to template sections is not provided;
the section structure itself enforces compliance.

**AI-assisted screening, extraction, and disclosure.** All three templates
embed a common stance on artificial intelligence (AI). Title-and-abstract
screening is performed with the TiAb Review plugin, a no-code, serverless
browser extension that combines large-language-model batch screening with
machine-learning active learning [@Kataoka2026-tb]. AI may also be used to
assist data extraction, where it can match human-only accuracy while reducing
time on task [@Gartlehner2025-cm; @Kataoka2025-kq]. In every case, the actual
use of AI is reported in accordance with the joint position statement on AI use
in evidence synthesis across Cochrane, the Campbell Collaboration, JBI, and the
Collaboration for Environmental Evidence [@Flemyng2025-ru], so that the role of
AI in each review remains transparent and reproducible.

**Versioning and license.** The repository follows semantic versioning, with
each GitHub release deposited to Zenodo and assigned a version DOI. All
templates are released under CC BY 4.0.

# 4. Intervention review template

The intervention review template (V.3) succeeds the protocols.io V.2 deposit
[@kataoka2022protocolsio]; it has been restructured to Markdown and updated
to current intervention-review methodology.

The framework is PICO (Population / Intervention / Comparator / Outcomes)
[@shamseer2015]. The protocol-stage reporting guideline is PRISMA-P 2015
[@shamseer2015]; the completed review is reported against PRISMA 2020
[@page2021prisma]. The template provides optional Abstract guidance
structured to match the PRISMA 2020 abstract checklist (Item 2)
[@page2021prisma].

The methodological reference is the Cochrane Handbook for Systematic Reviews
of Interventions, version 6.5 (August 2024) [@higgins2024cochrane],
upgraded from the v6.0 (2019) reference in the V.2 template. Risk of bias
for randomized trials uses RoB 2 [@sterne2019rob2].

For pairwise meta-analysis, the template recommends PMA tools
[@furukawa_pmatools], a browser-based pairwise meta-analysis web
application that requires no R or Stata installation. This replaces the V.2
reference to RevMan 5.4.2 and is offered as a low-friction alternative for
SRWS-PSG trainees who do not have a statistical software workflow set up.

Author affiliations are not baked into the template metadata, because they
go stale. The template instructs the user to fill in their own. The default
author list reflects the SRWS-PSG mentoring authorship convention, in which
the project lead serves as the corresponding author and the assigned
mentors are co-authors.

# 5. Scoping review template

The scoping review template (v2.0) succeeds an unreleased SRWS-PSG Google
Docs scoping review template.

The eligibility framework is PCC (Population / Concept / Context)
[@peters2022bestpractice], not PICO. The reporting guideline is PRISMA-ScR
[@tricco2018prismascr]. The conduct methodology is the JBI five-stage
framework [@peters2020jbi; @peters2020jbimanual], building on the original
Arksey & O'Malley framework [@arksey2005scoping] and Levac et al.'s
methodological refinements [@levac2010scoping]. The protocol structure is
aligned with the Peters et al. 2022 best-practice 17-item checklist
[@peters2022bestpractice]; items that were missing from earlier SRWS-PSG
scoping drafts — registration, author contributions, funder role, report
characteristics — have been added.

Stage 5 of the JBI methodology is qualitative synthesis and visualization,
so risk-of-bias assessment, meta-bias, and GRADE rating are flagged as
optional. A `> Note:` block at the relevant section guides users on when to
include them. Registration is to the Open Science Framework (OSF), because
PROSPERO does not accept scoping reviews. A charting form example (Author /
Year / Country / Population / Concept / Context / Methodology / Key
findings), based on the basic draft extraction tool proposed by Peters et
al. [@peters2022bestpractice], is provided in Appendix 6.

# 6. Diagnostic test accuracy (DTA) review template

The DTA review template (v2.0) succeeds an unreleased SRWS-PSG DTA Google
Docs template that referenced the Cochrane DTA Handbook v1.0 and QUADAS-2
only; it has been rewritten in Markdown and updated to current DTA-review
methodology.

The eligibility framework is PIRT — Participants / Index test / (Comparator) /
Reference standard / Target condition [@deeks2023dtahandbook ch. 4] — not
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
[@reitsma2005bivariate] when threshold heterogeneity is small, and the
HSROC model [@rutter2001hsroc] when it is large. The recommended software is
MetaDTA [@patel2021metadta], a browser-based Shiny application from the
University
of Leicester CRSU that fits bivariate models and produces forest plots and
SROCs without requiring an R or Stata installation. The Cochrane DTA
Handbook v2 lists MetaDTA among its recommended tools
[@deeks2023dtahandbook].

A DTA search filter is not used because the Cochrane DTA
Handbook v2 considers existing filters insufficiently sensitive for DTA
reviews [@deeks2023dtahandbook]. Funnel-plot asymmetry tests are not used
to assess publication bias, again following the Cochrane DTA Handbook v2;
trial-registry searches and direct author contact for unpublished data take
their place.

# 7. Usage and citation

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
article (MetaArXiv preprint DOI `10.31222/osf.io/<TBD>`), which reports the
design principles, methodological choices, and development process of the
templates.

# 8. Versioning policy

The repository follows Semantic Versioning 2.0. For a template collection,
the version components are interpreted as follows. A **major** bump signals
a structural or citation-breaking change — for example, replacing a
reporting guideline with its successor, switching a methodological framework
(such as PICO to PIRT), or removing a section. A **minor** bump introduces a
new section, a new template (as in the addition of the scoping template), or
substantive new guidance. A **patch** bump covers typos, citation
corrections, and formatting adjustments. This preprint is updated only when
the template repository undergoes a major bump.

# 9. Availability and license

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
Writing – review & editing. All authors read and approved the final
manuscript. Individual members of the SRWS-PSG Mentors group author are listed
in Appendix S1.

# Conflicts of interest

The authors declare no conflicts of interest related to this work.

# Funding

This work received no external funding. SRWS-PSG operates as a peer-support
community for SR methodology mentoring.

# Use of artificial intelligence in manuscript preparation

The authors used Claude Code (Anthropic; v2.1.168, model Claude Opus 4.8) to
proofread both this manuscript and the protocol templates. All authors reviewed and
verified the content and take full responsibility for the final manuscript and
templates. 


# References

::: {#refs}
:::

# Appendix S1. SRWS-PSG Mentors: members and affiliations

The author "SRWS-PSG Mentors" is a group author. Its membership is maintained as
a single living roster at
<https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit>.
The four named lead authors (Y. Kataoka, R. So, M. Banno, Y. Tsujimoto) appear in
the title block and are omitted here. "SRWS-PSG" abbreviates Scientific Research
WorkS Peer Support Group, Osaka, Japan.

| Name | ORCID | Affiliation(s) |
|------|-------|----------------|
| Shunsuke Taito, PT, PhD | 0000-0003-1218-4225 | Division of Rehabilitation, Department of Clinical Practice and Support, Hiroshima University Hospital, Hiroshima, Japan; SRWS-PSG |
| Jun Watanabe, MD, PhD | 0000-0003-4477-4238 | Division of Gastroenterological, General and Transplant Surgery, Department of Surgery, Jichi Medical University, Tochigi, Japan; Center for Community Medicine, Jichi Medical University, Tochigi, Japan; Division of Gastroenterology, Department of Medicine, Farncombe Family Digestive Health Research Institute, McMaster University, Hamilton, Ontario, Canada; SRWS-PSG |
| Akihiro Shiroshita, MD, MPH | 0000-0003-0262-459X | Division of Epidemiology, Department of Medicine, Vanderbilt University School of Medicine, Nashville, TN, USA; SRWS-PSG |
| Keisuke Anan, MD | 0000-0002-2701-7334 | Division of Respiratory Medicine, Saiseikai Kumamoto Hospital, Kumamoto, Japan; SRWS-PSG |
| Ryo Momosaki, MD, MPH, PhD | 0000-0003-3274-3952 | Department of Rehabilitation Medicine, Mie University Graduate School of Medicine, Mie, Japan; SRWS-PSG |
| Yoshitaka Wada, MD, PhD | 0000-0003-2191-3629 | Department of Rehabilitation Medicine I, School of Medicine, Fujita Health University, Aichi, Japan; SRWS-PSG |
| Yusuke Tsutsumi, MD, MPH, DrPH | 0000-0002-9160-0241 | Department of Emergency Medicine, National Hospital Organization Mito Medical Center, Ibaraki, Japan; Department of Human Health Science, Kyoto University Graduate School of Medicine, Kyoto, Japan; Department of Emergency and Critical Care Medicine, University of Tsukuba Hospital, Tsukuba, Japan; Department of Epidemiology, Disease Control and Prevention, Hiroshima University Graduate School of Biomedical and Health Sciences, Hiroshima, Japan; SRWS-PSG |
| Norio Yamamoto, MD, PhD | 0000-0002-7902-9994 | Department of Orthopedic Surgery, Hashimoto Hospital, Kagawa, Japan; SRWS-PSG |
| Takafumi Kubota, MD | 0000-0003-3632-9679 | Department of Neurology, Tohoku University Graduate School of Medicine, Sendai, Miyagi, Japan; SRWS-PSG |
| Yukiko Okami, RD, PhD | | Department of Public Health, Shiga University of Medical Science, Otsu, Shiga, Japan; SRWS-PSG |
| Yuki Itagaki, MD | 0000-0003-2133-2787 | Emergency and Critical Care Center, Sapporo City General Hospital, Hokkaido, Japan; SRWS-PSG |
| Takeshi Yamashina, MD, PhD | 0000-0003-2845-7988 | Division of Gastroenterology and Hepatology, Kansai Medical University Medical Center, Osaka, Japan; SRWS-PSG |
| Kayoko Morio, PhD | 0000-0002-9371-535X | Department of Pharmacy, Kobe University Hospital, Kobe, Japan; SRWS-PSG |
| Takashi Ariie, PT, PhD | 0000-0003-1457-3427 | Department of Physical Therapy, School of Health Sciences at Fukuoka, International University of Health and Welfare, Fukuoka, Japan; SRWS-PSG |
| Kotomi Sakai, SLP, MPH, PhD | 0000-0002-8700-9029 | Department of Research, Heisei Medical & Welfare Group Research Institute, Tokyo, Japan; SRWS-PSG |
| Michihito Kyo, MD, PhD | 0000-0002-2559-6440 | Department of Radiation Disaster Medicine, Research Institute for Radiation Biology and Medicine, Hiroshima University, Hiroshima, Japan; Department of Emergency and Critical Care Medicine, Graduate School of Biomedical and Health Sciences, Hiroshima University, Hiroshima, Japan; SRWS-PSG |
| Hiromu Okano, MD | 0000-0002-2116-0455 | Department of Emergency and Critical Care Medicine, National Hospital Organization Yokohama Medical Center, Kanagawa, Japan; International University of Health and Welfare Graduate School of Public Health, Tokyo, Japan; SRWS-PSG |
| Naoto Kuroda, MD | | Department of Pediatrics, Wayne State University, Detroit, MI, USA; Department of Epileptology, Tohoku University Graduate School of Medicine, Sendai, Japan; SRWS-PSG |
| Natsumi Saka, MD, PhD | | Department of Orthopaedics, Teikyo University School of Medicine, Tokyo, Japan; Department of Health Research Methods, Evidence & Impact, McMaster University, Hamilton, Ontario, Canada; SRWS-PSG |
| Yasutaka Kuniyoshi, MD, PhD | 0000-0001-6012-0037 | Department of Social Services and Healthcare Management, International University of Health and Welfare, Otawara, Tochigi, Japan; SRWS-PSG |
| Koshiro Kanaoka, MD, PhD | 0000-0001-7900-7835 | Department of Medical and Health Information Management, National Cerebral and Cardiovascular Center, Suita, Osaka, Japan; Department of Cardiovascular Medicine, Nara Medical University, Kashihara, Nara, Japan; SRWS-PSG |
| Yuji Okazaki, MD | | Department of Emergency Medicine, Hiroshima City Hiroshima Citizens Hospital, Hiroshima, Japan; SRWS-PSG |
| Yoshinosuke Shimamura, MD, MPH | | Department of Nephrology, Teine Keijinkai Medical Center, Sapporo, Hokkaido, Japan; SRWS-PSG |
| Shodai Yoshihiro, MPharm | 0000-0003-2418-2323 | Department of Pharmaceutical Services, Hiroshima University Hospital, Hiroshima, Japan; SRWS-PSG |
| Kyosuke Kamijo, MD | 0000-0001-7375-7651 | Department of Obstetrics and Gynecology, Nagano Prefectural Shinshu Medical Center, Suzaka, Japan; SRWS-PSG |
| Tomohiko Kamo, PT, PhD | 0000-0003-0490-8393 | Department of Physical Therapy, Faculty of Rehabilitation, Gunma Paz University, Takasaki, Gunma, Japan; SRWS-PSG |
| Takanori Miura, MD | 0000-0002-1516-6105 | Department of Orthopaedic Surgery, Akita Rosai Hospital, Odate, Akita, Japan; SRWS-PSG |
| Hidehiro Someko, MD | 0000-0002-7195-2055 | Department of Internal Medicine, Nagoya Tokushukai General Hospital, Kasugai, Aichi, Japan; Department of Healthcare Epidemiology, Kyoto University Graduate School of Medicine / Public Health, Kyoto, Japan; SRWS-PSG |
| Eriya Imai, MD | 0000-0002-4511-4672 | Division of Anesthesia, Mitsui Memorial Hospital, Tokyo, Japan; International University of Health and Welfare Graduate School of Public Health, Tokyo, Japan; SRWS-PSG |
| Yuji Kamimura, MD, PhD | 0000-0002-0885-6343 | Department of Anesthesiology and Intensive Care Medicine, Nagoya City University Graduate School of Medical Sciences, Nagoya, Japan; SRWS-PSG |
| Yuki Nakashima, PT, PhD | 0000-0001-7838-9472 | Division of Rehabilitation, Department of Clinical Practice and Support, Hiroshima University Hospital, Hiroshima, Japan; SRWS-PSG |
| Masatsugu Okamura, PT, PhD | 0000-0001-9136-5037 | Berlin Institute of Health Center for Regenerative Therapies (BCRT), Charité – Universitätsmedizin Berlin, Berlin, Germany; Department of Rehabilitation Medicine, School of Medicine, Yokohama City University, Yokohama, Kanagawa, Japan; SRWS-PSG |
| Takashi Fujiwara, MD, PhD | 0000-0002-6790-8713 | Department of Otolaryngology, Kurashiki Central Hospital, Kurashiki, Okayama, Japan; SRWS-PSG |
| Tomoo Sato, MSN | 0000-0003-4036-4629 | Department of Nursing, Faculty of Nursing, Kindai University, Sakai, Osaka, Japan; SRWS-PSG |
| Yuki Yoshimatsu, MD, PhD | 0000-0003-0913-3507 | Elderly Care, Queen Elizabeth Hospital, Lewisham and Greenwich NHS Trust, London, United Kingdom; Centre for Exercise Activity and Rehabilitation, School of Human Sciences, University of Greenwich, London, United Kingdom; SRWS-PSG |
| Yusuke Saishoji, MD, MHA | 0000-0001-7163-8229 | Department of General Medicine, Hakujyuji Hospital, Fukuoka, Japan; SRWS-PSG |
| Takahiro Tsuge, PT, MPH | 0000-0003-0497-944X | Department of Rehabilitation, Kurashiki Medical Center, Kurashiki, Okayama, Japan; Department of Epidemiology, Graduate School of Medicine, Dentistry and Pharmaceutical Sciences, Okayama University, Okayama, Japan; SRWS-PSG |
| Kazumasa Kotake, BS | 0000-0001-9869-1177 | Department of Pharmacy, Zikei Hospital / Zikei Institute of Psychiatry, Okayama, Japan; SRWS-PSG |
| Yoshimitsu Wada, MD | 0000-0001-5986-8726 | Department of Obstetrics and Gynecology, Jichi Medical University, Tochigi, Japan |
| Shuri Nakao, PT | | Division of Rehabilitation Medicine, Shimane University Hospital, Izumo, Shimane, Japan; SRWS-PSG |
| Ryota Kimura, MD, PhD | 0000-0002-4855-3283 | Department of Orthopedic Surgery, Akita University Graduate School of Medicine, Akita, Japan; SRWS-PSG |
| Tetsuro Aita, MD, FACP | 0000-0002-1693-361X | Department of General Internal Medicine, Fukushima Medical University, Fukushima, Japan; Department of Clinical Epidemiology, Graduate School of Medicine, Fukushima Medical University, Fukushima, Japan; SRWS-PSG |
| Yukiyoshi Sumi, MD, PhD | 0000-0001-6775-0883 | Department of Psychiatry, Shiga University of Medical Science, Otsu, Shiga, Japan; SRWS-PSG |
| Yasuhiro Ogura, MD | 0000-0001-8310-2069 | Department of Radiation Oncology, Cancer Institute Hospital of the Japanese Foundation for Cancer Research, Tokyo, Japan; Division of Cellular Senescence, Cancer Institute, Japanese Foundation for Cancer Research, Tokyo, Japan; Department of JFCR Cancer Biology, Graduate School of Medical and Dental Sciences, Institute of Science Tokyo, Tokyo, Japan; SRWS-PSG |
| Takeshi Nakata, MD | | Department of Endocrinology, Metabolism, Rheumatology and Nephrology, Faculty of Medicine, Oita University, Yufu, Oita, Japan; SRWS-PSG |
| Shunsuke Yasuo, MD | 0000-0002-3030-123X | Department of Healthcare Economics and Quality Management, School of Public Health, Graduate School of Medicine, Kyoto University, Kyoto, Japan; SRWS-PSG |
| Itsuki Terao, MD, PhD | | Department of Psychiatry, Ikokoro Clinic Nihonbashi, Chuo-ku, Tokyo, Japan |
| Hirotaka Mori, MD, MPH | | Department of Biostatistics, Graduate School of Medicine, Hokkaido University, Sapporo, Hokkaido, Japan |
| Takehiro Ohyama, MD | 0000-0002-2223-0769 | Division of Renal Surgery and Transplantation, General and Transplant Surgery, Department of Urology, Jichi Medical University, Shimotsuke, Tochigi, Japan |
| Mari Yamamoto, MD | 0000-0003-3927-399X | Department of Rheumatology and Nephrology, Chubu Rosai Hospital, Nagoya, Aichi, Japan; SRWS-PSG |
| Yukie Nitta, DDS, PhD | 0000-0003-3177-0246 | Department of Dental Anesthesiology, Faculty of Dental Medicine and Graduate School of Dental Medicine, Hokkaido University, Sapporo, Japan; SRWS-PSG |
| Shunsuke Kondo, MD | 0009-0007-3372-010X | Department of Medicine, John A Burns School of Medicine, Honolulu, HI, USA; SRWS-PSG |
| Shota Hoshika, MD, PhD | 0000-0002-4192-5072 | Shoulder & Elbow Service, Funabashi Orthopaedic Sports Medicine & Joint Center, Funabashi, Chiba, Japan; SRWS-PSG |
| Satoru Kitamura, MD | 0009-0005-6585-1580 | Department of Internal Medicine, Takemasa-kai Central Hospital, Fukuyama, Hiroshima, Japan; SRWS-PSG |
| Teiko Kawahigashi, MD, PhD | 0000-0003-1120-1230 | Department of Molecular and Human Genetics, Baylor College of Medicine, Houston, TX, USA; SRWS-PSG |
| Akiko Eto-Kimura, MD, PhD | 0009-0004-1233-1496 | AMS Landmark Clinic, Yokohama, Japan; SRWS-PSG |
| Haruka Tsuda, MD, MPH, PhD | 0000-0001-9740-0366 | Yamaga Home Clinic, Ichikawa, Chiba, Japan; SRWS-PSG |
| Masaki Karasuyama, PT, PhD | 0000-0002-4964-9033 | Department of Rehabilitation, Minamikawa Orthopedic Hospital, Fukuoka, Japan; SRWS-PSG |
| Ryota Kobayashi, MD | 0009-0003-1726-6921 | Department of Pediatrics, The Jikei University School of Medicine, Tokyo, Japan; SRWS-PSG |
| Masaki Takigawa, PhD | 0000-0002-7265-8579 | Department of Clinical Pharmaceutics, Faculty of Pharmaceutical Sciences, Toho University, Funabashi, Chiba, Japan; SRWS-PSG |
