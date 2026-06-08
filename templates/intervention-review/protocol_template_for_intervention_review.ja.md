---
title: "介入レビュー プロトコルテンプレート"
author:
  - SRWS-PSG Mentors
date: 2026-05-16
version: 3.0.0 (draft)
lang: ja
keywords:
  - systematic review protocol
  - intervention review
  - PRISMA 2020
  - Cochrane Handbook
license: CC BY 4.0
repository: https://github.com/SRWS-PSG/protocol-templates
template-path: templates/intervention-review
zenodo-concept-doi: 10.5281/zenodo.20586625
bibliography: references.bib
csl: vancouver.csl
link-citations: true
notes-after-punctuation: true
---
> このテンプレートの使い方
>
> この文書は介入レビューの SR プロトコルテンプレートです。`[English label / 日本語ラベル: 記入する内容]` で示した箇所を、自分たちのレビュー内容に置き換えてください。
>
> まず `2. Research question` で PICO を決め、次に `3.2 Inclusion criteria`、`3.3 Type of outcomes`、`Appendices` の検索式、`3.7` 以降の解析計画を埋めると進めやすいです。固定文は原則そのまま使えますが、研究疑問や組み入れる研究デザインに合わない場合はメンターに確認して修正してください。
>
> Note は作成中の補助説明です。提出版や登録版では、必要に応じて削除してください。
> メンターの所属は `https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit?usp=sharing` を参照してください。
>
> ライセンス: 本テンプレートは [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) で公開されています。出典として Zenodo DOI を明記すれば、利用・改変・再配布が可能です。

\newpage

# Title

Title: [review title / レビュータイトル: 対象者、介入、比較対照、主要アウトカムが分かる短い英語表現]: a systematic review and meta-analysis protocol

> Note: 介入レビューで RCT のみを組み入れる場合は、タイトルに *efficacy* を使ってください（理由: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC351867/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC351867/)）。

## Authors:

> メンターの名前もお忘れなく

Corresponding author: [corresponding author / 連絡著者（メンティー）: full name]

Address: [address / 連絡著者の所属先住所: department, institution, postal address]

E-mail: [e-mail / 連絡著者の連絡先メールアドレス]

Author contributions:

[guarantor initials / 連絡責任者のイニシャル] が本研究の保証人 (guarantor) を務めた。[drafting author initials / 原稿ドラフト担当者のイニシャル] が原稿を執筆した。すべての著者が組み入れ基準、バイアスリスク評価戦略、データ抽出基準の策定に貢献した。[search strategy author initials / 検索式担当者のイニシャル] が検索式を作成した。[statistics author initials / 統計担当者のイニシャル] が統計的助言を提供した。[content expert initials / 臨床・方法論の専門家のイニシャル] が [expertise area / 専門領域: 対象疾患、介入、方法論など] についての専門的助言を提供した。すべての著者が最終原稿を読み、フィードバックを行い、承認した。


\newpage


> *Note*: プロトコルであるため、Abstract は必須ではありません。もし書きたい場合は、PRISMA 2020 [@page2021prisma] の Abstract 項目（PRISMA 2020 abstract checklist）を参考に、必要に応じて以下の見出しを修正して使用してください。
>
> # Abstract
>
> - Background — Objectives
> - Methods
> - Eligibility criteria
> - Information sources
> - Risk of bias
> - Synthesis of results
> - Discussion
> - Funding
> - Registration

\newpage

# 1. Introduction

