---
title: "Protocol template for diagnostic test accuracy review"
author:
  - SRWS-PSG Mentors
date: 2026-05-20
version: 2.0.0 (draft)
lang: en
keywords:
  - diagnostic test accuracy
  - systematic review protocol
  - PRISMA-DTA
  - QUADAS-3
  - MetaDTA
license: CC BY 4.0
repository: https://github.com/SRWS-PSG/protocol-templates
template-path: templates/dta-review
zenodo-concept-doi: 10.5281/zenodo.20586625
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
> まず `2. Research question` で Participants / Index test / Comparator (任意) / Reference standard / Target condition を決め、次に `3.2 Inclusion criteria` の各サブセクション、`Appendices` の検索式、`3.7 Synthesis` の解析方針を埋めると進めやすいです。固定文は原則そのまま使えますが、検査の種類（単一 vs 比較、人 vs AI など）に合わせて `> Note:` の分岐に従って調整してください。
>
> Note は作成中の補助説明です。提出版や登録版では、必要に応じて削除してください。
> メンターの所属は `https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit?usp=sharing` を参照してください。
>
> ライセンス: 本テンプレートは [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) で公開されています。出典として Zenodo DOI を明記すれば、利用・改変・再配布が可能です。

\newpage

# Title

Title: [review title / レビュータイトル: Index test、Target condition、対象集団が分かる短い英語表現]: a systematic review and meta-analysis of diagnostic test accuracy protocol

> Note: 過去版の更新としてプロトコルを公開する場合は、本タイトル末尾に "(update)" を付け、YAML front-matter の `is-update` を `true` に変更してください。

## Authors:

> メンターの名前もお忘れなく

Corresponding author: [corresponding author / 連絡著者（メンティー）: full name]

Address: [address / 連絡著者の所属先住所: department, institution, postal address]

E-mail: [e-mail / 連絡著者の連絡先メールアドレス]

Author contributions:

[guarantor initials / 連絡責任者のイニシャル] is the guarantor of this review. [drafting author initials / 原稿ドラフト担当者のイニシャル] drafted the manuscript. [search strategy author initials / 検索式担当者のイニシャル] developed the search strategy. [statistics author initials / 統計担当者のイニシャル] provided statistical advice on DTA meta-analysis (bivariate / HSROC models). [content expert initials / 臨床・方法論の専門家のイニシャル] provided expertise on [expertise area / 専門領域: target condition, index test, reference standard, methodology, etc.]. All authors read, provided feedback and approved the final manuscript.


\newpage


> *Note*: プロトコルであるため、Abstract は必須ではありません。もし書きたい場合は、PRISMA-DTA [@mcinnes2018prismadta] の Abstract 項目 を参考に、必要に応じて以下の見出しを修正して使用してください。
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

