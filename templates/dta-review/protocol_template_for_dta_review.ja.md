---
title: "診断精度レビュー プロトコルテンプレート"
author:
  - SRWS-PSG Mentors
date: 2026-05-20
version: 1.0.0 (draft)
lang: ja
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

> Note: 過去版の更新としてプロトコルを公開する場合は、本タイトル末尾に "(update)" を付け、YAML front-matter の `is-update` を `true` に変更してください。

## Authors:

> メンターの名前もお忘れなく

Corresponding author: [corresponding author / 連絡著者（メンティー）: full name]

Address: [address / 連絡著者の所属先住所: department, institution, postal address]

E-mail: [e-mail / 連絡著者の連絡先メールアドレス]

Author contributions:

[guarantor initials / 連絡責任者のイニシャル] が本研究の保証人 (guarantor) を務めた。[drafting author initials / 原稿ドラフト担当者のイニシャル] が原稿を執筆した。すべての著者が組み入れ基準、QUADAS-3 評価戦略、データ抽出基準の策定に貢献した。[search strategy author initials / 検索式担当者のイニシャル] が検索式を作成した。[statistics author initials / 統計担当者のイニシャル] が診断精度メタアナリシス（bivariate / HSROC モデル）について統計的助言を提供した。[content expert initials / 臨床・方法論の専門家のイニシャル] が [expertise area / 専門領域: 対象疾患、Index test、Reference standard、方法論など] についての専門的助言を提供した。すべての著者が最終原稿を読み、フィードバックを行い、承認した。

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
> すべての記述に必要に応じてリファレンスを付ける

# 2. Research question

DTA レビューでは PICO ではなく、Cochrane DTA Handbook v2 [@deeks2023dtahandbook] の枠組みに従って Participants / Index test / (Comparator) / Reference standard / Target condition を定義する。

- P (Participants): [participants / 対象者: 疾患疑い・症状・スクリーニング集団など、Index test を適用する集団]
- I (Index test): [index test / Index test: 評価対象の検査名、機器・モデル名、判定者の資格、閾値の扱い]
- C (Comparator, optional): [comparator index test / 比較対象 Index test: 同一被験者に実施される代替検査を比較する場合のみ記入。比較しない場合は "該当なし" と書く]
- R (Reference standard): [reference standard / 参照基準: 真の状態を定義する検査・診断基準、判定タイミング、判定者]
- T (Target condition): [target condition / 対象とする状態: 診断対象の疾患・状態、定義]

レビュークエスチョン:

1. [research question 1 / リサーチクエッション 1: Participants における Index test の Target condition に対する診断精度はどの程度か]
2. [research question 2 / リサーチクエッション 2: 必要に応じて Comparator との比較、サブグループ、閾値依存性などを追加]

## Keywords

> Note: アルファベット順に 5 つまで、セミコロンとスペースで区切って記載する（タイトルやアブストラクトに現れる語と異なることが理想的）。

[keywords / キーワード: 例) diagnostic accuracy; index test; reference standard; sensitivity and specificity; target condition]

# 3. Method

## 3.1 Protocol

