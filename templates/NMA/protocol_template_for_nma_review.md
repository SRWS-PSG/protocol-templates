---
title: "Protocol template for network meta-analysis review"
author:
  - SRWS-PSG Mentors
date: 2026-06-09
version: 1.0.0 (draft)
keywords:
  - systematic review protocol
  - network meta-analysis
  - intervention review
  - PRISMA 2020
  - PRISMA-NMA
  - CINeMA
  - Cochrane Handbook
license: CC BY 4.0
repository: https://github.com/SRWS-PSG/protocol-templates
template-path: templates/NMA
zenodo-concept-doi: 10.5281/zenodo.20586625
bibliography: references.bib
csl: vancouver.csl
link-citations: true
notes-after-punctuation: true
---
> このテンプレートの使い方
>
> この文書はネットワークメタアナリシス（NMA）の SR プロトコルテンプレートです。`[English label / 日本語ラベル: 記入する内容]` で示した箇所を、自分たちのレビュー内容に置き換えてください。
>
> まず `2. Research question` で PICO を決め、次に `3.2 Inclusion criteria`（特に `3.2.3 Types of interventions` のネットワーク）、`3.3 Type of outcomes`、`Appendices` の検索式、`3.11` 以降の NMA 解析計画を埋めると進めやすいです。固定文は原則そのまま使えますが、研究疑問や組み入れる研究デザインに合わない場合はメンターに確認して修正してください。
>
> Note は作成中の補助説明です。提出版や登録版では、必要に応じて削除してください。
> メンターの所属は `https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit?usp=sharing` を参照してください。
>
> ライセンス: 本テンプレートは [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) で公開されています。出典として Zenodo DOI を明記すれば、利用・改変・再配布が可能です。

\newpage

# Title

Title: [review title / レビュータイトル: 対象者、比較する複数の介入、主要アウトカムが分かる短い英語表現]: a systematic review and network meta-analysis protocol

> Note: 複数の介入を RCT のみで比較する NMA の場合は、タイトルに *efficacy* を使ってください（理由: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC351867/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC351867/)）。

## Authors:

> メンターの名前もお忘れなく

Corresponding author: [corresponding author / 連絡著者: full name]

Address: [address / 連絡著者の所属先住所: department, institution, postal address]

E-mail: [e-mail / 連絡著者の連絡先メールアドレス: 例, name@institution.ac.jp]

Author contributions:

[guarantor initials / 連絡責任者のイニシャル: 例, YK] is the guarantor. [drafting author initials / 原稿ドラフト担当者のイニシャル: 例, RS] drafted the manuscript. All authors contributed to the development of the selection criteria, the risk of bias assessment strategy and data extraction criteria. [search strategy author initials / 検索式担当者のイニシャル: 例, MB] developed the search strategy. [statistics author initials / 統計担当者のイニシャル: 例, YT] provided statistical expertise on network meta-analysis. [content expert initials / 臨床・方法論の専門家のイニシャル: 例, AB] provided expertise on [expertise area / 専門領域: 対象疾患、介入、方法論など]. All authors read, provided feedback and approved the final manuscript.

\newpage

> *Note*: プロトコルであるため、Abstract は必須ではありません。もし書きたい場合は、PRISMA 2020 の Abstract 項目（PRISMA 2020 abstract checklist）を参考に、必要に応じて以下の見出しを修正して使用してください。
>
> # Abstract
>
> - Background and Objectives
> - Methods
> - Eligibility criteria
> - Information sources
> - Risk of bias
> - Synthesis of results
> - Discussion
> - Other
> - Funding
> - Registration

\newpage

# 1. Introduction