> Note: 背景の書き方
>
> すべての記述にリファレンスを付けてください。3 パラグラフ構成を推奨します。Clinical pathway を明確にしてください。
>
> Introduction で必ず明示すべき要素 
>
> - Target condition being diagnosed / 対象とする状態
> - Index test(s) / 評価対象の検査
> - Clinical pathway / 臨床診療パス
>     - Prior test(s) / Index test より前に行われる検査
>     - Role of index test(s) / Index test の位置付け (triage / replacement / add-on, rule-in / rule-out)
>     - Alternative test(s) / 代替となりうる検査
> - Rationale / 本 DTA SR を行う根拠
>
> 第一パラグラフ — 対象疾患 (Target condition) について 4–5 文。例:
>
> 1. 疾患の臨床的・社会的重要性
> 2. 疾患の頻度・診断を要する患者数
> 3. 現在の標準的な診断アプローチ (Reference standard を含む) の説明
> 4. 標準的な診断アプローチの限界（侵襲性、コスト、入手性、診断遅延など）
>
> 第二パラグラフ — Index test の役割について 4–5 文。例:
>
> 1. Index test の原理と臨床での位置付け (rule-in / rule-out、triage、replacement、add-on のいずれか)
> 2. 既存の研究で報告されている診断精度の概要とそのばらつき
> 3. Index test を導入することで期待される clinical pathway の変化
> 4. 一方で、Index test の偽陽性・偽陰性によって生じうる害
>
> 第三パラグラフ — なぜ DTA SR を行うべきか 3–4 文。例:
>
> 1. このトピックに関する既存の DTA SR が無い、または古い・対象が限定的である
> 2. 臨床現場での意思決定のため、感度・特異度の統合推定とエビデンスの確実性評価が必要である
> 3. そのため本研究ではこのトピックにおける DTA SR & meta-analysis を行う
>
> 背景を対話で指導してくれる GPTs: [https://chatgpt.com/g/g-YF7pcAKdG-background-editor](https://chatgpt.com/g/g-YF7pcAKdG-background-editor)
>
> すべての記述に必要に応じてリファレンスを付ける

# 2. Research question

> Note: DTA レビューでは PICO ではなく、Cochrane DTA Handbook v2 [@deeks2023dtahandbook] の枠組みに従って Participants / Index test / (Comparator) / Reference standard / Target condition を定義する。

- P (Participants): [participants / 対象者: 疾患疑い・症状・スクリーニング集団など、Index test を適用する集団]
- I (Index test): [index test / Index test: 評価対象の検査名、機器・モデル名、判定者の資格、閾値の扱い]
- C (Comparator, optional): [comparator index test / 比較対象 Index test: 同一被験者に実施される代替検査を比較する場合のみ記入。比較しない場合は "Not applicable" と書く]
- R (Reference standard): [reference standard / 参照基準: 真の状態を定義する検査・診断基準、判定タイミング、判定者]
- T (Target condition): [target condition / 対象とする状態: 診断対象の疾患・状態、定義]

Review questions:

1. [research question 1 / リサーチクエッション 1: What is the diagnostic accuracy of the Index test for the Target condition in Participants?]
2. [research question 2 / リサーチクエッション 2: Optional comparator question, subgroup question, or threshold-dependence question]

## Keywords

> Note: アルファベット順に 5 つまで、セミコロンとスペースで区切って記載する（タイトルやアブストラクトに現れる語と異なることが理想的）。

[keywords / キーワード: 例) diagnostic accuracy; index test; reference standard; sensitivity and specificity; target condition]

# 3. Method

## 3.1 Protocol