本レビューでは、SRWS-PSG が管理する診断精度レビュー プロトコルテンプレート（リポジトリ: [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates)、Zenodo concept DOI: 10.5281/zenodo.&lt;TBD&gt;）を使用した。本プロトコルの作成および本レビューの実施にあたっては Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy v2.0 [@deeks2023dtahandbook] に従う。本レビューの報告は PRISMA-DTA 声明 [@mcinnes2018prismadta] および同 E&E [@salameh2020prismadtaee] に従う。本プロトコルは PROSPERO ([https://www.crd.york.ac.uk/prospero/](https://www.crd.york.ac.uk/prospero/)) に登録する予定である。

## 3.2 Inclusion criteria of the studies for the review

### 3.2.1 Type of studies

[participants and index/target / 対象者・Index test・Target condition: 例, the diagnostic accuracy of [index test] for [target condition] in [participants]] の診断精度を検討した以下の研究を組み入れる。

- 横断的にコホートを Index test と Reference standard の両方で評価した cohort 研究（前向き・後ろ向きを問わない）
- ランダム化比較試験 (RCT) の二次解析として診断精度が報告されているもの
- Case-control デザイン (two-gate / diagnostic case-control)

Reference standard を元に、Index test の真陽性 (TP)、偽陽性 (FP)、偽陰性 (FN)、真陰性 (TN) の数を抽出できる、もしくは 2×2 表を再構成できる研究のみを組み入れる。

言語および研究実施国の制限は設けない。出版済論文、未出版論文、学会抄録、letter を含むすべての文献を対象とする。Case series および case report は除外する。観察期間や出版年による除外は行わない。

> Note (比較精度レビューの場合): 同一被験者に複数の Index test を適用した paired comparative accuracy study、または対象者を Index test 群にランダム化した randomized comparative accuracy study を組み入れる場合は、§3.5 のバイアスリスク評価で QUADAS-C [@yang2021quadasc] を併用してください。

### 3.2.2 Participants

[participants overview / 対象者の概要: 疾患・状態の疑い、年齢層、診療場面、Index test を適用する臨床的タイミングなどを文章で記入]

組み入れ基準: [participant inclusion criteria / 対象者の組入基準: 対象疾患疑い、年齢、性別、セッティング (一次・二次・三次医療、検診など)、症状の有無]

除外基準: [participant exclusion criteria / 対象者の除外基準: 除外する併存疾患、既治療、特定集団など]

### 3.2.3 Index test

[index test details / Index test の詳細: 検査名、機器・試薬・モデル (AI/ML の場合はバージョン)、実施手順、判定者の資格、判定の盲検化、使用する閾値 (cutoff)・閾値設定方針]

> Note: 閾値 (cutoff) を1つに固定するか、複数の閾値を許容するかは、解析方針（§3.6）と密接に関わるため、ここで明示してください。閾値を「研究ごとに事後選択された最適閾値」とする場合、HSROC モデルでの解析が前提となります。
>
> Note (AI/ML を Index test とする場合): モデル名、バージョン、訓練データセット、入力データの前処理、判定の自動化レベル (fully automated / semi-automated / with human-in-the-loop) を明示してください。バイアスリスクは QUADAS-AI（開発中）[@guni2024quadasai;@sounderajah2021quadasaiposition] と STARD-AI [@sounderajah2025stardai] を参照すべきですが、QUADAS-AI が未公開の場合は QUADAS-3 の各ドメインに対し AI 特有の signaling questions を追加してください。

### 3.2.4 Comparator (optional)

[comparator details / 比較対象 Index test の詳細: 比較対象がある場合のみ。Index test と同一の被験者・同一の Reference standard で評価された別の検査名、閾値、実施者など。比較対象がなければ「該当なし」と記入]

### 3.2.5 Reference standard

[reference standard / Reference standard: 真の Target condition の有無を判定する基準（臨床診断、組織診、長期フォローアップ、複合 reference standard など）、判定タイミング (Index test と何時間/何日以内に実施されたか)、判定者の盲検化]

> Note: Index test と Reference standard の実施間隔 (interval) が長すぎると、その間に状態が変化することで Disease progression bias が生じます。臨床的に妥当な上限を明示してください（例: 同日内、1 週間以内、4 週間以内など）。
>
> Note: Reference standard が完全 (gold standard) ではない場合、または被験者によって異なる reference standard が用いられる場合は、QUADAS-3 の "Reference standard" および "Flow and timing" ドメインで partial verification / differential verification bias として評価されます。

### 3.2.6 Target condition

[target condition / Target condition: 診断対象の疾患・状態の臨床的定義、病期・重症度の範囲、除外する亜型など]

## 3.3 Outcomes

### 3.3.1 Primary outcomes

Primary outcome は、Reference standard を真値とした Index test の **感度 (sensitivity) と特異度 (specificity)** および 95% 信頼区間 (CI) である。研究ごとに Index test の真陽性 (TP)、偽陽性 (FP)、偽陰性 (FN)、真陰性 (TN) の数を抽出し、これらから感度・特異度を算出する。

### 3.3.2 Secondary outcomes

1. [secondary diagnostic outcomes / 副次的な精度指標: 例, positive predictive value (PPV), negative predictive value (NPV), likelihood ratio, diagnostic odds ratio, area under SROC curve]
   - 定義: [outcome definition / アウトカム定義: 2×2 表からの算出式または原著の報告値を採用するかを明示]
2. All adverse events
   - 定義: 有害事象の定義は原著者の定義に従う。Index test に起因する有害事象（造影剤アレルギー、生検合併症など、偽陽性・偽陰性による下流の影響とは別の直接的害）を発症した人数の割合を集計する。
   - 評価時点: フォローアップ期間中
3. [additional secondary outcomes / 追加の副次アウトカム: 例, inconclusive/uninterpretable result の割合]

## 3.4 Search method

> Note: 初回プロトコル作成時は、まず MEDLINE のみを完成させ、CENTRAL・EMBASE・各レジストリの検索式は後回しにして構いません（プロトコルのほかのパートが完成後、メンターの確認を経てから他データベース・レジストリの検索式を整えます）。
>
> Note: DTA レビューでは、MEDLINE/EMBASE 向けに公開されている **診断研究フィルター (diagnostic filter)** は感度が不十分とされており、Cochrane DTA Handbook v2 [@deeks2023dtahandbook] は使用しないことを推奨しています。したがって本レビューでは検索フィルターを使わず、Participants（または Target condition）と Index test のブロックを AND で組み合わせる検索式とします。

検索期間: [search date range / 検索対象期間: 例) inception to YYYY-MM-DD]

### 3.4.1 Electronic search

以下のデータベースを検索する。

1. MEDLINE (PubMed)
2. the Cochrane Central Register of Controlled Trials (CENTRAL)
3. EMBASE (Dialog)

検索式は Appendix 1、2、3 を参照のこと。

### 3.4.2 Other resources

進行中または未出版の研究について、以下のレジストリも検索する。

1. the World Health Organization International Clinical Trials Registry Platform (ICTRP)
2. ClinicalTrials.gov

検索式は Appendix 4 および 5 を参照のこと。

組み入れ研究のリファレンスリスト、国際的な診療ガイドライン ([guideline names or organizations / 確認する診療ガイドライン名・作成組織])、ならびに組み入れ研究を引用している論文のリファレンスリストもチェックする。原著者には、未出版データや追加データ (特に 2×2 表の再構成に必要なセル数) の提供を依頼する。

## 3.5 Risk of bias assessment

2 人のレビュアー ([risk of bias reviewers / RoB 評価担当者: initials of two reviewers]) が QUADAS-3 [@whiting2026quadas3] を用いて独立にバイアスリスクおよび適用可能性 (applicability) を評価する。不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアー: initials]) が裁定者として加わる。

