---
title: "Protocol template for diagnostic test accuracy review"
author:
  - SRWS-PSG Mentors
date: 2026-05-20
version: 1.0.0 (draft)
keywords:
  - diagnostic test accuracy
  - systematic review protocol
  - PRISMA-DTA
  - QUADAS-3
  - MetaDTA
license: CC BY 4.0
repository: https://github.com/SRWS-PSG/protocol-templates
template-path: templates/dta-review
zenodo-concept-doi: 10.5281/zenodo.<TBD>
is-update: false
bibliography: references.bib
csl: vancouver.csl
link-citations: true
notes-after-punctuation: true
---

> このテンプレートの使い方
>
> この文書は診断精度 (diagnostic test accuracy; DTA) の系統的レビュー (SR) プロトコルテンプレートです。`[English label / 日本語ラベル: 記入する内容]` で示した箇所を、自分たちのレビュー内容に置き換えてください。
>
> まず `2. Research question` で Participants / Index test / Comparator (任意) / Reference standard / Target condition を決め、次に `3.2 Inclusion criteria` の各サブセクション、`Appendices` の検索式、`3.6 Synthesis` の解析方針を埋めると進めやすいです。固定文は原則そのまま使えますが、検査の種類（単一 vs 比較、人 vs AI など）に合わせて `> Note:` の分岐に従って調整してください。
>
> Note は作成中の補助説明です。提出版や登録版では、必要に応じて削除してください。
> メンターの所属は `https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit?usp=sharing` を参照してください。

\newpage

# Title

Title: [review title / レビュータイトル: Index test、Target condition、対象集団が分かる短い英語表現]: a systematic review and meta-analysis of diagnostic test accuracy protocol

> Note: If this protocol is an update of a previously published DTA review, append "(update)" to the title and set `is-update: true` in the YAML front-matter.

## Authors:

> Do not forget to include mentor names.

Corresponding author: [corresponding author / 連絡著者（メンティー）: full name]

Address: [address / 連絡著者の所属先住所: department, institution, postal address]

E-mail: [e-mail / 連絡著者の連絡先メールアドレス]

Author contributions:

[guarantor initials / 連絡責任者のイニシャル] is the guarantor. [drafting author initials / 原稿ドラフト担当者のイニシャル] drafted the manuscript. All authors contributed to developing the inclusion criteria, QUADAS-3 assessment strategy, and data extraction criteria. [search strategy author initials / 検索式担当者のイニシャル] developed the search strategy. [statistics author initials / 統計担当者のイニシャル] provided statistical advice on DTA meta-analysis (bivariate / HSROC models). [content expert initials / 臨床・方法論の専門家のイニシャル] provided expertise on [expertise area / 専門領域: target condition, index test, reference standard, methodology, etc.]. All authors read, provided feedback and approved the final manuscript.

> *Note*: Since this is a protocol, an abstract is not mandatory. If you wish to include one, follow the PRISMA-DTA [@mcinnes2018prismadta] abstract items and adjust the headings below as needed.
>
> # Abstract
>
> - Background — Objectives
> - Methods
> - Eligibility criteria (Participants / Index test / Reference standard / Target condition)
> - Information sources
> - Risk of bias (QUADAS-3)
> - Synthesis of results (bivariate / HSROC; MetaDTA)
> - Discussion
> - Funding
> - Registration

\newpage

# 1. Introduction