This review uses the diagnostic test accuracy review protocol template maintained by SRWS-PSG (repository: [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates); Zenodo concept DOI: 10.5281/zenodo.20586625; the design rationale for these templates is described in the companion paper [@Kataoka2026-cj]). In preparing this protocol we referred to the Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy v2.0 [@deeks2023dtahandbook], the PRISMA-DTA statement [@mcinnes2018prismadta], and its Explanation and Elaboration document [@salameh2020prismadtaee]. This protocol will be registered on OSF ([https://osf.io/](https://osf.io/)).

## 3.2 Inclusion criteria of the studies for the review

### 3.2.1 Type of studies

We will include all cohort studies, secondary analyses of RCTs, and case-control studies that evaluated the diagnostic accuracy of the Index test for the Target condition.

There will be no restriction on publication status (published, unpublished, conference abstracts, and letters are all eligible).

There will be no restriction on language or country in which the study was conducted.

Case series and case reports will be excluded.

Studies will be included if they present data from which the true positive, false positive, true negative, and false negative counts of the Index test against the Reference standard can be derived.

No restriction will be placed on the observation period.

> Note (比較精度レビューの場合): 同一被験者に複数の Index test を適用した paired comparative accuracy study、または対象者を Index test 群にランダム化した randomized comparative accuracy study を組み入れる場合は、§3.6 のバイアスリスク評価で QUADAS-C [@yang2021quadasc] を併用してください。

### 3.2.2 Participants

[participants overview / 対象者の概要: 疾患・状態の疑い、年齢層、診療場面、Index test を適用する臨床的タイミングなどを文章で記入]

- Inclusion criteria (all must be met): [participant inclusion criteria / 対象者の組入基準: suspected condition, age, sex, setting (primary/secondary/tertiary care, screening), symptoms]
- Exclusion criteria (any of which apply): [participant exclusion criteria / 対象者の除外基準: comorbidities, prior treatments, specific populations to exclude]

As required by QUADAS-3 phase 2 (ideal test accuracy trial / D1 signaling questions), the "ideal" participant profile for this review is prespecified here. These statements anchor the operationalization of the D1 signaling questions in §3.6.

- Intended-use population: [intended-use population / 想定使用集団: e.g., adults presenting to primary care with [symptom]. Specify the age, sex, symptom status, and comorbidity range of the population to which the index test would actually be applied in practice]
- Role of the index test within the clinical pathway: [role of index test / Index test の役割: one of triage / replacement / add-on / parallel testing. State the assumed prior tests (e.g., history and physical only; or after a separate test)]

### 3.2.3 Index test

[index test details / Index test の詳細: 検査名、機器・試薬・モデル (AI/ML の場合はバージョン)、sample type (specimen, imaging target, etc.)、実施手順]

Operators and readers: [operator and reader / 判定者・実施者: training and qualifications required to conduct and interpret the test (e.g., board-certified radiologist, laboratory technician, clinician, standalone AI model). Specify the level of expertise consistent with the intended-use population in §3.2.2]

As required by QUADAS-3 phase 2 (ideal test accuracy trial / D2 signaling questions 2.1–2.4), the "ideal" conditions for conducting and interpreting the index test in this review are prespecified here.

- Recommended instructions / standardized protocol: [recommended instructions / 推奨手順: manufacturer instructions, guideline-recommended SOP, etc. State concretely what counts as "appropriate conduct" and what kind of deviation will lead to signaling question 2.1 being judged "N"]
- **Clinical information that would be available in routine practice** when interpreting the index test: [available clinical information / 通常臨床で利用できる情報: e.g., participant age, sex, presenting symptoms, vital signs, prior test results that would already be on hand at the moment the index test is interpreted. This anchors signaling question 2.3 ("interpreted with the same information as would be available when the test is used in practice")]
- Information that must **not** be available at the time of index test interpretation: [prohibited information / 利用不可情報: reference standard results, the final target-condition diagnosis, results of tests that lie downstream of the index test in the clinical pathway. Anchors signaling question 2.2]
- Prespecified threshold: [prespecified threshold / 事前指定された閾値: e.g., the manufacturer-recommended cutoff X, or guideline-recommended cutoff Y. Studies that use a data-driven, post-hoc-selected threshold will be judged "N" on signaling question 2.4]

> Note: 閾値 (cutoff) を1つに固定するか、複数の閾値を許容するかは、解析方針（§3.7）と密接に関わるため、ここで明示してください。閾値を「研究ごとに事後選択された最適閾値」とする場合、HSROC モデルでの解析が前提となります。
>
> Note: 「通常の臨床で利用できる情報」を Index test 判定時に故意に隠した (blind した) 研究は、現実の運用と乖離するため signaling question 2.3 で "N" となり得ます。逆に、Index test 判定時に Reference standard 結果まで開示している研究は signaling question 2.2 で "N" となります。両者を取り違えないよう、ここで「利用できる情報」と「利用してはならない情報」を別行に分けて明記してください。

### 3.2.4 Comparator (optional)

[comparator details / 比較対象 Index test の詳細: 比較対象がある場合のみ。Index test と同一の被験者・同一の Reference standard で評価された別の検査名、閾値、実施者など。比較対象がなければ「Not applicable」と記入]

### 3.2.5 Reference standard

As required by QUADAS-3 phase 2 (ideal test accuracy trial / D3 signaling questions 3.1–3.8), the "ideal" conditions for the reference standard in this review are prespecified here.

- Hierarchy of acceptable reference standards: [reference standard hierarchy / Reference standard の階層: 1) most preferred (e.g., histology); 2) second-best (e.g., imaging plus ≥6-month clinical follow-up); 3) lowest acceptable (e.g., discharge clinical diagnosis). State the cutoff below which a study will not be included]
- Single reference standard applied to all participants: [single reference standard policy / 単一 reference standard 方針: state whether the same reference standard must be applied to all participants, or whether different reference standards (e.g., histology for index-test positives, follow-up for negatives) are acceptable. Anchors signaling question 3.3]
- Reference standard threshold: [reference threshold / Reference standard 閾値: e.g., histology Marsh score ≥ 3a, culture CFU/mL cutoff, specific imaging criteria. Data-driven post-hoc thresholds will be judged "N" on signaling question 3.7]
- Independence of reference standard and index test: [independence from index test / Index test との独立性: the reference standard must be interpreted **blinded to** index test results (signaling question 3.6), and the index test must not form part of a composite reference standard (signaling question 3.4 = incorporation bias)]
- Appropriate time interval: [appropriate interval / 適切な実施間隔: e.g., same day, within 1 week, within 4 weeks — the upper bound during which the disease status is assumed not to change. For long-term follow-up reference standards, state the minimum follow-up period (e.g., ≥6 months). Anchors signaling question 3.8]
- Handling of indeterminate reference standard results: [indeterminate reference / 判定不能 Reference standard の扱い: whether participants with indeterminate reference standard results will be excluded from the analysis or handled via composite adjudication, in a way that reflects clinical management]

