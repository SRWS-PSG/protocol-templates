---
title: "Protocol template for scoping review"
author:
  - SRWS-PSG Mentors
date: 2026-05-19
version: 1.0.0 (draft)
keywords:
  - scoping review protocol
  - PRISMA-ScR
  - JBI
  - PCC
license: CC BY 4.0
repository: https://github.com/SRWS-PSG/protocol-templates
template-path: templates/scoping-review
zenodo-concept-doi: 10.5281/zenodo.<TBD>
is-update: false
bibliography: references.bib
csl: vancouver.csl
link-citations: true
notes-after-punctuation: true
---

> このテンプレートの使い方
>
> この文書はスコーピングレビュー (scoping review) のプロトコルテンプレートです。`[English label / 日本語ラベル: 記入する内容]` で示した箇所を、自分たちのレビュー内容に置き換えてください。
>
> まず `2. Research question` で PCC (Population / Concept / Context) を決め、次に `3.3 Eligibility criteria` の各サブセクション、`Appendices` の検索式、`3.5 Charting the data` の抽出項目を埋めると進めやすいです。固定文は原則そのまま使えますが、レビュー内容に合わない場合はメンターに確認して修正してください。
>
> Note は作成中の補助説明です。提出版や登録版では、必要に応じて削除してください。
メンターの所属は `https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit?usp=sharing` を参照してください。


# Title

Title: [review title / レビュータイトル: 対象者 (Population)、コンセプト (Concept)、文脈 (Context) が分かる短い英語表現]: a scoping review protocol

> Note: If this protocol is an update of a previously published scoping review, append "(update)" to the title and set `is-update: true` in the YAML front-matter.

## Registration

Registration: [OSF registration / OSF 登録: e.g. osf.io/xxxxx]