> Note: Writing the background
>
> Add a reference to every statement. A three-paragraph structure is recommended. Make the clinical pathway explicit.
>
> First paragraph — about the Target condition, 4–5 sentences. Example:
>
> 1. Clinical and social importance of the condition
> 2. Frequency of the condition and number of patients needing diagnosis
> 3. Description of the current standard diagnostic approach (including the reference standard)
> 4. Limitations of the standard approach (invasiveness, cost, availability, diagnostic delay, etc.)
>
> Second paragraph — about the role of the Index test, 4–5 sentences. Example:
>
> 1. The principle of the Index test and its clinical position (rule-in / rule-out, triage, replacement, or add-on)
> 2. Summary of diagnostic accuracy reported in prior studies and its variability
> 3. Expected changes to the clinical pathway if the Index test is adopted
> 4. Potential harms from false-positive / false-negative results
>
> Third paragraph — why a DTA SR is needed, 3–4 sentences. Example:
>
> 1. Existing DTA SRs on this topic are absent, outdated, or narrowly scoped
> 2. Pooled estimates of sensitivity / specificity and a certainty-of-evidence assessment are needed to inform clinical decision-making
> 3. Therefore, we will conduct a DTA SR and meta-analysis on this topic
>
> A GPTs that guides you through the background interactively: [https://chatgpt.com/g/g-YF7pcAKdG-background-editor](https://chatgpt.com/g/g-YF7pcAKdG-background-editor)
> Add references where needed for every statement.

# 2. Research question

DTA reviews do not use PICO; we follow the Cochrane DTA Handbook v2 framework [@deeks2023dtahandbook] and define Participants / Index test / (Comparator) / Reference standard / Target condition.

- P (Participants): [participants / 対象者: 疾患疑い・症状・スクリーニング集団など、Index test を適用する集団]
- I (Index test): [index test / Index test: 評価対象の検査名、機器・モデル名、判定者の資格、閾値の扱い]
- C (Comparator, optional): [comparator index test / 比較対象 Index test: 同一被験者に実施される代替検査を比較する場合のみ記入。比較しない場合は "Not applicable" と書く]
- R (Reference standard): [reference standard / 参照基準: 真の状態を定義する検査・診断基準、判定タイミング、判定者]
- T (Target condition): [target condition / 対象とする状態: 診断対象の疾患・状態、定義]

Review questions:

1. [research question 1 / リサーチクエッション 1: What is the diagnostic accuracy of the Index test for the Target condition in Participants?]
2. [research question 2 / リサーチクエッション 2: Optional comparator question, subgroup question, or threshold-dependence question]

## Keywords

> Note: List up to 5 keywords in alphabetical order, separated by "; ". Ideally use terms not appearing in the title or abstract.

[keywords / キーワード: 例) diagnostic accuracy; index test; reference standard; sensitivity and specificity; target condition]

# 3. Method

## 3.1 Protocol