> Note: Index test と Reference standard の間隔が長すぎると disease progression bias が生じ得ます。臨床的に妥当な上限 (例) 同日・1 週間以内・4 週間以内) を明示してください。
>
> Note: Reference standard が imperfect (no gold standard) であったり、被験者によって異なる Reference standard が適用される場合は、QUADAS-3 の "Target condition" / "Analysis" ドメインで partial verification bias / differential verification bias として評価されます。事前規定した階層があれば、各研究をどの層の Reference standard で判定されたかで分類できます。

### 3.2.6 Target condition

[target condition / Target condition: 診断対象の疾患・状態の clinical definition、stage/severity range、excluded subtypes]

Alignment between the target condition and the reference standard (QUADAS-3 phase 2):

- Target condition sub-category (if applicable): [target subcategory / Target condition のサブカテゴリ: e.g., not "malignancy in general" but "localized stage I–II colorectal cancer". State that studies evaluating a broader or narrower sub-category will be judged High concern for D3 applicability]
- Acceptable variability in reference standard thresholds: [acceptable threshold variability / Reference standard 閾値差の許容: e.g., a 10² CFU/mL difference is tolerable but 10⁴ is considered a different target condition — consistent with §3.2.5]

## 3.3 Outcomes

### 3.3.1 Primary outcomes

The primary outcomes are the **sensitivity and specificity** of the Index test against the Reference standard, with 95% confidence intervals (CI). For each study we will extract the 2×2 counts (TP / FP / FN / TN) of the Index test and compute sensitivity and specificity.

The unit of analysis is [unit of analysis / 解析単位: e.g., per participant, per sample, per lesion, per scan, per organ. Align with the clinical unit of decision making].

For each study, 95% CIs will be taken from the original report or, when needed, recomputed from the 2×2 table using the **Wilson method or the Jeffreys Bayesian credible interval** [@whiting2026quadas3] (which behave well even at boundary values such as 0/N or N/N).

Following QUADAS-3 Phase 4 [@whiting2026quadas3], for each included study we will identify the accuracy estimates to be carried forward to Phase 5 (risk of bias assessment). A single study may report multiple paired sensitivity/specificity estimates (i.e., multiple 2×2 tables) corresponding to different thresholds, subgroups, reference standards, target-condition definitions, or units of analysis. Only paired estimates linked to the synthesis question(s) prespecified in §2 will be carried forward to Phase 5. The selection rules for this review are:

- Handling of multiple reported thresholds: [phase 4 threshold rule / Phase 4 閾値ルール: e.g., only the 2×2 table at the threshold prespecified in §3.2.3 will be carried forward to Phase 5 / every reported threshold will be treated as a separate estimate and carried forward to Phase 5 / the single threshold closest to the prespecified one will be carried forward to Phase 5]
- Handling of subgroup-stratified estimates: [phase 4 subgroup rule / Phase 4 サブグループルール: e.g., only paired sens/spec for subgroup analyses prespecified in §3.7.x will be treated as separate estimates and carried forward to Phase 5; subgroup-stratified estimates not prespecified in this protocol will not be carried forward]
- Unit of analysis: only 2×2 tables matching the unit of analysis prespecified in §3.3.1 will be carried forward to Phase 5.