> Note: QUADAS-2 [@whiting2011quadas2] は 2026 年 2 月公開の QUADAS-3 [@whiting2026quadas3] により改訂されました。2026 年以降に新規開始する DTA SR は QUADAS-3 の使用を推奨します。既に QUADAS-2 で評価を開始している進行中のレビューについては、QUADAS-2 のままで完了して差し支えありませんが、その旨を本セクションで明示してください。
>
> Note (比較精度レビュー): 同一被験者に複数の Index test を適用した、もしくは Index test 群にランダム化された比較精度デザインを組み入れる場合は、QUADAS-3 に加え QUADAS-C [@yang2021quadasc] を用いて pair 単位での比較バイアスを評価してください。
>
> Note (AI ベース Index test): Index test が AI/ML モデルの場合、QUADAS-AI（開発中、Sounderajah 2021 position [@sounderajah2021quadasaiposition]、Guni 2024 protocol [@guni2024quadasai]）の枠組みを参照しつつ、原著研究側の報告品質は STARD-AI [@sounderajah2025stardai] で確認してください。

## 3.6 Synthesis of results

### 3.6.1 Data extraction

組み入れ基準を満たした研究について、対象者の demographic、サンプルサイズ、Index test の詳細、Reference standard の詳細、閾値、2×2 表 (TP / FP / FN / TN)、QUADAS-3 ドメイン別判定を 2 人のレビュアー ([data extraction reviewers / データ抽出担当者: initials of two reviewers]) が独立して抽出する。データ抽出フォームは、ランダムに選んだ 10 件の研究を用いて事前にチェックしたものを使用する（Appendix 6 参照）。