This review uses the diagnostic test accuracy review protocol template maintained by SRWS-PSG (repository: [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates); Zenodo concept DOI: 10.5281/zenodo.&lt;TBD&gt;). The protocol and conduct of this review follow the Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy v2.0 [@deeks2023dtahandbook]. Reporting follows the PRISMA-DTA statement [@mcinnes2018prismadta] and its explanation and elaboration [@salameh2020prismadtaee]. This protocol will be registered with PROSPERO ([https://www.crd.york.ac.uk/prospero/](https://www.crd.york.ac.uk/prospero/)).

## 3.2 Inclusion criteria of the studies for the review

### 3.2.1 Type of studies

We will include studies that evaluated [participants and index/target / 対象者・Index test・Target condition: 例, the diagnostic accuracy of [index test] for [target condition] in [participants]] using the following designs:

- Cross-sectional cohort studies (prospective or retrospective) in which all participants are assessed by both the index test and the reference standard
- Secondary analyses of randomized controlled trials (RCTs) reporting diagnostic accuracy
- Case-control (two-gate / diagnostic case-control) studies

Only studies that report — or from which it is possible to reconstruct — the 2×2 counts (true positives [TP], false positives [FP], false negatives [FN], true negatives [TN]) of the Index test against the Reference standard will be included.

There will be no restriction on language or country of origin. Published, unpublished, conference abstracts, and letters will be eligible. Case series and case reports will be excluded. No restriction will be placed on observation period or year of publication.

> Note (for comparative accuracy reviews): If you include paired comparative accuracy studies (multiple index tests applied to the same participants) or randomized comparative accuracy studies (participants randomized to different index tests), assess risk of bias with QUADAS-C [@yang2021quadasc] in addition to QUADAS-3 in §3.5.

### 3.2.2 Participants

[participants overview / 対象者の概要: 疾患・状態の疑い、年齢層、診療場面、Index test を適用する臨床的タイミングなどを文章で記入]

Inclusion criteria: [participant inclusion criteria / 対象者の組入基準: suspected condition, age, sex, setting (primary/secondary/tertiary care, screening), symptoms]

Exclusion criteria: [participant exclusion criteria / 対象者の除外基準: comorbidities, prior treatments, specific populations to exclude]

### 3.2.3 Index test

[index test details / Index test の詳細: 検査名、機器・試薬・モデル (AI/ML の場合はバージョン)、実施手順、判定者の資格、判定の盲検化、使用する閾値 (cutoff)・閾値設定方針]

> Note: Whether you fix the threshold at a single value or allow multiple thresholds directly affects the synthesis plan (§3.6). State this clearly here. If you accept "the post-hoc optimal threshold of each study", an HSROC model is the default.
>
> Note (for AI/ML-based index tests): Specify model name, version, training dataset, input preprocessing, and degree of automation (fully automated / semi-automated / human-in-the-loop). For risk of bias, refer to QUADAS-AI (in development) [@guni2024quadasai;@sounderajah2021quadasaiposition] and report primary-study quality with STARD-AI [@sounderajah2025stardai]. If QUADAS-AI has not yet been finalized, add AI-specific signaling questions to each QUADAS-3 domain.

### 3.2.4 Comparator (optional)

[comparator details / 比較対象 Index test の詳細: 比較対象がある場合のみ。Index test と同一の被験者・同一の Reference standard で評価された別の検査名、閾値、実施者など。比較対象がなければ「Not applicable」と記入]

### 3.2.5 Reference standard

[reference standard / Reference standard: 真の Target condition の有無を判定する基準（clinical diagnosis、histology、long-term follow-up、composite reference standard など）、判定タイミング、判定者の盲検化]

> Note: If the interval between the Index test and the Reference standard is too long, disease progression bias can arise. State a clinically reasonable upper bound (e.g., same day, within 1 week, within 4 weeks).
>
> Note: If the Reference standard is imperfect (no gold standard), or different reference standards are used for different participants, this will be captured by the QUADAS-3 "Reference standard" and "Flow and timing" domains as partial verification / differential verification bias.

### 3.2.6 Target condition

[target condition / Target condition: 診断対象の疾患・状態の clinical definition、stage/severity range、excluded subtypes]

## 3.3 Outcomes

### 3.3.1 Primary outcomes

The primary outcomes are the **sensitivity and specificity** of the Index test against the Reference standard, with 95% confidence intervals (CI). For each study we will extract the 2×2 counts (TP / FP / FN / TN) of the Index test and compute sensitivity and specificity.

### 3.3.2 Secondary outcomes

1. [secondary diagnostic outcomes / 副次的な精度指標: 例, positive predictive value (PPV), negative predictive value (NPV), likelihood ratio, diagnostic odds ratio, area under the SROC curve]
   - Definition: [outcome definition / アウトカム定義: 2×2 表からの算出式または原著の報告値を採用するかを明示]
2. All adverse events
   - Definition: Adverse events follow each original study's definition. We will tabulate the proportion of participants experiencing adverse events directly caused by the Index test (e.g., contrast-medium allergy, biopsy complication) — distinct from downstream effects of false-positive / false-negative results.
   - Time point: during follow-up
3. [additional secondary outcomes / 追加の副次アウトカム: 例, the proportion of inconclusive / uninterpretable test results]

## 3.4 Search method

> Note: For the first version of the protocol, you may complete only MEDLINE and leave CENTRAL, EMBASE, and the registry searches for later (finish them after a mentor has reviewed the rest of the protocol).
>
> Note: For DTA reviews, the published diagnostic-study search filters for MEDLINE / EMBASE have inadequate sensitivity, and the Cochrane DTA Handbook v2 [@deeks2023dtahandbook] recommends against using them. We therefore use no diagnostic filter — searches combine the Participants (or Target condition) block and the Index test block with AND.

Search period: [search date range / 検索対象期間: 例) inception to YYYY-MM-DD]

### 3.4.1 Electronic search

We will search the following databases:

1. MEDLINE (PubMed)
2. the Cochrane Central Register of Controlled Trials (CENTRAL)
3. EMBASE (Dialog)

See Appendices 1, 2, and 3 for the search strategies.

### 3.4.2 Other resources

For ongoing or unpublished studies, we will also search:

1. the World Health Organization International Clinical Trials Registry Platform (ICTRP)
2. ClinicalTrials.gov

See Appendices 4 and 5 for the search strategies.

We will check the reference lists of included studies, international clinical guidelines ([guideline names or organizations / 確認する診療ガイドライン名・作成組織]), and the reference lists of papers citing included studies. We will contact original authors for unpublished data or additional data (in particular, missing 2×2 cell counts).

## 3.5 Risk of bias assessment

Two reviewers ([risk of bias reviewers / RoB 評価担当者: initials of two reviewers]) will independently assess risk of bias and applicability using QUADAS-3 [@whiting2026quadas3]. Disagreements will be resolved by discussion, and if needed a third reviewer ([third reviewer / 第三レビュアー: initials]) will arbitrate.

> Note: QUADAS-2 [@whiting2011quadas2] was superseded by QUADAS-3 [@whiting2026quadas3] in February 2026. DTA SRs initiated from 2026 onward should default to QUADAS-3. Reviews already using QUADAS-2 may continue with it but should state so explicitly here.
>
> Note (comparative accuracy review): If you include paired or randomized comparative accuracy designs, use QUADAS-C [@yang2021quadasc] alongside QUADAS-3 to assess pair-level comparative bias.
>
> Note (AI-based index test): If the Index test is an AI/ML model, refer to QUADAS-AI (in development; Sounderajah 2021 position [@sounderajah2021quadasaiposition], Guni 2024 protocol [@guni2024quadasai]) for risk-of-bias assessment, and check primary-study reporting against STARD-AI [@sounderajah2025stardai].

## 3.6 Synthesis of results

### 3.6.1 Data extraction

For studies meeting the inclusion criteria, two reviewers ([data extraction reviewers / データ抽出担当者: initials of two reviewers]) will independently extract participant demographics, sample size, Index test details, Reference standard details, threshold, 2×2 counts (TP / FP / FN / TN), and QUADAS-3 domain-level ratings. The data extraction form (see Appendix 6) will be pilot-tested using ten randomly selected studies before full extraction.

For studies that report multiple 2×2 tables across different thresholds, we will extract all of them.

Primary-study reporting will be checked against STARD 2015 [@bossuyt2015stard]; we will contact original authors when essential information is missing.

Disagreements will be resolved by discussion, and if needed a third reviewer ([third reviewer / 第三レビュアー: initials]) will arbitrate.

To improve efficiency, AI may be used to assist data extraction [@Gartlehner2025-cm;@Kataoka2025-kq]. The actual use of AI will be reported following the Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru].