> Note: 背景の書き方
>
> すべての記述にリファレンスを付けてください。3 パラグラフ構成を推奨します。
>
> 第一パラグラフ — P（対象疾患）について 4–5 文。例:
>
> 1. P の疾患は世界的な問題である
> 2. P の疾患の頻度・治療を要する患者数
> 3. P の疾患の標準的な治療法の説明
> 4. 標準的な治療法では不十分である点
>
> 第二パラグラフ — I（介入）について 4–5 文。例:
>
> 1. I が有用であるという報告がいくつかある
> 2. 臨床現場で P に対して I を使っている割合は xx くらいあると報告がある
>    3–4. I は yy という機序で改善する可能性が示唆されている
> 3. 一方、I は zz という害がある
>
> 第三パラグラフ — なぜ SR を行うべきか 3–4 文。例:
>
> 1. このトピックに関して益と害の available evidence をまとめたものはなく、効果についても先行研究でばらつきがある
> 2. 臨床で広く使われている P における I に関してエビデンスの確実性評価は重要である
> 3. そのため本研究ではこのトピックにおける SR&MA を行う
>
> 背景を対話で指導してくれる GPTs: [https://chatgpt.com/g/g-YF7pcAKdG-background-editor](https://chatgpt.com/g/g-YF7pcAKdG-background-editor)
> すべての記述に必要に応じてリファレンスを付ける

# 2. Research question

- P: [participants / 対象者: 疾患、状態、年齢層、診断基準、重症度、診療場面など]
- I: [intervention / 介入: 介入名、用量、頻度、期間、実施方法など]
- C: [comparator / 比較対照: placebo、usual care、無治療、他治療など]
- O: [outcomes / アウトカム: 主要アウトカムを中心に]

# 3. Method

## 3.1 Protocol

本レビューでは、SRWS-PSG が管理するシステマティック・レビュー プロトコルテンプレート [@Kataoka2026-cj] を使用した。本プロトコルの作成にあたっては Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 (PRISMA 2020) 声明 [@page2021prisma] および PRISMA-P 2015 [@shamseer2015] に従った。本プロトコルは OSF.io ([https://osf.io/](https://osf.io/)) に公開する予定である。

## 3.2 Inclusion criteria of the articles for the review

### 3.2.1 Type of studies

[intervention and target condition / 評価する介入と対象状態: 例, intervention for participants with condition] を評価したランダム化比較試験 (RCT) を組み入れる。言語および研究実施国の制限は設けない。出版済論文、未出版論文、学会抄録、letter を含むすべての文献を対象とする。[excluded study designs or records / 除外する研究デザイン・文献種別: 例, quasi-randomized trials, observational studies] は除外する。観察期間や出版年による除外は行わない。

### 3.2.2 Study participants

[participants overview / 対象者の概要: 疾患・状態、年齢層、診断基準、重症度、診療場面などを文章で記入]

組み入れ基準: [participant inclusion criteria / 対象者の組入基準: 対象疾患、診断基準、年齢、性別、重症度、セッティングなど]

除外基準: [participant exclusion criteria / 対象者の除外基準: 除外する併存疾患、既治療、特定集団など]

### 3.2.3 Intervention

[intervention details / 介入の詳細: 介入名、用量、頻度、期間、実施者、併用療法の扱いなど]

### 3.2.4 Control

[comparator details / 比較対照の詳細: placebo、usual care、無治療、他治療、併用療法の扱いなど]

## 3.3 Type of outcomes

### 3.3.1 Primary outcomes

> Note: 主要アウトカムの選び方
>
> 最大で 3 つまでとし、そのうち少なくとも 1 つには望ましくない効果（害）のアウトカムを含めてください。各アウトカムは「測定指標」「分子・分母」「観察期間（評価時点）」までを定義します。例:
>
> - 例 1: 28 日死亡割合
>   - 分子: 研究開始から 28 日後までに死亡した人数
>   - 分母: 研究に組み入れられた人数
>   - 評価時点: 研究開始 28 日後
> - 例 2: 疼痛 (VAS)
>   - 測定指標: visual analogue scale (0–100 mm)
>   - 評価時点: 介入から 1 週間後

1. [primary outcome name / 主要アウトカム名: 例, all-cause mortality]
   - 定義: [outcome definition / アウトカム定義: 測定指標、判定基準、スコアの向き、イベントの定義、分子と分母など]
   - 評価時点: [time point / 評価時点: 例, closest to 12 weeks, during follow-up period]
2. [primary outcome name / 主要アウトカム名]
   - 定義: [outcome definition / アウトカム定義]
   - 評価時点: [time point / 評価時点]
3. [primary outcome name / 主要アウトカム名]
   - 定義: [outcome definition / アウトカム定義]
   - 評価時点: [time point / 評価時点]

### 3.3.2 Secondary outcomes

1. [secondary outcome name / 副次アウトカム名]
   - 定義: [outcome definition / アウトカム定義: 測定指標、判定基準、スコアの向き、イベントの定義など]
   - 評価時点: [time point / 評価時点]
2. [secondary outcome name / 副次アウトカム名]
   - 定義: [outcome definition / アウトカム定義]
   - 評価時点: [time point / 評価時点]
3. All adverse events
   - 定義: 有害事象の定義は原著者の定義に従う。すべての有害事象の発症割合を集計する。
   - 評価時点: フォローアップ期間中

## 3.4 Search method

> Note: 初回プロトコル作成時は、まず MEDLINE のみを完成させ、CENTRAL・EMBASE・各レジストリの検索式は後回しにして構いません（フォーム入力後、メンターの確認を経てから他データベース・レジストリの検索式を整えます）。

### 3.4.1 Electronic search

以下のデータベースを検索する。

1. MEDLINE (PubMed)
2. the Cochrane Central Register of Controlled Trials (Cochrane Library)
3. EMBASE (Dialog)

検索式は Appendix 1、2、3 を参照のこと。

### 3.4.2 Other resources

進行中または未出版の試験について、以下のレジストリも検索する。

1. the World Health Organization International Clinical Trials Platform Search Portal (ICTRP)
2. ClinicalTrials.gov

検索式は Appendix 4 および 5 を参照のこと。

組み入れ研究のリファレンスリスト、国際的な診療ガイドライン ([guideline names or organizations / 確認する診療ガイドライン名・作成組織])、ならびに組み入れ研究を引用している論文のリファレンスリストもチェックする。原著者には、未出版データや追加データの提供を依頼する。

## 3.5 Data collection and analysis

### 3.5.1 Selection of the studies

2 人の独立したレビュアー ([screening reviewers / スクリーニング担当者のイニシャル: initials of two reviewers]) が、Tiab Review plugin [@Kataoka2026-tb] を用いてタイトルおよび抄録のスクリーニングを行い、続いてフルテキストに基づき適格性を評価する。関連するデータが欠けている場合は原著者に問い合わせる。2 人のレビュアー間の不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアーのイニシャル: initials]) が裁定者として加わる。

> note: 3 人以上で screening を行う場合は "two of three independent reviewers..." と記載してください。

### 3.5.2 Data extraction and management

2 人のレビュアー ([data extraction reviewers / データ抽出担当者のイニシャル: initials of two reviewers]) が、標準化されたデータ収集フォームを用いて、組み入れ研究のデータを独立して抽出する。
フォームには研究デザイン、研究集団、介入、アウトカムに関する情報を含める。

> Note: ここは表を作るつもりで、すべての変数名を書いてください。

不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアーのイニシャル: initials]) が裁定者として加わる。
効率向上のため、必要に応じて AI をデータ抽出の補助に用いる [@Gartlehner2025-cm;@Kataoka2025-kq]。AI を実際にどう用いたかは、Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru] に従って報告する。