閾値ごとに複数の 2×2 表が報告されている研究については、すべての閾値の 2×2 表を抽出する。

原著研究の報告基準としては STARD 2015 [@bossuyt2015stard] を参照し、欠落情報がある場合は原著者に問い合わせる。

不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアー: initials]) が裁定者として加わる。

効率向上のため、必要に応じて AI をデータ抽出の補助に用いる [@Gartlehner2025-cm;@Kataoka2025-kq]。AI を実際にどう用いたかは、Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru] に従って報告する。

### 3.6.2 Meta-analysis

結果の統合は Cochrane DTA Handbook v2 [@deeks2023dtahandbook] の推奨に従う。

研究ごとに 2×2 表から感度・特異度およびその 95% CI を算出し、**paired forest plot** (sensitivity と specificity を並べて表示) で提示する。あわせて **SROC 平面** に各研究の感度・特異度プロットし、その分布を記述する。

統合の方針は以下の分岐で決定する。

1. **組み入れ研究数 ≥ 4 かつ、組み入れ研究で同一閾値とみなせる場合**: **bivariate model** [@reitsma2005bivariate] を用い、SROC 平面上に summary point、95% 信頼区間、95% 予測区間を提示する。
2. **組み入れ研究数 ≥ 4 かつ、研究間で閾値がばらつく場合**: **HSROC model** [@rutter2001hsroc] を用い、SROC 曲線を描いて統合結果を提示する。
3. **組み入れ研究数 < 4 の場合**: 統計学的統合は行わず、研究ごとの感度・特異度を表および paired forest plot で記述的に提示する。

すべての解析は **MetaDTA** [@patel2021metadta]（[https://crsu-metadta.le.ac.uk/MetaDTA/](https://crsu-metadta.le.ac.uk/MetaDTA/)、University of Leicester CRSU が提供する無料のブラウザベース Shiny アプリケーション）を用いて行う。MetaDTA は bivariate モデルによる統合と SROC・paired forest plot・summary ROC を生成でき、登録や R/Stata のインストールを必要としない。

> Note: MetaDTA は bivariate モデルを主に実装しています。HSROC を必要とする閾値混在ケースで MetaDTA の機能で不十分な場合は、R `mada` パッケージ (CRAN) または Stata `metandi` / `metadta` の併用を検討してください。その場合、使用ソフトウェアとバージョンを §3.6.2 に追記してください。

有害事象については、原著の定義に従いまとめるが、メタアナリシスは行わない。

## 3.7 Heterogeneity

感度・特異度の研究間ばらつきは、SROC 平面および paired forest plot の目視、ならびに bivariate / HSROC モデルから得られる予測区間の幅により評価する。DTA メタアナリシスでは `I²` 統計量のカットオフは推奨されていない [@deeks2023dtahandbook] ため使用しない。

実質的な異質性が認められる場合、その原因を以下の事前定義したサブグループまたは共変量によるメタ回帰で検討する。

1. [participant subgroup / 対象者サブグループ: 例, 年齢層 (小児 vs 成人)、有病率、症状の有無、セッティング (一次/二次/三次医療)]
2. [index test subgroup / Index test サブグループ: 例, 機器メーカー、モデルバージョン、判定者の専門資格、閾値カテゴリ]
3. [reference standard subgroup / Reference standard サブグループ: 例, 単一 reference standard vs 複合 reference standard、フォロー期間]
4. [methodological subgroup / 方法論的サブグループ: 例, QUADAS-3 で「Low risk」のみの研究 vs 全研究、前向き vs 後ろ向き]

## 3.8 Sensitivity analysis

プライマリアウトカムについて、レビュー過程の判断に対する結果の頑健性を評価するため、以下の感度分析を行う。

1. QUADAS-3 で 1 つ以上のドメインが High risk と判定された研究を除外しての再解析（特に [most influential domain / 最も結果に影響しそうな QUADAS-3 ドメイン番号: 例, Patient selection (D1)]）
2. [other sensitivity analysis / その他の感度分析: 例, 学会抄録のみの研究の除外、データ補完を行った研究の除外、最大規模の研究の除外]

## 3.9 Reporting bias

臨床試験登録 (ClinicalTrials.gov および ICTRP) を検索するとともに、完了しているにも関わらず出版されていない研究を探す。Cochrane DTA Handbook v2 [@deeks2023dtahandbook] に従い、ファンネルプロットおよび Egger 検定などの統計学的な出版バイアス検定は行わない（DTA メタアナリシスでは、これらの検定の妥当性が確立されていないため）。

# 4. Summary of findings table

2 人のレビュアー ([GRADE reviewers / GRADE 評価担当者のイニシャル、一人はメンター: initials of two reviewers, including one mentor if applicable]) が GRADE for DTA [@schunemann2020grade21p1;@schunemann2020grade21p2] に基づきエビデンスの確実性を評価する。不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアーのイニシャル: initials]) が裁定者として加わる。