### 3.6.2 Meta-analysis

Synthesis follows the recommendations of the Cochrane DTA Handbook v2 [@deeks2023dtahandbook].

For each study we will compute sensitivity and specificity with 95% CI from the 2×2 table and present them in a **paired forest plot** (sensitivity and specificity side by side). We will also plot study-level pairs on the **SROC plane** and describe their distribution.

The synthesis approach is selected as follows:

1. **≥ 4 included studies and a common threshold**: use a **bivariate model** [@reitsma2005bivariate] and present the summary point with 95% confidence and 95% prediction regions on the SROC plane.
2. **≥ 4 included studies with varying thresholds**: use the **HSROC model** [@rutter2001hsroc] and present the SROC curve.
3. **< 4 included studies**: do not perform statistical pooling; present study-level sensitivity and specificity descriptively in a table and a paired forest plot.

All analyses will be performed in **MetaDTA** [@patel2021metadta] ([https://crsu-metadta.le.ac.uk/MetaDTA/](https://crsu-metadta.le.ac.uk/MetaDTA/)), a free browser-based Shiny application maintained by the University of Leicester CRSU. MetaDTA fits the bivariate model and produces paired forest plots, SROC plots, and summary ROC graphs without requiring registration or local R/Stata installation.

> Note: MetaDTA primarily implements the bivariate model. For threshold-heterogeneous datasets where HSROC is required and MetaDTA's features are insufficient, consider using the R `mada` package (CRAN) or Stata `metandi` / `metadta`. If you do so, record the software name and version in §3.6.2.

Adverse events will be summarized narratively per study definition; we will not perform meta-analysis of adverse events.

## 3.7 Heterogeneity

Between-study variability in sensitivity and specificity will be assessed visually on the SROC plane and the paired forest plot, and by the width of the prediction region from the bivariate / HSROC model. The `I²` statistic and its cutoff values are not recommended for DTA meta-analysis [@deeks2023dtahandbook] and will not be used.

When substantial heterogeneity is observed, we will explore the following pre-specified subgroups or covariates via meta-regression:

1. [participant subgroup / 対象者サブグループ: 例, age group (children vs adults), prevalence, symptom status, setting (primary/secondary/tertiary care)]
2. [index test subgroup / Index test サブグループ: 例, device manufacturer, model version, reader expertise, threshold category]
3. [reference standard subgroup / Reference standard サブグループ: 例, single vs composite reference standard, follow-up duration]
4. [methodological subgroup / 方法論的サブグループ: 例, QUADAS-3 low-risk-only studies vs all studies, prospective vs retrospective]

## 3.8 Sensitivity analysis

For the primary outcome, we will assess the robustness of results to review-process decisions with the following sensitivity analyses:

1. Excluding studies rated High risk on one or more QUADAS-3 domains (especially [most influential domain / 最も結果に影響しそうな QUADAS-3 ドメイン番号: 例, Patient selection (D1)])
2. [other sensitivity analysis / その他の感度分析: 例, excluding conference-abstract-only studies, excluding studies with imputed cell counts, excluding the largest study]

## 3.9 Reporting bias

We will search trial registries (ClinicalTrials.gov and ICTRP) for completed but unpublished studies. Following the Cochrane DTA Handbook v2 [@deeks2023dtahandbook], we will not perform statistical tests for publication bias (such as funnel plots or Egger's test), because their validity in DTA meta-analysis is not established.

# 4. Summary of findings table

Two reviewers ([GRADE reviewers / GRADE 評価担当者のイニシャル、一人はメンター: initials of two reviewers, including one mentor if applicable]) will rate the certainty of evidence using GRADE for DTA [@schunemann2020grade21p1;@schunemann2020grade21p2]. Disagreements will be resolved by discussion, and if needed a third reviewer ([third reviewer / 第三レビュアーのイニシャル: initials]) will arbitrate.

The Summary of Findings table will be constructed following the Cochrane DTA Handbook v2 [@deeks2023dtahandbook] and GRADE 21 part 2 [@schunemann2020grade21p2], presenting the expected TP / FP / FN / TN per 1,000 participants at an assumed typical prevalence for the following outcomes: [outcomes for SoF table / SoF テーブルに含めるアウトカム: 例, sensitivity, specificity, TP/FP/FN/TN per 1,000 at assumed prevalence, estimated patient impact].

# 5. Conflict of Interest

The authors declare that they have no conflicts of interest.

# 6. Funding

Self-funded.

> Note: Mention monetary support (English-editing fees, database fees, analytic support) as well as in-kind support (e.g., librarian support for the search strategy, AI tool provision, institutional support). If a funder or sponsor exists, state whether they had any role in the design, data collection, analysis, interpretation, or publication decision. Otherwise, "Self-funded." is fine.

# References

::: {#refs}
:::

\newpage

# Appendices

## Appendix 1: MEDLINE (PubMed) search strategy

> 03_06、03_07 の検索式の課題については、フォームに入力し、その旨を URL とともに Slack でメンターに伝えてください。

> Note: Building the DTA search strategy
>
> 1. Decide the search blocks (typically: Participants or Target condition, and Index test)
> 2. Identify controlled vocabulary (MeSH etc.) for each block
> 3. Expand each block with free text + controlled vocabulary
> 4. Combine the blocks with AND
> 5. **Do not add a diagnostic-study filter** (sensitivity is insufficient; the Cochrane DTA Handbook v2 [@deeks2023dtahandbook] recommends against it)
>
> Drafting helper tool (requires a free Google account): [https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&amp;usp=sharing](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

[MEDLINE search strategy / MEDLINE の検索式: Participants (または Target condition) と Index test の検索語、MeSH、組み合わせ式を記入。診断研究フィルターは付けない]

## Appendix 2: CENTRAL (Cochrane Library) search strategy

[CENTRAL search strategy / CENTRAL の検索式: Participants (または Target condition) と Index test の検索語、組み合わせ式を記入]

## Appendix 3: EMBASE (Dialog) search strategy

> Note: You may leave this appendix blank when first drafting the protocol; fill it in after the MEDLINE strategy is finalized, translating MeSH to Emtree and free-text variants as needed. Do not add a diagnostic-study filter.

[EMBASE search strategy / EMBASE の検索式: Participants (または Target condition) と Index test の検索語、Emtree、組み合わせ式を記入]

## Appendix 4: ICTRP search strategy

[ICTRP search strategy / ICTRP の検索式: Target condition、Index test、類義語、検索日を記入]

## Appendix 5: ClinicalTrials.gov search strategy

- Condition or disease: [condition or disease / 対象状態: ClinicalTrials.gov に入力する Target condition 名や類義語]
- Intervention / Other terms: [index test terms / Index test 関連語: ClinicalTrials.gov に入力する Index test 名や類義語]

## Appendix 6: Data extraction form (2×2 table + study characteristics)

Below is a minimum data-extraction form. Add or remove columns according to the review question. For studies reporting multiple 2×2 tables at different thresholds, extract them on separate rows.

| Author (Year)                   | Country        | Setting / Design                                    | Population                  | Sample size | Index test (model/version, threshold) | Reference standard      | Target condition | TP  | FP  | FN  | TN  | Sensitivity (95% CI) | Specificity (95% CI) | QUADAS-3 ratings (D1/D2/D3/D4 RoB & Applicability) |
| ------------------------------- | -------------- | --------------------------------------------------- | --------------------------- | ----------- | ------------------------------------- | ----------------------- | ---------------- | --- | --- | --- | --- | -------------------- | -------------------- | -------------------------------------------------- |
| [author1 year / 例: Smith 2020] | [country / 国] | [setting/design / 例: tertiary, prospective cohort] | [population / 対象者の特徴] | [n]         | [index test / Index test、閾値]       | [reference / Reference] | [target / 状態]  | [n] | [n] | [n] | [n] | [sens (CI)]          | [spec (CI)]          | [ratings]                                          |

Item priorities: Required = author, year, country, design, population, sample size, index test, reference standard, target condition, TP/FP/FN/TN, threshold, QUADAS-3 ratings. Optional = [optional items / 任意項目: 例) funding source, conflict of interest, language, time interval between index test and reference standard].