## 3.6 Assessment of risk of bias in included studies

2 人のレビュアー ([risk of bias reviewers / RoB 評価担当者: initials of two reviewers]) が Risk of Bias 2 ツール [@sterne2019rob2] を用いて独立にバイアスリスクを評価する。不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアー: initials]) が裁定者として加わる。

## 3.7 Measures of treatment effects

以下の二値アウトカムについては、相対リスク (relative risk) と 95% 信頼区間 (CI) を統合する: [binary outcomes / 二値アウトカム: 例, mortality, response, adverse events]。

以下の連続アウトカムについては、平均差 (mean difference, MD) と 95% CI を統合する: [continuous outcomes / 連続アウトカム: 例, symptom score, quality-of-life score]。

組み入れ研究で異なる尺度が用いられている場合は、標準化平均差 (standardized mean difference, SMD) を用いて統合する。

有害事象は原著の定義に従ってまとめるが、メタアナリシスは行わない。

## 3.8 Unit of analysis issues

クラスターランダム化試験における登録単位でのクラスタリング。 クラスターRCT の二値データについては、Cochrane Handbook 16.3.5 章 [@higgins2024cochrane] に従い、ユニット内の級内相関係数 (intra-cluster correlation coefficient, ICC) と平均クラスターサイズを用いて design effect を適用し、実効サンプルサイズおよび実効イベント数を算出する。ICC が報告されていない場合は類似研究の ICC で代替する。連続データについてはサンプルサイズのみを縮小し、平均値と標準偏差はそのまま用いる [@higgins2024cochrane]。