> Note: 背景の書き方
>
> すべての記述にリファレンスを付けてください。3 パラグラフ構成を推奨します。NMA では「複数の治療選択肢が併存し、それらを直接比較した試験が乏しい」という点を背景で説明できると、ネットワークで比較する意義が伝わります。
>
> 第一パラグラフ: P（対象疾患）について 4–5 文。
> 例:
>
> 1. P の疾患は世界的な問題である
> 2. P の疾患の頻度・治療を要する患者数
> 3. P の疾患に対して複数の治療選択肢（介入）が存在することの説明
> 4. それらの治療法を直接比較したエビデンスが不足している点
>
> 第二パラグラフ: 比較する複数の介入について 4–5 文。
> 例:
>
> 1. 候補となる介入それぞれに有用性の報告がある
> 2. 臨床現場でこれらの介入が使い分けられている現状
>    3–4. 各介入の作用機序や位置づけ
> 3. 一方、各介入には害もある
>
> 第三パラグラフ: なぜ NMA を行うべきか 3–4 文。例:
>
> 1. 複数の介入を直接比較した試験は限られ、どの介入が相対的に優れるかは未確立である
> 2. 直接比較と間接比較を統合する NMA により、介入間の相対効果と順位づけを評価できる
> 3. そのため本研究ではこのトピックにおける SR&NMA を行う
>
> 背景を対話で指導してくれる GPTs: [https://chatgpt.com/g/g-YF7pcAKdG-background-editor](https://chatgpt.com/g/g-YF7pcAKdG-background-editor)
> すべての記述に必要に応じてリファレンスを付ける

# 2. Research question

- P: [participants / 対象者: 疾患、状態、年齢層、診断基準、重症度、診療場面など]
- I: [interventions / 介入: ネットワークで比較する複数の介入名、用量、頻度、期間、実施方法など]
- C: [comparator / 比較対照: ネットワーク内の共通比較対照、例, placebo、usual care、無治療]
- O: [outcomes / アウトカム: 主要アウトカムを中心に]

# 3. Method

## 3.1 Protocol

We used a systematic review protocol template maintained by SRWS-PSG [@Kataoka2026-cj]. We followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 (PRISMA 2020) statement [@page2021prisma], PRISMA-P 2015 [@shamseer2015], and the PRISMA extension for Network Meta-Analyses (PRISMA-NMA) [@hutton2015] for preparing this protocol. We will publish this protocol on OSF.io ([https://osf.io/](https://osf.io/)).

## 3.2 Inclusion criteria of the articles for the review

### 3.2.1 Type of studies

We will include randomized controlled trials that assess [interventions and target condition / 評価する介入と対象状態: 例, interventions for participants with condition]. We will not apply language or country restrictions. We will include all papers including published, unpublished articles, abstract of conference and letter. We will exclude [excluded study designs or records / 除外する研究デザイン・文献種別: 例, quasi-randomized trials, observational studies]. We will not exclude studies based on the observation period or publication year.

### 3.2.2 Study participants

[participants overview / 対象者の概要: 疾患・状態、年齢層、診断基準、重症度、診療場面などを文章で記入]

Inclusion criteria: [participant inclusion criteria / 対象者の組入基準: 対象疾患、診断基準、年齢、性別、重症度、セッティングなど]

Exclusion criteria: [participant exclusion criteria / 対象者の除外基準: 除外する併存疾患、既治療、特定集団など]

### 3.2.3 Types of interventions

Figure 1 shows the network of all possible pairwise comparisons between the eligible interventions.

> Note: ネットワーク図（Figure 1）には、ノード（各介入）とエッジ（直接比較が存在する介入の組）を示してください。どの介入を 1 つのノードにまとめるか（例, 用量や製剤の異なる同系統薬をまとめるか分けるか）は、レビューの臨床的な問いに合わせて事前に決め、その基準をここに明記してください。

#### 3.2.3.1 Decision set

[decision set / 意思決定セット: 臨床的な意思決定の対象として、相互に比較したい主要な介入（ノード）を列挙]

> Note: Decision set は、本レビューが相対効果を明らかにしたい中心的な介入群です。ネットワークの主要ノードに相当します。

#### 3.2.3.2 Supplementary set

[supplementary set / 補助セット: ネットワークを連結し間接比較を可能にするために含める追加の介入（例, placebo、usual care、共通比較対照）]

> Note: Supplementary set は、それ自体が主たる関心ではないものの、ネットワークを連結し直接・間接比較を成立させるために含めるノード（例, placebo や usual care）です。

### 3.2.4 Comparators

[comparator details / 比較対照の詳細: ネットワーク内の共通比較対照、placebo、usual care、無治療、併用療法の扱いなど]

## 3.3 Type of outcomes

### 3.3.1 Primary outcomes

1. [primary outcome name / 主要アウトカム名: 例, all-cause mortality]
   - Definition: [outcome definition / アウトカム定義: 測定指標、判定基準、スコアの向き、イベントの定義など]
   - Period: [time point / 評価時点: 例, closest to 12 weeks, during follow-up period]
2. [primary outcome name / 主要アウトカム名: 例, all-cause mortality]
   - Definition: [outcome definition / アウトカム定義: 測定指標、判定基準、スコアの向き、イベントの定義など]
   - Period: [time point / 評価時点: 例, closest to 12 weeks, during follow-up period]
3. [primary outcome name / 主要アウトカム名: 例, all-cause mortality]
   - Definition: [outcome definition / アウトカム定義: 測定指標、判定基準、スコアの向き、イベントの定義など]
   - Period: [time point / 評価時点: 例, closest to 12 weeks, during follow-up period]

### 3.3.2 Secondary outcomes

1. [secondary outcome name / 副次アウトカム名: 例, quality-of-life score]
   - Definition: [outcome definition / アウトカム定義: 測定指標、判定基準、スコアの向き、イベントの定義など]
   - Period: [time point / 評価時点: 例, closest to 12 weeks, during follow-up period]
2. [secondary outcome name / 副次アウトカム名: 例, quality-of-life score]
   - Definition: [outcome definition / アウトカム定義: 測定指標、判定基準、スコアの向き、イベントの定義など]
   - Period: [time point / 評価時点: 例, closest to 12 weeks, during follow-up period]
3. All adverse events
   - Definition: The definition of adverse events will be set by the original authors. Incidence proportion of all adverse events.
   - Period: during follow-up period

## 3.4 Search method

### 3.4.1 Electronic search

We will search the following databases:

1. MEDLINE (PubMed)
2. the Cochrane Central Register of Controlled Trials (Cochrane Library)
3. EMBASE (Dialog)

See Appendix 1, 2, and 3 for the search strategies.

### 3.4.2 Other resources

We will also search the following databases for ongoing or unpublished trials:

1. the World Health Organization International Clinical Trials Platform Search Portal (ICTRP)
2. ClinicalTrials.gov

See Appendix 4 and 5 for the search strategies.

We will check the reference lists of studies, including international guidelines [guideline names or organizations / 確認する診療ガイドライン名・作成組織: 例, WHO guidelines, 関連学会の診療ガイドライン], as well as the reference lists of eligible studies and articles citing eligible studies. We will ask the authors of original studies for unpublished or additional data.

## 3.5 Data collection and analysis

### 3.5.1 Selection of the studies

Two independent reviewers ([screening reviewers / スクリーニング担当者のイニシャル: initials of two reviewers]) will screen titles and abstracts using the Tiab Review plugin [@Kataoka2026-tb], followed by the assessment of eligibility based on the full texts. We will contact original authors if relevant data is missing. Disagreements between the two reviewers will be resolved by discussion, and if this fails, a third reviewer will act as an arbiter ([third reviewer / 第三レビュアーのイニシャル: initials]).

> note: 3 人以上で screening を行う場合は "two of three independent reviewers..." と記載してください。

### 3.5.2 Data extraction and management

Two reviewers ([data extraction reviewers / データ抽出担当者のイニシャル: initials of two reviewers]) will perform independent data extraction of the included studies using a standardized data collection form.
The form will include the information on study design, study population, interventions, and outcomes.

> Note: ここは表を作るつもりで、すべての変数名を書いてください。NMA では各研究の「どの介入アーム同士を比較しているか」を必ず記録し、ノードの割り当て（どの介入をどのノードに対応させるか）も記録してください。

Any disagreements will be resolved by discussion, and if this fails, a third reviewer will act as an arbiter ([third reviewer / 第三レビュアーのイニシャル: initials]).
To improve efficiency, we will use AI to assist with data extraction as needed [@Gartlehner2025-cm;@Kataoka2025-kq]. We will report how AI was actually used in accordance with the Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru].

## 3.6 Assessment of risk of bias in included studies

Two reviewers ([risk of bias reviewers / RoB 評価担当者: initials of two reviewers]) will evaluate the risk of bias independently using the Risk of Bias 2 tool [@sterne2019rob2]. Disagreements between the two reviewers will be discussed, and if this fails, a third reviewer ([third reviewer / 第三レビュアー: initials]) will be acting as an arbiter, if necessary.

## 3.7 Measures of treatment effects

We will pool the relative risk ratios and the 95% confidence intervals (CIs) for the following binary variables: [binary outcomes / 二値アウトカム: 例, mortality, response, adverse events].

We will pool the mean differences and the 95% CIs for the following continuous variables: [continuous outcomes / 連続アウトカム: 例, symptom score, quality-of-life score].

If several different scales have been used in the included studies, we will pool the effect estimates using standardized mean differences (SMDs).

We will summarize adverse events based on the definition by the original article, but we will not perform meta-analysis.

## 3.8 Unit of analysis issues

Clustering at the level of the enrolled units in cluster randomised studies. In dealing with cluster-RCTs, for dichotomous data, we will apply the design effect and calculate effective sample size and number of events using the intra-cluster correlation coefficient (ICC) among each unit and the average cluster size, as described in Chapter 16.3.5 of the Cochrane Handbook [@higgins2024cochrane]. If the ICC has not been reported, we will use the ICC of a similar study as a substitute. For continuous data, only the sample size will be reduced; means and standard deviation will remain unchanged [@higgins2024cochrane].

Randomized cross-over studies. For dichotomous outcomes, we will use the data from the first period of the cross-over trial. If it is not available, we will deal with the data from both periods as if the trial is a parallel trial.

For continuous outcomes we will use the data according to the following hierarchy:

1. First-period data
2. Mean difference between intervention and control periods, and its SD
3. If the SD above is not available, we will use 95% CI, t-statistic, or p-value for the t-test to calculate it
4. If none of the statistics above is available, we will perform approximate analyses to impute the SD of the mean difference between intervention and control periods according to the Cochrane Handbook Chapter 23.2.7

Multiple comparisons. All intervention groups that are relevant to this review will be included. For multi-arm studies, we will account for the correlation induced by including more than one pairwise comparison from the same study within the network meta-analysis model (see Section 3.11).

## 3.9 Handling of missing data

We will ask not-presented data to the original authors.

### 3.9.1 Missing outcomes

We will perform the intention-to-treat (ITT) analysis for all dichotomous data as much as possible. For continuous data, we will not impute missing data based on the recommendation by the Cochrane Handbook [@higgins2024cochrane]. We will perform meta-analysis with the available data in the original study.

### 3.9.2 Missing statistics

When original studies only report standard error or p-value, we will calculate the standard deviation based on the method by Altman [@altman1996skewness]. If we do not know these values when we contact the authors, the standard deviation will be calculated using confidence interval and t-value based on the method described in the Cochrane Handbook [@higgins2024cochrane], or by validated methods [@furukawa2006imputing]. The validity of these methods will be assessed by sensitivity analysis.

## 3.10 Assessment of heterogeneity

We will evaluate statistical heterogeneity by visual inspection of the forest plots for each pairwise comparison and by calculating the *I*² statistic (*I*² of 0–40%: might not be important; 30–60%: may represent moderate heterogeneity; 50–90%: may represent substantial heterogeneity; 75–100%: considerable heterogeneity). For the network meta-analysis, we will summarize the common heterogeneity variance (τ²) across the network and interpret its magnitude against empirical distributions of heterogeneity for the relevant outcome type.

## 3.11 Network meta-analysis

We will use group-level (aggregate) data. We will use the binomial likelihood for dichotomous outcomes and the normal likelihood for continuous outcomes. We will synthesize the study effect sizes using a random-effects network meta-analysis model that combines direct and indirect evidence. We will account for the correlations induced by multi-arm studies by using multivariate distributions. The variance of the random-effects distribution (heterogeneity variance, τ²) will be assumed to be common across comparisons and will be used to measure the extent of across-study, within-comparison variability in treatment effects. We will perform the network meta-analysis using MetaInsight [@owen2019metainsight].

> Note: 効果指標（OR/RR/MD/SMD）、固定効果か変量効果か、頻度論かベイズか、使用ソフト（MetaInsight 等）をここで確定させてください。MetaInsight: [https://crsu.shinyapps.io/MetaInsight/](https://crsu.shinyapps.io/MetaInsight/)。多腕試験の相関の扱いを明記してください。

## 3.12 Assessment of the transitivity assumption

The potential effect modifiers are [effect modifiers / 推移性に影響しうる効果修飾因子: 例, baseline severity, age, dose, follow-up length]. We will check whether these variables are similarly distributed across the studies grouped by comparison. If there are enough included trials, we will conduct meta-regression to assess their distribution. If a violation of the transitivity assumption is suspected, we will conduct pairwise meta-analysis only, and not network meta-analysis.

## 3.13 Assessment of inconsistency

Where the network contains closed loops, we will assess the agreement between direct and indirect evidence (coherence). We will evaluate local inconsistency using a node-splitting (separating indirect from direct evidence) approach, and global inconsistency using the design-by-treatment interaction model. A statistically significant inconsistency will prompt us to explore its sources (for example, effect modifiers across designs).

> Note: 不整合（incoherence）は CINeMA の incoherence ドメインにも反映されます（Section 4 参照）。閉ループが存在しない場合は、その旨を記載し、本セクションの評価は適用しないと明記してください。

## 3.14 Assessment of reporting bias

We will search the clinical trial registry system (ClinicalTrials.gov and ICTRP) and perform an extensive literature search for unpublished trials. To assess outcome reporting bias, we will compare the outcomes defined in the trial protocols with the outcomes reported in the publications. We will assess potential publication bias by visual inspection of the comparison-adjusted funnel plot. We will conduct the Egger test to assess publication bias. We will not conduct the test when we find fewer than 10 trials or trials of similar sample size.

## 3.15 Subgroup analysis

To elucidate the influence of effect modifiers on results, we will evaluate the subgroup analyses of the primary outcomes on the following factors when sufficient data are available.

1. (For participants) [participant subgroup factor / 対象者に関するサブグループ因子: 例, age group, disease severity]
2. (For intervention) [intervention subgroup factor / 介入に関するサブグループ因子: 例, dose, duration, delivery method]

## 3.16 Sensitivity analysis

We will undertake the following sensitivity analyses for the primary outcomes to assess whether the results of the review are robust to the decisions made during the review process.

1. Exclusion of studies using imputed statistics.
2. Missing participants: verify the robustness of the results by seeking informative missingness odds ratios [@furukawa2006imputing].
3. Only the participants who complete the study with complete data.

# 4. Confidence in the evidence

Two reviewers ([CINeMA reviewers / CINeMA 評価担当者のイニシャル、一人はメンター: initials of two reviewers, including one mentor if applicable]) will evaluate the confidence in the evidence for each primary outcome using the CINeMA (Confidence In Network Meta-Analysis) framework [@nikolakopoulou2020cinema]. The CINeMA framework includes the following six domains: within-study bias, across-studies bias, indirectness, imprecision, heterogeneity, and incoherence. For within-study bias and indirectness, CINeMA calculates the percentage contribution of each study to each network estimate and combines these contributions with the study-specific judgements to rate the relative effect for each comparison in the network. The domains of imprecision, heterogeneity, and incoherence use a pre-specified clinically important size of effect to define the margin of clinical equivalence between two interventions. Disagreements between the two reviewers will be discussed, and if this fails, a third reviewer ([third reviewer / 第三レビュアーのイニシャル: initials]) will act as an arbiter, if necessary.

We will rank the interventions for the following outcomes and present the ranking using P-scores (or the surface under the cumulative ranking curve, SUCRA): [outcomes for ranking / 順位づけを行うアウトカム: 主要アウトカムと重要な副次アウトカム] [@rucker2015ranking].

> Note: 順位指標（P-score / SUCRA）は「最も良い介入」を断定するものではなく、不確実性を伴う相対的な順位の要約です。効果量の大きさと確実性（CINeMA）とあわせて解釈し、順位だけで結論づけないでください。

# 5. Conflict of Interest

The authors declare no conflicts of interest.

# 6. Support

Self-funding.

> Note: 英文校正等に何らかの資金を使う場合はその旨を記載してください。資金を使わない場合は "Self-funding." のままでよいです。

# Use of artificial intelligence in manuscript preparation

We used [AI tool and version / 使用した生成 AI の名称とバージョン: e.g., Claude Code (Anthropic), v2.1.168, model Claude Opus 4.8] to proofread and copy-edit the text of this protocol. AI was not used to generate or select references, to produce or interpret data, or to make methodological decisions. The authors reviewed and verified all content and take full responsibility for the final manuscript.

> Note: 本プロトコルや本文の文章作成・校正に生成 AI を使った場合は、ツール名とバージョンを明記してください。使っていなければこのセクションは削除して構いません。References の作成・挿入に AI を使ってはいけません（# References の Note 参照）。

# References

> Note: References（引用文献リスト）は AI に作成・挿入させないでください。AI は実在しない文献・誤った著者名・巻号・DOI を生成することがあります。引用を入れ終えたら、提出前に必ず [https://citation-checker-three.vercel.app/](https://citation-checker-three.vercel.app/) ですべての citation をチェックしてください。誤った citation は投稿時に機械的にチェックされ、それが原因でリジェクトされた事例があります。

::: {#refs}
:::

\newpage

# Appendices

## Appendix 1: MEDLINE (PubMed) search strategy

> 03_06、03_07 の検索式の課題については、フォームに入力し、その旨を URL とともに Slack でメンターに伝えてください。

[MEDLINE search strategy / MEDLINE の検索式: participants と interventions の検索語、MeSH、RCT filter、組み合わせ式を記入]

## Appendix 2: CENTRAL (Cochrane Library) search strategy

> Note: CENTRAL では RCT フィルター不要です。

[CENTRAL search strategy / CENTRAL の検索式: participants と interventions の検索語、組み合わせ式を記入。RCT filter は不要]

## Appendix 3: EMBASE (Dialog) search strategy

[EMBASE search strategy / EMBASE の検索式: participants と interventions の検索語、Emtree、下記 RCT filter との組み合わせ式を記入]

> Note: Dialog の RCT filter です。Cochrane high sensitivity filter の転用です。以下は必要に応じて検索式に組み込んでください。

```text
S1 EMB.EXACT.EXPLODE("randomized controlled trial")
S2 EMB.EXACT.EXACT("controlled clinical trial")
S3 TI(random*) OR AB(random*)
S4 EMB.EXACT.EXACT("randomization")
S5 EMB.EXACT.EXACT("intermethod comparison")
S6 TI(placebo) OR AB(placebo)
S7 TI(compare) OR TI(compared) OR TI(comparison) OR AB(compare) OR AB(compared) OR AB(comparison)
S8 (AB(evaluated) OR AB(evaluate) OR AB(evaluating) OR AB(assessed) OR AB(assess)) AND (AB(compare) OR AB(compared) OR AB(comparing) OR AB(comparison))
S9 TI(open NEAR/1 label) OR AB(open NEAR/1 label)
S10 TI(double NEAR/1 blind) OR TI(single NEAR/1 blind) OR TI(doubly NEAR/1 blind) OR TI(singly NEAR/1 blind) OR AB(double NEAR/1 blind) OR AB(single NEAR/1 blind) OR AB(doubly NEAR/1 blind) OR AB(singly NEAR/1 blind)
S11 EMB.EXACT.EXACT("double blind procedure")
S12 TI(parallel NEAR/1 group*) OR AB(parallel NEAR/1 group*)
S13 TI(crossover) OR TI(cross over) OR AB(crossover) OR AB("cross over")
S14 (TI(assign* OR match OR matched OR allocation) NEAR/6 TI(alternate OR group OR groups OR intervention OR interventions OR patient OR patients OR subject OR subjects OR participant OR participants)) OR (AB(assign* OR match OR matched OR allocation) NEAR/6 AB(alternate OR group OR groups OR intervention OR interventions OR patient OR patients OR subject OR subjects OR participant OR participants))
S15 TI(assigned) OR TI(allocated) OR AB(assigned) OR AB(allocated)
S16 TI(controlled NEAR/8 (study OR design OR trial)) OR AB(controlled NEAR/8 (study OR design OR trial))
S17 TI(volunteer) OR TI(volunteers) OR AB(volunteer) OR AB(volunteers)
S18 EMB.EXACT.EXACT("human experiment")
S19 TI(trial)
S20 S1 OR S2 OR S3 OR S4 OR S5 OR S6 OR S7 OR S8 OR S9 OR S10 OR S11 OR S12 OR S13 OR S14 OR S15 OR S16 OR S17 OR S18 OR S19
S21 TI(random* NEAR/1 sampl* NEAR/8 ("cross section*" OR questionnaire* OR survey OR surveys OR database OR databases)) OR AB(random* NEAR/1 sampl* NEAR/8 ("cross section*" OR questionnaire* OR survey OR surveys OR database OR databases)) NOT (EMB.EXACT.EXACT("comparative study") OR EMB.EXACT.EXACT("controlled study") OR TI(randomised controlled) OR TI(randomized controlled) OR TI(randomly assigned))
S22 EMB.EXACT.EXACT("cross-sectional study") NOT (EMB.EXACT.EXPLODE("randomized controlled trial") OR EMB.EXACT.EXACT("controlled clinical study") OR EMB.EXACT.EXACT("controlled study") OR TI(randomised controlled) OR TI(randomized controlled) OR TI(control group) OR TI(control groups))
S23 TI(case control*) OR AB(case control*) AND TI(random*) OR AB(random*) NOT (TI(randomised controlled) OR TI(randomized controlled))
S24 TI(systematic review) NOT (TI(trial) OR TI(study))
S25 TI(nonrandom*) OR AB(nonrandom*) NOT TI(random*) OR AB(random*)
S26 TI(random field*) OR AB(random field*)
S27 TI('random cluster' NEAR/4 sampl*) OR AB('random cluster' NEAR/4 sampl*)
S28 AB(review) AND RTYPE(review) NOT TI(trial)
S29 AB('we searched') AND (TI(review) OR RTYPE(review))
S30 AB('update review')
S31 AB(databases NEAR/5 searched)
S32 (TI(rat) OR TI(rats) OR TI(mouse) OR TI(mice) OR TI(swine) OR TI(porcine) OR TI(murine) OR TI(sheep) OR TI(lambs) OR TI(pigs) OR TI(piglets) OR TI(rabbit) OR TI(rabbits) OR TI(cat) OR TI(cats) OR TI(dog) OR TI(dogs) OR TI(cattle) OR TI(bovine) OR TI(monkey) OR TI(monkeys) OR TI(trout) OR TI(marmoset*)) AND EMB.EXACT.EXACT('animal experiment')
S33 EMB.EXACT.EXACT('animal experiment') NOT (EMB.EXACT.EXACT('human experiment') OR EMB.EXACT.EXACT('human'))
S34 S21 OR S22 OR S23 OR S24 OR S25 OR S26 OR S27 OR S28 OR S29 OR S30 OR S31 OR S32 OR S33
S35 S20 NOT S34
```

## Appendix 4: ICTRP search strategy

[ICTRP search strategy / ICTRP の検索式: condition、interventions、類義語、検索日を記入]

## Appendix 5: ClinicalTrials.gov search strategy

- Condition or disease: [condition or disease / 対象疾患・状態: ClinicalTrials.gov に入力する疾患名や類義語]
- Intervention: [interventions / 介入: ClinicalTrials.gov に入力する介入名や類義語]