> Note: Register the scoping review protocol on the Open Science Framework (OSF, [https://osf.io/](https://osf.io/)). PROSPERO does not accept scoping review protocols [@peters2022bestpractice].


## Authors:

> Do not forget to include mentor names.

Corresponding author: [corresponding author / 連絡著者（メンティー）: full name]

Address: [address / 連絡著者の所属先住所: department, institution, postal address]

E-mail: [e-mail / 連絡著者の連絡先メールアドレス]

Author contributions:

[guarantor initials / 連絡責任者のイニシャル] is the guarantor. [drafting author initials / 原稿ドラフト担当者のイニシャル] drafted the manuscript. All authors contributed to the development of the eligibility (PCC) criteria and the data-charting items. [search strategy author initials / 検索式担当者のイニシャル] developed the search strategy. [content expert initials / 臨床・方法論の専門家のイニシャル] provided expertise on [expertise area / 専門領域: target population, concept, methodology, etc.]. All authors read, provided feedback and approved the final manuscript.

\newpage

# 1. Introduction

> Note: Writing the background
>
> Add a reference to every statement. A three-paragraph structure is recommended.
>
> First paragraph — about the topic (Population), 4–5 sentences. Example:
>
> 1. Clinical and social importance of the topic
> 2. Size and impact of the target population
> 3. Standard approaches currently used
> 4. Existing gaps or limitations in current knowledge
>
> Second paragraph — about the Concept, 4–5 sentences. Example:
>
> 1. Description of the concept of interest (intervention, assessment, outcome, definition, etc.)
> 2. Current heterogeneity in how the concept is reported or defined in the literature
> 3. Aspects of the concept that this review aims to map
>
> Third paragraph — why a scoping review, 3–4 sentences. Example:
>
> 1. Results of a preliminary search for existing systematic reviews / scoping reviews on this topic (state "none found", or, if any exist, explain in one sentence how this review differs)
> 2. Why mapping the breadth (scope) of the available evidence is necessary
> 3. Therefore, we will conduct a scoping review on this topic
>
> GPTs that helps draft a background interactively: [https://chatgpt.com/g/g-YF7pcAKdG-background-editor](https://chatgpt.com/g/g-YF7pcAKdG-background-editor)

# 2. Research question

Using the PCC (Population, Concept, Context) framework, we state the questions this scoping review will address as follows.

- P (Population): [participants / 対象者: disease, condition, age range, care setting, etc.]
- C (Concept): [concept / コンセプト: the core concept the review will map — intervention, assessment, phenomenon, experience, etc. Specify whether the concept is defined by a fixed **terminology** or by a broader **concept**]
- C (Context): [context / 文脈: setting, region, time period, cultural background, etc. that bound the question]

Review questions:

1. [research question 1 / リサーチクエスチョン 1: a specific question phrased using PCC]
2. [research question 2 / リサーチクエスチョン 2: list more questions if needed]
3. [research question 3 / リサーチクエスチョン 3]

## Keywords

List up to 5 keywords, in alphabetical order, separated by semicolons and a space. Ideally these should differ from words appearing in the title or abstract.

[keywords / キーワード: e.g. concept; intervention; population; scoping review; setting]

# 3. Method

## 3.1 Protocol

This review follows the best-practice guidance for scoping review protocols by Peters et al. [@peters2022bestpractice] and the JBI methodological guidance for the conduct of scoping reviews [@peters2020jbi;@peters2020jbimanual]. Reporting of the eventual review will follow the PRISMA Extension for Scoping Reviews (PRISMA-ScR) [@tricco2018prismascr]. This protocol uses the scoping review protocol template maintained by SRWS-PSG (repository: [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates); Zenodo concept DOI: 10.5281/zenodo.&lt;TBD&gt;). The protocol will be made publicly available on OSF.io ([https://osf.io/](https://osf.io/)).

We adopt the JBI five-stage framework (Stage 1: identifying the research question / Stage 2: identifying relevant studies / Stage 3: study selection / Stage 4: charting the data / Stage 5: collating, summarizing, and reporting the results) [@peters2020jbi;@arksey2005scoping;@levac2010scoping].

## 3.2 Stage 1: Identifying the research question

Stage 1 corresponds to the PCC-based research questions stated in §2. See §2 for details.

## 3.3 Stage 2: Identifying relevant studies (eligibility criteria)

Using the PCC framework [@peters2020jbi], we define the inclusion criteria as follows.

### 3.3.1 Participants

[participants overview / 対象者の概要: describe the disease, condition, age range, and care setting in prose]

Inclusion criteria: [participant inclusion criteria / 対象者の組入基準: target condition, diagnostic criteria, age, sex, severity, setting]

Exclusion criteria: [participant exclusion criteria / 対象者の除外基準: comorbidities, prior treatments, specific subgroups to exclude]

### 3.3.2 Concept

[concept overview / コンセプトの概要: describe the core concept of the review in prose]

![Defining the concept in a scoping review: at Stage 2, decide explicitly whether the concept is defined by a narrow **terminology** (e.g. the word "tree / 木") or by a broader **concept** (e.g. forest, woodland, forestry).](media/scoping_concept_focus.png){#fig:concept-focus width=100%}

> Note: As shown above, state clearly whether you are defining the Concept by a narrow **terminology** or by a broader **concept** that includes related and derived terms. This decision drives the breadth of the search strategy and the inclusion judgement.

Inclusion criteria: [concept inclusion criteria / コンセプトの組入基準: the range of terms or related concepts that will be included]

Exclusion criteria: [concept exclusion criteria / コンセプトの除外基準: terms or related concepts that will be excluded]

### 3.3.3 Context

[context overview / 文脈の概要: setting, region, time period, cultural background, etc.]

Inclusion criteria: [context inclusion criteria / 文脈の組入基準: e.g. acute-care hospitals, home setting, high-income countries, specific health-care systems]

Exclusion criteria: [context exclusion criteria / 文脈の除外基準: e.g. animal experiments, exclusion of specific cultural settings]

### 3.3.4 Types of sources

[study designs / 組み入れる研究デザイン: e.g. quantitative studies (RCT, non-RCT, before-after, cohort, case-control, cross-sectional, case series, case reports), qualitative studies, systematic reviews, grey literature — list whichever fits the research question]

> Note: Conference abstracts are often excluded because they carry limited information. If you plan to include or exclude them, discuss the rationale with your mentor and state it explicitly.

### 3.3.5 Search method

> Note: When drafting the protocol for the first time, complete only the MEDLINE search strategy; defer CENTRAL, Embase, and the trial-registry searches until later (after mentor review of the form submission).

Search date range: [search date range / 検索対象期間: e.g. inception to YYYY-MM-DD]

#### 3.3.5.1 Electronic search

We will search the following databases.

1. MEDLINE (PubMed)
2. the Cochrane Central Register of Controlled Trials (Cochrane Library)
3. Embase (Dialog)

See Appendices 1, 2, and 3 for the search strategies.

#### 3.3.5.2 Other resources

We will search the following registries for ongoing or unpublished studies.

1. the World Health Organization International Clinical Trials Registry Platform (ICTRP)
2. ClinicalTrials.gov

See Appendices 4 and 5 for the search strategies.

We will also check the reference lists of included studies, as well as the reference lists of articles that cite the included studies. We will contact original authors to request any unpublished or additional data. If grey literature (government reports, theses, white papers from organizations, etc.) will be included, list the information sources here: [grey literature sources / 灰色文献の情報源: e.g. WHO database, OpenGrey, thesis databases].

### 3.3.6 Report characteristics

We will limit included documents by the following report characteristics.

- Language: [language / 言語: e.g. English and Japanese, or no language restriction]
- Years considered: [years considered / 検索対象年: e.g. 2000 onward, or no year restriction]
- Publication status: [publication status / 出版状態: state how peer-reviewed articles, preprints, and conference abstracts will be handled]

## 3.4 Stage 3: Study selection

Two independent reviewers ([screening reviewers / スクリーニング担当者のイニシャル: initials of two reviewers]) will screen titles and abstracts using the Tiab Review plugin [@Kataoka2026-tb], followed by full-text assessment for eligibility. We will contact original authors when key information needed for eligibility decisions is missing (e.g. only an abstract is available). Disagreements between the two reviewers will be resolved by discussion, with a third reviewer ([third reviewer / 第三レビュアーのイニシャル: initials]) acting as arbitrator if discussion does not resolve them. The search results and inclusion process will be reported in the final scoping review using a PRISMA-ScR flow diagram [@tricco2018prismascr].

> Note: If screening is done by more than two reviewers, write "two of three independent reviewers..." instead.

## 3.5 Stage 4: Charting the data

Two reviewers ([data extraction reviewers / データ抽出担当者のイニシャル: initials of two reviewers]) will independently extract data from the included studies using a standardized data-charting form (see Appendix 6). The draft form will be pilot-tested on 10 randomly selected studies, and revised as needed.

> Note: Scoping reviews do not typically extract individual study outcomes for quantitative synthesis [@peters2022bestpractice]. Instead, specify the **data items** required to answer the review questions in the Appendix 6 charting form, and prioritize them as required vs. optional items.

Disagreements will be resolved by discussion, with a third reviewer ([third reviewer / 第三レビュアーのイニシャル: initials]) acting as arbitrator if needed. We will contact original authors to request additional information when needed.

For efficiency, AI may be used to assist data extraction as appropriate [@Gartlehner2025-cm;@Kataoka2025-kq]. The actual use of AI will be reported in accordance with the Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru].

> Note (Risk of bias, optional): Scoping reviews do not typically include a critical appraisal (risk of bias) of individual studies [@peters2022bestpractice]. If you judge it necessary for your review question, describe the unit of assessment (study level / outcome level / both), the tool used, and how the appraisal results will be handled in the synthesis: [risk of bias plan / バイアスリスク評価計画: tool, level, treatment in synthesis].

## 3.6 Stage 5: Collating, summarizing, and reporting the results

We will synthesize the extracted data qualitatively, presenting results in a form that directly addresses the review questions. The presentation format (tables, figures, evidence and gap map, etc.) will be chosen to match the nature of the data [@south2023visualisation;@fredlund2024egm]. We plan to present the following.

1. A PRISMA-ScR flow diagram (inclusion process)
2. A characteristics table of included studies (columns for Author / Year / Country / Population / Concept / Context / Methodology / Key findings; see Appendix 6)
3. [planned visualisations / 提示予定の図表: e.g. evidence gap map, bubble plot, matrix map, timeline, narrative summary — choose the visualisation that fits the topic, using `cesm.12096` Table 3 [@fredlund2024egm] and the worked example in `s13643-023-02309-y` [@south2023visualisation] as references]

> Note (Meta-bias, optional): Scoping reviews do not typically assess meta-bias (e.g. publication bias) [@peters2022bestpractice]. If you will do so, describe the method here: [meta-bias plan / メタバイアス評価計画].

> Note (Confidence in cumulative evidence, optional): There is no established GRADE adaptation for scoping reviews [@peters2022bestpractice]. If you will assess the confidence in the cumulative evidence, describe the method and justification: [confidence assessment plan / 確実性評価計画].

# 4. Conflict of Interest

There is no conflict of interest in this project.

# 5. Funding

This work was self-funded.

> Note: In addition to monetary support (English-editing fees, database licences, analytic support), record any in-kind support (e.g. librarian help with search strategies, AI tools provided, institutional support). If there is a funder or sponsor, also record the funder name and whether and how the funder was involved in the study design, data collection, analysis, interpretation, or publication decision [@peters2022bestpractice]. If none, leave "This work was self-funded." as is.

# References

::: {#refs}
:::

&nbsp;

\newpage
# Appendices

## Appendix 1: MEDLINE (PubMed) search strategy

> For unresolved search strategy issues, fill in the form and share the URL with your mentor on Slack.

> Note: Steps for building a search strategy
>
> 1. Decide on the search blocks (e.g. population, concept, context, study design)
> 2. Decide on the controlled vocabulary (e.g. MeSH) for each block
> 3. Expand each block with free-text terms and controlled vocabulary
> 4. Combine blocks with AND
>
> A drafting tool (requires a free Google account): paste your eligibility criteria and it generates a draft search strategy. [https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&amp;usp=sharing](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

[MEDLINE search strategy / MEDLINE の検索式: terms for population, concept (and context), MeSH, and the combined query. Do not add an RCT filter for scoping reviews.]

## Appendix 2: CENTRAL (Cochrane Library) search strategy

[CENTRAL search strategy / CENTRAL の検索式: terms for population and concept, and the combined query]

## Appendix 3: Embase (Dialog) search strategy

> Note: When drafting the protocol for the first time, leave this Appendix empty. Build it after the MEDLINE strategy is finalised by substituting the corresponding Emtree and free-text terms.

[Embase search strategy / Embase の検索式: terms for population and concept, Emtree, and the combined query]

## Appendix 4: ICTRP search strategy

[ICTRP search strategy / ICTRP の検索式: terms for population and concept, synonyms, and search date]

## Appendix 5: ClinicalTrials.gov search strategy

- Condition or disease: [condition or disease / 対象集団・状態: terms and synonyms entered into ClinicalTrials.gov]
- Intervention / Other terms: [concept terms / コンセプト関連語: concept-related terms and synonyms entered into ClinicalTrials.gov]

## Appendix 6: Data charting form (basic draft extraction tool)

The table below is an example based on the basic draft extraction tool proposed by Peters et al. [@peters2022bestpractice]. Add or remove columns to suit your review question.

| Author (Year) | Country | Population | Concept | Context | Methodology / Study design | Key findings relevant to the review question |
|---|---|---|---|---|---|---|
| [author1 year / 例: Smith 2020] | [country / 国] | [population / 対象者の特徴] | [concept / 該当する用語・概念] | [context / セッティング・期間] | [methodology / デザイン] | [key findings / 主要な知見] |

Priority of data items: required = [required items / 必須項目: e.g. author, year, country, population, concept, context, study design]; optional = [optional items / 任意項目: e.g. sample size, funding source, language].

## Appendix 7: Scoping review protocol checklist (Peters 2022 Table 1)

Mapping of where this protocol addresses each item of the Peters et al. best-practice checklist [@peters2022bestpractice]. Use this as a self-check before submission.

| Item No | Section and topic | Where in this protocol |
|---|---|---|
| 1a | Title — Identification (states this is a scoping review protocol) | # Title |
| 1b | Title — Update (whether this is an update of a previous review) | # Title Note + YAML `is-update` |
| 2 | Title — Registration (registry and registration number) | ## Registration |
| 3a | Authors — Contact (name, affiliation, e-mail, address) | ## Authors (Corresponding author, Address, E-mail) |
| 3b | Authors — Contributions (includes guarantor) | ## Authors (Author contributions) |
| 4 | Amendments (amendment plan and history) | ## Amendments |
| 5a | Support — Sources of support | # 5. Funding |
| 5b | Support — Funder/Sponsor name | # 5. Funding (in Note) |
| 5c | Support — Role of funder/sponsor | # 5. Funding (in Note) |
| 6 | Rationale (review rationale, including rationale for choosing scoping) | # 1. Introduction |
| 7 | Objectives (review questions using PCC) | # 2. Research question |
| 8 | Eligibility criteria (PCC + study designs + report characteristics) | ## 3.3 Stage 2 (3.3.1–3.3.6) |
| 9 | Information sources (databases, registries, grey literature, search date range) | ## 3.3.5 Search method |
| 10 | Search strategy (draft for at least one database) | Appendices 1–5 |
| 11a | Study records — Data management | ## 3.4 Stage 3 (record management via Tiab Review plugin) |
| 11b | Study records — Selection process | ## 3.4 Stage 3 |
| 11c | Study records — Data collection process | ## 3.5 Stage 4 |
| 12 | Data items (charting items) | ## 3.5 Stage 4 + Appendix 6 |
| 13 | Outcomes and prioritization (described as prioritisation of data items for scoping) | ## 3.5 Stage 4 Note + Appendix 6 |
| 14 | Risk of bias in individual studies (optional) | ## 3.5 Stage 4 trailing Note |
| 15a–d | Data synthesis / presentation (tables, figures, evidence gap map, etc.) | ## 3.6 Stage 5 |
| 16 | Meta-bias(es) (optional) | ## 3.6 Stage 5 trailing Note |
| 17 | Confidence in cumulative evidence (optional) | ## 3.6 Stage 5 trailing Note |