> Note: 1 つの研究から複数の候補ペアが上記ルールに同等に整合する場合、どれを Phase 5 評価対象とするかは case-by-case の判断となる。判断要素としては precision (95% CI 幅)、reference standard の risk of bias、target condition 定義の臨床的整合性、unit of analysis の妥当性などがある（QUADAS-3 [@whiting2026quadas3] は順位付けを規定していない）。複数候補がある場合はメンターと協議のうえ決定し、選択した推定値と判断根拠を記録する。

### 3.3.2 Secondary outcomes

1. [secondary diagnostic outcomes / 副次的な精度指標: 例, positive predictive value (PPV), negative predictive value (NPV), likelihood ratio, diagnostic odds ratio, area under the SROC curve]
   - Definition: [outcome definition / アウトカム定義: 2×2 表からの算出式または原著の報告値を採用するかを明示]
2. All adverse events
   - Definition: Adverse events follow each original study's definition. We will tabulate the proportion of participants experiencing adverse events directly caused by the Index test (e.g., contrast-medium allergy, biopsy complication) — distinct from downstream effects of false-positive / false-negative results.
   - Time point: during follow-up
3. [additional secondary outcomes / 追加の副次アウトカム: 例, the proportion of inconclusive / uninterpretable test results]

## 3.4 Search method

> Note: 初回プロトコル作成時は、まず MEDLINE のみを完成させ、CENTRAL・EMBASE・各レジストリの検索式は後回しにして構いません（プロトコルのほかのパートが完成後、メンターの確認を経てから他データベース・レジストリの検索式を整えます）。
>
> Note: DTA レビューでは、MEDLINE/EMBASE 向けに公開されている 診断研究フィルター (diagnostic filter) は感度が不十分とされており、Cochrane DTA Handbook v2 [@deeks2023dtahandbook] は使用しないことを推奨しています。したがって本レビューでは検索フィルターを使わず、Participants（または Target condition）と Index test のブロックを AND で組み合わせる検索式とします。

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

## 3.5 Selection of studies

Two independent reviewers ([screening reviewers / スクリーニング担当者のイニシャル: initials of two reviewers]) will perform title and abstract screening using the Tiab Review plugin [@Kataoka2026-tb], followed by full-text eligibility assessment. We will contact original authors when relevant data are missing. Disagreements between the two reviewers will be resolved by discussion, and if needed a third reviewer ([third reviewer / 第三レビュアーのイニシャル: initials]) will arbitrate.

> note: 3 人以上で screening を行う場合は "two of three independent reviewers..." と記載してください。

## 3.6 Risk of bias assessment

Two reviewers ([risk of bias reviewers / RoB 評価担当者: initials of two reviewers]) will independently assess risk of bias and applicability using QUADAS-3 [@whiting2026quadas3]. Disagreements will be resolved by discussion, and if needed a third reviewer ([third reviewer / 第三レビュアー: initials]) will arbitrate.

QUADAS-3 is structured around six phases. In this protocol:

- **Phase 1 (synthesis questions)** is specified in §2,
- **Phase 2 (ideal test accuracy trial)** elements are prespecified across §3.2.2 (Participants), §3.2.3 (Index test), §3.2.5 (Reference standard), §3.2.6 (Target condition), and §3.3.1 (unit of analysis).

Reviewers will perform phases 3 (flow diagram check), 4 (identifying the accuracy estimates to assess), 5 (signaling question and domain-level judgments), and 6 (overall judgment per accuracy estimate).

Domain-level judgments (Low / High / Insufficient information) are made on the basis of whether deviations from the §3.2 "ideal" conditions are **likely to over- or under-estimate sensitivity or specificity in a clinically meaningful manner**. A single "PN" or "N" signaling-question answer does not automatically force a domain-level High judgment (QUADAS-3 phase 5 guidance [@whiting2026quadas3]).