ランダム化クロスオーバー試験。 二値アウトカムについては、クロスオーバー試験の第 1 期のデータを使用する。利用できない場合は両期のデータを並行群試験として扱う。

連続アウトカムについては以下の優先順位でデータを使用する。

1. 第 1 期のデータ
2. 介入期と対照期の平均差およびその SD
3. 上記 SD が得られない場合は、95% CI、t 統計量、または t 検定の p 値から計算する
4. 上記いずれの統計量も得られない場合は、Cochrane Handbook 23.2.7 章に従い、介入期と対照期の平均差の SD を近似的に補完する

複数群比較。 本レビューに関連するすべての介入群を組み入れる。

## 3.9 Handling of missing data

提示されていないデータについては原著者に問い合わせる。

### 3.9.1 Missing outcomes

すべての二値データについては可能な限り intention-to-treat (ITT) 解析を行う。連続データについては、Cochrane Handbook [@higgins2024cochrane] の推奨に従い、欠測値の補完は行わない。原著研究で利用可能なデータでメタアナリシスを行う。

### 3.9.2 Missing statistics

原著で標準誤差または p 値のみが報告されている場合は、Altman の方法 [@altman1996skewness] に基づき標準偏差を計算する。原著者に問い合わせても得られない場合は、信頼区間および t 値から Cochrane Handbook [@higgins2024cochrane] の方法、または妥当性が検証された方法 [@furukawa2006imputing] に基づき標準偏差を算出する。これらの方法の妥当性は感度分析で検証する。

## 3.10 Assessment of heterogeneity

フォレストプロットの目視および *I*² 統計量により統計的異質性を評価する (*I*² 0–40%: 重要でない可能性; 30–60%: 中等度の異質性の可能性; 50–90%: 実質的な異質性の可能性; 75–100%: 大きな異質性)。実質的な異質性 (*I*² > 50%) が認められる場合は、その原因を検討する。*I*² 統計量に対しては Cochran χ² 検定 (Q 検定) を行い、P 値 0.10 未満を統計学的に有意とみなす。

## 3.11 Assessment of reporting bias

臨床試験登録 (ClinicalTrials.gov および ICTRP) を検索するとともに、未出版試験について広範な文献検索を行う。アウトカム報告バイアスを評価するため、試験プロトコルで定義されたアウトカムと出版物で報告されたアウトカムを比較する。出版バイアスはファンネルプロットの目視により評価する。Egger 検定により出版バイアスを評価する。組み入れ試験が 10 件未満、もしくはサンプルサイズの似た試験のみの場合は本検定を行わない。

## 3.12 Meta-analysis

メタアナリシスは PMA tools ([https://yukifurukawa.jp/pmatools/](https://yukifurukawa.jp/pmatools/)) を用いて行う。ランダム効果モデルを用いる。

## 3.13 Subgroup analysis

効果修飾因子の影響を検討するため、十分なデータが得られた場合、主要アウトカムについて以下の因子でサブグループ解析を行う。

1. (For participants) [participant subgroup factor / 対象者に関するサブグループ因子: 例, age group, disease severity]
2. (For intervention) [intervention subgroup factor / 介入に関するサブグループ因子: 例, dose, duration, delivery method]

## 3.14 Sensitivity analysis

主要アウトカムについて、レビュー過程の判断に対する結果の頑健性を評価するため、以下の感度分析を行う。

1. 補完された統計量を用いた研究の除外
2. 欠測参加者: informative missingness odds ratio を求めて結果の頑健性を検証する [@furukawa2006imputing]
3. 完全データで研究を完了した参加者のみによる解析

# 4. Summary of findings table

2 人のレビュアー ([GRADE reviewers / GRADE 評価担当者のイニシャル、一人はメンター: initials of two reviewers, including one mentor if applicable]) が GRADE (Grading of Recommendations Assessment, Development and Evaluation) アプローチ [@Guyatt2011-qq] に基づきエビデンスの確実性を評価する。不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアーのイニシャル: initials]) が裁定者として加わる。Summary of Findings テーブルは、Cochrane Handbook [@higgins2024cochrane] に基づき以下のアウトカムについて作成する: [outcomes for Summary of Findings table / SoF テーブルに含めるアウトカム: 主要アウトカムと重要な副次アウトカム]。