Summary of Findings テーブルは Cochrane DTA Handbook v2 [@deeks2023dtahandbook] および GRADE 21 part 2 [@schunemann2020grade21p2] に基づき、典型的な有病率を仮定したときの 1,000 人あたりの TP/FP/FN/TN 数とあわせて以下のアウトカムについて作成する: [outcomes for SoF table / SoF テーブルに含めるアウトカム: 例, 感度・特異度、想定有病率における TP/FP/FN/TN per 1,000、推定患者影響]。

# 5. Conflict of Interest

著者らは利益相反を有しない。

# 6. Funding

自己資金。

> Note: 金銭的支援（英文校正費・データベース利用料・解析支援費など）に加え、人手の支援（例: 司書による検索式作成支援、AI ツールの提供、所属機関のサポート等）があれば記載してください。資金提供者やスポンサーがいる場合は、その名称と、本研究のデザイン・データ収集・解析・結果解釈・出版判断のいずれに関与/不関与かも併記してください。いずれもなければ「自己資金。」のままで構いません。

# References

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
> 5. **診断研究フィルター (diagnostic filter) は使用しない**（感度不足のため、Cochrane DTA Handbook v2 [@deeks2023dtahandbook] が非推奨）
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

## Appendix 6: Data extraction form (2×2 table + study characteristics)

下記はデータ抽出フォームの最小構成例である。レビュー設問に応じて列を増減してください。閾値ごとに複数の 2×2 表が報告されている研究は、行を複数に分けて抽出してください。

| Author (Year)                   | Country        | Setting / Design                | Population                  | Sample size | Index test (model/version, threshold) | Reference standard      | Target condition | TP  | FP  | FN  | TN  | Sensitivity (95% CI) | Specificity (95% CI) | QUADAS-3 ratings (D1/D2/D3/D4 RoB & Applicability) |
| ------------------------------- | -------------- | ------------------------------- | --------------------------- | ----------- | ------------------------------------- | ----------------------- | ---------------- | --- | --- | --- | --- | -------------------- | -------------------- | -------------------------------------------------- |
| [author1 year / 例: Smith 2020] | [country / 国] | [setting/design / 例: tertiary, prospective cohort] | [population / 対象者の特徴] | [n]         | [index test / Index test、閾値]       | [reference / Reference] | [target / 状態]  | [n] | [n] | [n] | [n] | [sens (CI)]          | [spec (CI)]          | [ratings]                                          |