> Note (比較精度レビュー): 同一被験者に複数の Index test を適用した、もしくは Index test 群にランダム化された比較精度デザインを組み入れる場合は、QUADAS-3 に加え QUADAS-C [@yang2021quadasc] を用いて pair 単位での比較バイアスを評価してください。
>
> Note (AI ベース Index test): Index test が AI/ML モデルの場合、QUADAS-AI（開発中、Sounderajah 2021 [@sounderajah2021quadasaiposition]、Guni 2024 [@guni2024quadasai]）、STARD-AI [@sounderajah2025stardai] の枠組みを参照しつつsignaling questionの更新を検討してください。

## 3.7 Synthesis of results

### 3.7.1 Data extraction

For studies meeting the inclusion criteria, two reviewers ([data extraction reviewers / データ抽出担当者: initials of two reviewers]) will independently extract participant demographics, sample size, Index test details, Reference standard details, threshold, 2×2 counts (TP / FP / FN / TN), and QUADAS-3 domain-level ratings.
Disagreements will be resolved by discussion, and if needed a third reviewer ([third reviewer / 第三レビュアー: initials]) will arbitrate.
To improve efficiency, AI may be used to assist data extraction [@Gartlehner2025-cm;@Kataoka2025-kq]. The actual use of AI will be reported following the Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru].

### 3.7.2 Meta-analysis

Synthesis follows the recommendations of the Cochrane DTA Handbook v2 [@deeks2023dtahandbook].