# 5. Conflict of Interest

著者らは利益相反を有しない。

# 6. Support

自己資金。

> Note: 金銭的支援（英文校正費・データベース利用料・解析支援費など）に加え、人手の支援（例: 司書による検索式作成支援、AI ツールの提供、所属機関のサポート等）があれば記載してください。いずれもなければ「自己資金。」のままで構いません。

# Use of artificial intelligence in manuscript preparation

本プロトコルの文章の校正・推敲に [AI tool and version / 使用した生成 AI の名称とバージョン: 例, Claude Code (Anthropic), v2.1.168, model Claude Opus 4.8] を用いた。AI は参考文献の作成・選定、データの作成・解釈、方法論上の判断には使用していない。著者はすべての内容を確認・検証し、最終原稿に全責任を負う。

> Note: 本プロトコルや本文の文章作成・校正に生成 AI を使った場合は、ツール名とバージョンを明記してください。使っていなければこのセクションは削除して構いません。References の作成・挿入に AI を使ってはいけません（# References の Note 参照）。

# References

> Note: References（引用文献リスト）は AI に作成・挿入させないでください。AI は実在しない文献・誤った著者名・巻号・DOI を生成することがあります。引用を入れ終えたら、提出前に必ず <https://citation-checker-three.vercel.app/> ですべての citation をチェックしてください。誤った citation は投稿時に機械的にチェックされ、それが原因でリジェクトされた事例があります。

::: {#refs}
:::

\newpage

# Appendices

## Appendix 1: MEDLINE (PubMed) search strategy

> 03_06、03_07 の検索式の課題については、フォームに入力し、その旨を URL とともに Slack でメンターに伝えてください。

> Note: 検索式作成のステップ
>
> 1. どういう検索ブロック（例: participants、intervention、study design など）に分けるかを決める
> 2. 各ブロックの統制語（MeSH 等）として何を使うかを考える
> 3. 各ブロックを自由語と統制語で展開する
> 4. ブロックを AND で組み合わせる
>
> 下書き支援ツール（要 Google アカウントの無料登録）。組み入れ基準を入力すると検索式の下書きを生成してくれます: [https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&amp;usp=sharing](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

[MEDLINE search strategy / MEDLINE の検索式: participants と intervention の検索語、MeSH、RCT filter、組み合わせ式を記入]

## Appendix 2: CENTRAL (Cochrane Library) search strategy

> Note: CENTRAL では RCT フィルター不要です。

[CENTRAL search strategy / CENTRAL の検索式: participants と intervention の検索語、組み合わせ式を記入。RCT filter は不要]

## Appendix 3: EMBASE (Dialog) search strategy

> Note: 初回プロトコル作成時はこの Appendix は空欄のままで構いません。MEDLINE の検索式が確定してから、対応する Emtree と自由語に置き換えて作成します。

[EMBASE search strategy / EMBASE の検索式: participants と intervention の検索語、Emtree、下記 RCT filter との組み合わせ式を記入]

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

[ICTRP search strategy / ICTRP の検索式: condition、intervention、類義語、検索日を記入]

## Appendix 5: ClinicalTrials.gov search strategy

- Condition or disease: [condition or disease / 対象疾患・状態: ClinicalTrials.gov に入力する疾患名や類義語]
- Intervention: [intervention / 介入: ClinicalTrials.gov に入力する介入名や類義語]