抽出項目の優先順位: 必須項目 = author, year, country, design, population, sample size, index test, reference standard, target condition, TP/FP/FN/TN, threshold, QUADAS-3 ratings。任意項目 = [optional items / 任意項目: 例) funding source, conflict of interest, language, time interval between index test and reference standard]。

## Appendix 7: DTA protocol self-check (PRISMA-DTA + QUADAS-3 mapping)

本プロトコルが PRISMA-DTA [@mcinnes2018prismadta;@salameh2020prismadtaee] および QUADAS-3 [@whiting2026quadas3] の主要項目をどこで満たしているかを示す。投稿前のセルフチェックに使用すること。

| 項目分類            | 項目                                                                          | Where in this protocol                |
| ------------------- | ----------------------------------------------------------------------------- | ------------------------------------- |
| PRISMA-DTA / Title  | 報告ガイドライン (PRISMA-DTA) およびスタディタイプ (DTA SR&MA) の明示         | # Title                               |
| PRISMA-DTA / Title  | 過去版の更新かどうか                                                          | # Title の Note + YAML `is-update`    |
| PRISMA-DTA / Abstract | Structured summary (任意)                                                   | 著者欄下の Abstract Note               |
| PRISMA-DTA / Intro  | Rationale (clinical pathway における Index test の位置付け)                   | # 1. Introduction                     |
| PRISMA-DTA / Intro  | Objectives (PIRT に基づくリサーチクエッション)                                | # 2. Research question                |
| PRISMA-DTA / Methods | Protocol and registration (PROSPERO 登録予定)                                | ## 3.1 Protocol                       |
| PRISMA-DTA / Methods | Eligibility criteria (Participants/Index test/Comparator/Reference/Target)   | ## 3.2 Inclusion criteria             |
| PRISMA-DTA / Methods | Information sources                                                          | ## 3.4 Search method                  |
| PRISMA-DTA / Methods | Search strategy (少なくとも 1 DB のドラフト)                                  | Appendix 1–5                          |
| PRISMA-DTA / Methods | Study selection                                                              | ## 3.6.1 Data extraction（screening を含む明示は 3.5.x で補完すること） |
| PRISMA-DTA / Methods | Data collection process                                                      | ## 3.6.1 Data extraction              |
| PRISMA-DTA / Methods | Definitions for data extraction (2×2 表のセル定義、閾値の扱い)               | ## 3.3 Outcomes + Appendix 6          |
| PRISMA-DTA / Methods | Risk of bias of individual studies (QUADAS-3 / QUADAS-C / QUADAS-AI)         | ## 3.5 Risk of bias assessment        |
| PRISMA-DTA / Methods | Diagnostic accuracy measures (sens/spec を primary、LR/PPV/NPV を secondary) | ## 3.3 Outcomes                       |
| PRISMA-DTA / Methods | Synthesis of results (bivariate / HSROC / MetaDTA)                           | ## 3.6.2 Meta-analysis                |
| PRISMA-DTA / Methods | Risk of bias across studies (出版バイアス: 統計検定なし)                      | ## 3.9 Reporting bias                 |
| PRISMA-DTA / Methods | Additional analyses (subgroup, sensitivity)                                  | ## 3.7 Heterogeneity + ## 3.8 Sensitivity analysis |
| QUADAS-3 / Domain 1 | Patient selection (RoB + Applicability)                                      | ## 3.5 + Appendix 6 列                |
| QUADAS-3 / Domain 2 | Index test (RoB + Applicability)                                             | ## 3.5 + ## 3.2.3 + Appendix 6 列     |
| QUADAS-3 / Domain 3 | Reference standard (RoB + Applicability)                                     | ## 3.5 + ## 3.2.5 + Appendix 6 列     |
| QUADAS-3 / Domain 4 | Flow and timing (RoB)                                                        | ## 3.5 + ## 3.2.5 Note + Appendix 6 列|
| GRADE for DTA       | Certainty of evidence (GRADE 21 part 1 & 2)                                  | # 4. Summary of findings table        |
| Reporting           | Funding / Conflict of interest                                               | # 5. Conflict of Interest + # 6. Funding |