For each study we will compute sensitivity and specificity with 95% CI from the 2×2 table and present them in a paired forest plot (sensitivity and specificity side by side). We will also plot study-level sensitivity/specificity pairs on the SROC plane and describe their distribution.
A hierarchical model will be used to pool primary-study results.
When the included studies are considered to use a common threshold, we will use a bivariate model and present a summary point with 95% confidence and 95% prediction regions on the ROC plane.
When the included studies are not considered to use a common threshold, we will use an HSROC model and present the pooled result on the ROC plane.
All analyses will be performed in MetaDTA [@patel2021metadta] ([https://crsu-metadta.le.ac.uk/MetaDTA/](https://crsu-metadta.le.ac.uk/MetaDTA/)).

> Note: MetaDTA は bivariate モデルを主に実装しています。HSROC を必要とする閾値混在ケースで MetaDTA の機能で不十分な場合は、R `mada` パッケージ (CRAN) または Stata `metandi` / `metadta` の併用を検討してください。その場合、使用ソフトウェアとバージョンを §3.7.2 に追記してください。

Adverse events will be summarized narratively per study definition; we will not perform meta-analysis of adverse events.

## 3.8 Heterogeneity

Between-study variability in sensitivity and specificity will be assessed visually on the SROC plane and the paired forest plot, and by the width of the prediction region from the bivariate / HSROC model. The `I²` statistic and its cutoff values are not recommended for DTA meta-analysis [@deeks2023dtahandbook] and will not be used.

When substantial heterogeneity is observed, we will explore the following pre-specified subgroups or covariates via meta-regression:

1. [participant subgroup / 対象者サブグループ: 例, age group (children vs adults), prevalence, symptom status, setting (primary/secondary/tertiary care)]
2. [index test subgroup / Index test サブグループ: 例, device manufacturer, model version, reader expertise, threshold category]
3. [reference standard subgroup / Reference standard サブグループ: 例, single vs composite reference standard, follow-up duration]
4. [methodological subgroup / 方法論的サブグループ: 例, QUADAS-3 low-risk-only studies vs all studies, prospective vs retrospective]

## 3.9 Sensitivity analysis

For the primary outcome, we will assess the robustness of results to review-process decisions with the following sensitivity analyses:

1. Excluding studies rated High risk on one or more QUADAS-3 domains (especially [most influential domain / 最も結果に影響しそうな QUADAS-3 ドメイン番号: 例, Patient selection (D1)])
2. [other sensitivity analysis / その他の感度分析: 例, excluding conference-abstract-only studies, excluding studies with imputed cell counts, excluding the largest study]

## 3.10 Reporting bias

We will search trial registries (ClinicalTrials.gov and ICTRP) for completed but unpublished studies. Following the Cochrane DTA Handbook v2 [@deeks2023dtahandbook], we will not perform statistical tests for publication bias (such as funnel plots or Egger's test), because their validity in DTA meta-analysis is not established.

# 4. Summary of findings table

The Summary of Findings table will be constructed following the Cochrane DTA Handbook v2 [@deeks2023dtahandbook] for the following outcomes: [outcomes for SoF table / SoF テーブルに含めるアウトカム: 例, sensitivity and specificity, TP/FP/FN/TN per 1,000 at an assumed prevalence, estimated patient impact].

# 5. Conflict of Interest

The authors declare that they have no conflicts of interest.

# 6. Funding

Self-funded.

> Note: 金銭的支援（英文校正費・データベース利用料・解析支援費など）に加え、人手の支援（例: 司書による検索式作成支援、AI ツールの提供、所属機関のサポート等）があれば記載してください。資金提供者やスポンサーがいる場合は、その名称と、本研究のデザイン・データ収集・解析・結果解釈・出版判断のいずれに関与/不関与かも併記してください。いずれもなければ「自己資金。」のままで構いません。

# Use of artificial intelligence in manuscript preparation

We used [AI tool and version / 使用した生成 AI の名称とバージョン: e.g., Claude Code (Anthropic), v2.1.168, model Claude Opus 4.8] to proofread and copy-edit the text of this protocol. AI was not used to generate or select references, to produce or interpret data, or to make methodological decisions. The authors reviewed and verified all content and take full responsibility for the final manuscript.

> Note: 本プロトコルや本文の文章作成・校正に生成 AI を使った場合は、ツール名とバージョンを明記してください。使っていなければこのセクションは削除して構いません。References の作成・挿入に AI を使ってはいけません（# References の Note 参照）。

# References

> Note: References（引用文献リスト）は AI に作成・挿入させないでください。AI は実在しない文献・誤った著者名・巻号・DOI を生成することがあります。引用を入れ終えたら、提出前に必ず <https://citation-checker-three.vercel.app/> ですべての citation をチェックしてください。誤った citation は投稿時に機械的にチェックされ、それが原因でリジェクトされた事例があります。

::: {#refs}
:::

\newpage

# Appendices

## Appendix 1: MEDLINE (PubMed) search strategy

> 03_06、03_07 の検索式の課題については、フォームに入力し、その旨を URL とともに Slack でメンターに伝えてください。

> Note: DTA レビューの検索式作成のステップ
>
> 1. 検索ブロックを決める（典型: Participants または Target condition、Index test）
> 2. 各ブロックの統制語（MeSH 等）として何を使うかを考える
> 3. 各ブロックを自由語と統制語で展開する
> 4. ブロックを AND で組み合わせる
> 5. 診断研究フィルター (diagnostic filter) は使用しない（感度不足のため、Cochrane DTA Handbook v2 [@deeks2023dtahandbook] が非推奨）
>
> 下書き支援ツール（要 Google アカウントの無料登録）: [https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&amp;usp=sharing](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

[MEDLINE search strategy / MEDLINE の検索式: Participants (または Target condition) と Index test の検索語、MeSH、組み合わせ式を記入。診断研究フィルターは付けない]

## Appendix 2: CENTRAL (Cochrane Library) search strategy

[CENTRAL search strategy / CENTRAL の検索式: Participants (または Target condition) と Index test の検索語、組み合わせ式を記入]

## Appendix 3: EMBASE (Dialog) search strategy

> Note: 初回プロトコル作成時はこの Appendix は空欄のままで構いません。MEDLINE の検索式が確定してから、対応する Emtree と自由語に置き換えて作成します。診断研究フィルターは付けません。

[EMBASE search strategy / EMBASE の検索式: Participants (または Target condition) と Index test の検索語、Emtree、組み合わせ式を記入]

## Appendix 4: ICTRP search strategy

[ICTRP search strategy / ICTRP の検索式: Target condition、Index test、類義語、検索日を記入]

## Appendix 5: ClinicalTrials.gov search strategy

- Condition or disease: [condition or disease / 対象状態: ClinicalTrials.gov に入力する Target condition 名や類義語]
- Intervention / Other terms: [index test terms / Index test 関連語: ClinicalTrials.gov に入力する Index test 名や類義語]
