---
title: "診断精度レビュー プロトコルテンプレート"
author:
  - SRWS-PSG Mentors
date: 2026-05-20
version: 2.0.0 (draft)
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

[guarantor initials / 連絡責任者のイニシャル] が本研究の保証人 (guarantor) を務めた。[drafting author initials / 原稿ドラフト担当者のイニシャル] が原稿を執筆した。[search strategy author initials / 検索式担当者のイニシャル] が検索式を作成した。[statistics author initials / 統計担当者のイニシャル] が診断精度メタアナリシス（bivariate / HSROC モデル）について統計的助言を提供した。[content expert initials / 臨床・方法論の専門家のイニシャル] が [expertise area / 専門領域: 対象疾患、Index test、Reference standard、方法論など] についての専門的助言を提供した。すべての著者が最終原稿を読み、フィードバックを行い、承認した。


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

本レビューでは、SRWS-PSG が管理する診断精度レビュー プロトコルテンプレート（リポジトリ: [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates)、Zenodo concept DOI: 10.5281/zenodo.20586625）を使用した。本プロトコルの作成にあたっては Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy v2.0 [@deeks2023dtahandbook] 、PRISMA-DTA 声明 [@mcinnes2018prismadta] を参照した。本プロトコルは OSF ([https://osf.io/](https://osf.io/)) に登録する予定である。

## 3.2 Inclusion criteria of the studies for the review

### 3.2.1 Type of studies

Target conditionに対するIndex testの診断精度を検討したすべてのCohort研究、RCTの二次解析結果、Case control研究 を組み入れる。

出版の状態については問わない（出版済のもの、未出版のもの、学会抄録やletterも含む）。

言語および、研究の実施された国についても問わない。

Case seriesとcase reportは除外する。

Reference standardを元に、Index testの真陽性、偽陽性、真陰性、偽陰性の数を抽出できるデータを提示している研究は組み入れる。

観察期間での除外はしない。

> Note (比較精度レビューの場合): 同一被験者に複数の Index test を適用した paired comparative accuracy study、または対象者を Index test 群にランダム化した randomized comparative accuracy study を組み入れる場合は、§3.6 のバイアスリスク評価で QUADAS-C [@yang2021quadasc] を併用してください。

### 3.2.2 Participants

[participants overview / 対象者の概要: 疾患・状態の疑い、年齢層、診療場面、Index test を適用する臨床的タイミングなどを文章で記入]

- 組み入れ基準（すべてを満たす）: [participant inclusion criteria / 対象者の組入基準: 対象疾患疑い、年齢、性別、セッティング (一次・二次・三次医療、検診など)、症状の有無]
- 除外基準（いずれかを満たす）: [participant exclusion criteria / 対象者の除外基準: 除外する併存疾患、既治療、特定集団など]

QUADAS-3 phase 2 (ideal test accuracy trial / D1 signaling questions) が要求する「理想的な対象者像」を、本レビューについてここで事前規定しておきます。これらが §3.6 の D1 評価の判定基準になります。

- 想定使用集団 (intended-use population): [intended-use population / 想定使用集団: 例) [症状]を主訴に一次医療を受診する成人。Index test を実際に適用する対象集団の年齢・性別・症状の有無・併存疾患の範囲を明記]
- 臨床経路における Index test の役割 (role of the index test within the clinical pathway): [role of index test / Index test の役割: triage / replacement / add-on / parallel testing のいずれか。前段に置かれる検査 (例) 病歴・身体所見のみ／別検査の後 など) も明示]

### 3.2.3 Index test

[index test details / Index test の詳細: 検査名、機器・試薬・モデル (AI/ML の場合はバージョン)、サンプル種別 (検体・撮像対象など)、実施手順]

- 判定者・実施者: [operator and reader / 判定者・実施者: 検査を実施する者および結果を判定する者の資格 (例: 認定放射線科医、検査技師、臨床医、AI モデル単独)、訓練・経験要件、想定使用集団 (§3.2.2) と整合する熟達度のレベル]

QUADAS-3 phase 2 (ideal test accuracy trial / D2 signaling questions 2.1–2.4) が要求する「理想的な Index test 実施・判定条件」を、本レビューについてここで事前規定しておきます。

- 推奨される実施手順 (recommended instructions / standardized protocol): [recommended instructions / 標準手順: メーカー添付文書、ガイドライン、SOP など、本レビューが「適切な実施」とみなす基準。これから外れた研究が signaling question 2.1 で "N" となる]
- 判定時に利用できる「通常臨床の情報」 (clinical information available in routine practice): [available clinical information / 通常臨床で利用できる情報: 例) 患者年齢・性別、主訴、症状経過、バイタル、過去の検査結果のうち今回の Index test の前段階に既に得られているもの。signaling question 2.3 の判定基準]
- 判定時に利用しては**ならない**情報: [prohibited information / 利用不可情報: Reference standard 結果、Target condition の最終診断、本来 Index test より下流に位置する別の検査結果など。signaling question 2.2 の判定基準]
- 閾値 (threshold) の事前指定: [prespecified threshold / 事前指定された閾値: 例) メーカー推奨値である X、ガイドライン推奨値である Y。研究ごとに事後選択された最適閾値は signaling question 2.4 で "N"]

> Note: 閾値 (cutoff) を1つに固定するか、複数の閾値を許容するかは、解析方針（§3.7）と密接に関わるため、ここで明示してください。閾値を「研究ごとに事後選択された最適閾値」とする場合、HSROC モデルでの解析が前提となります。
>
> Note: 「通常の臨床で利用できる情報」を Index test 判定時に故意に隠した (blind した) 研究は、現実の運用と乖離するため signaling question 2.3 で "N" となり得ます。逆に、Index test 判定時に Reference standard 結果まで開示している研究は signaling question 2.2 で "N" となります。両者を取り違えないよう、ここで「利用できる情報」と「利用してはならない情報」を別行に分けて明記してください。

### 3.2.4 Comparator (optional)

[comparator details / 比較する Index test の詳細: ある場合のみ。Index test と同一の被験者・同一の Reference standard で評価された別の検査名、閾値、実施者など。なければ「該当なし」と記入]

### 3.2.5 Reference standard

QUADAS-3 phase 2 (ideal test accuracy trial / D3 signaling questions 3.1–3.8) が要求する「理想的な Reference standard 条件」を、本レビューについてここで事前規定しておきます。

- 採用可能な Reference standard の階層 (hierarchy of acceptable reference standards): [reference standard hierarchy / Reference standard の階層: 1) 最も望ましいもの (例) 組織診)、2) 次善 (例) 画像 + 臨床経過 6 か月以上の追跡)、3) 許容下限 (例) 退院時の臨床診断)。各層について「これより下は組み入れない」境界も明記]
- 同一 Reference standard の全員適用 (single reference standard policy): [single reference standard policy / 単一 reference standard 方針: 全被験者に同じ Reference standard を適用するか、被験者によって異なる Reference standard を許容するか。許容する場合の条件 (例) 倫理的・侵襲性の理由で、Index test 陰性者には follow-up を Reference standard として許容) を明記。signaling question 3.3 の判定基準]
- Reference standard の閾値 (reference standard threshold): [reference threshold / Reference standard 閾値: 例) 組織診における Marsh score ≥ 3a、培養 CFU/mL 閾値、画像所見の定義など。事後選択された閾値は signaling question 3.7 で "N"]
- Index test からの独立性 (independence from index test): [independence from index test / Index test との独立性: Reference standard は Index test の結果に**盲検化**された状態で判定されること (signaling question 3.6)。また Index test 自体が composite reference standard の構成要素になっていないこと (signaling question 3.4 = incorporation bias)]
- 適切な実施間隔 (appropriate time interval): [appropriate interval / 適切な実施間隔: 例) 同日内、1 週間以内、4 週間以内など、臨床的に状態が変化しないと見なせる上限。Reference standard が long-term follow-up の場合は最低追跡期間 (例) ≥ 6 か月) を明記。signaling question 3.8 の判定基準]
- 不確定 (indeterminate) Reference standard 結果の扱い: [indeterminate reference / 判定不能 Reference standard の扱い: 例) Reference standard が判定不能となった被験者を分析から除外するか、複合判定で対応するか。臨床の流れに即した判断方針を記載]

> Note: Index test と Reference standard の間隔が長すぎると disease progression bias が生じ得ます。臨床的に妥当な上限 (例) 同日・1 週間以内・4 週間以内) を明示してください。
>
> Note: Reference standard が imperfect (no gold standard) であったり、被験者によって異なる Reference standard が適用される場合は、QUADAS-3 の "Target condition" / "Analysis" ドメインで partial verification bias / differential verification bias として評価されます。事前規定した階層があれば、各研究をどの層の Reference standard で判定されたかで分類できます。

### 3.2.6 Target condition

[target condition / Target condition: 診断対象の疾患・状態の臨床的定義、病期・重症度の範囲、除外する亜型など]

QUADAS-3 phase 2 における Target condition と Reference standard の整合:

- Target condition の sub-category (該当する場合): [target subcategory / Target condition のサブカテゴリ: 例) 「悪性腫瘍」一般ではなく「ステージ I-II の限局性大腸癌」など、本レビューの臨床問題に対応する範囲を限定。研究側がより広い (または狭い) sub-category を評価している場合は applicability を High concern とする旨を記載]
- Reference standard の閾値による定義差の許容範囲: [acceptable threshold variability / Reference standard 閾値差の許容: 例) 培養 CFU/mL 閾値が研究間で 10² 違うのは許容するが、10⁴ 違うものは別 condition とみなす など、§3.2.5 と整合する形で]

## 3.3 Outcomes

### 3.3.1 Primary outcomes

Primary outcome は、Reference standard を真値とした Index test の 感度 (sensitivity) と特異度 (specificity) および 95% 信頼区間 (CI) である。研究ごとに Index test の真陽性 (TP)、偽陽性 (FP)、偽陰性 (FN)、真陰性 (TN) の数を抽出し、これらから感度・特異度を算出する。

解析単位 (unit of analysis) は [unit of analysis / 解析単位: 例) 個々の被験者 (per participant)、検体 (per sample)、病変 (per lesion)、撮像 (per scan)、検査部位 (per organ) のいずれか。臨床判断・臨床管理の単位と整合させる]。

各研究の 95% CI は、原著で報告された CI を採用するか、または 2×2 表から Wilson 法または Jeffreys ベイズ信用区間 [@whiting2026quadas3] で再計算する（極端な値 0/N、N/N に対しても挙動が安定するため）。

QUADAS-3 Phase 4 [@whiting2026quadas3] に従い、各組み入れ研究から Phase 5 (risk of bias 評価) の対象とする accuracy estimate を特定する。1 つの研究から、異なる閾値・サブグループ・reference standard・target condition の定義・unit of analysis などにより、複数の paired sensitivity/specificity (= 複数の 2×2 表) が報告されうるため、§2 の synthesis question に紐づくペアのみを Phase 5 の評価対象とする。本レビューでの選択ルールは以下のとおり:

- 閾値が複数報告されている場合の取扱い: [phase 4 threshold rule / Phase 4 閾値ルール: 例) §3.2.3 で事前指定した閾値の 2×2 表のみを Phase 5 評価対象とする / 報告された全閾値を別 estimate として Phase 5 評価対象とする / 事前指定閾値に最も近い 1 つを Phase 5 評価対象とする のいずれか]
- サブグループ別推定値の取扱い: [phase 4 subgroup rule / Phase 4 サブグループルール: 例) §3.7.x で事前指定したサブグループ解析に該当する paired sens/spec のみを別 estimate として Phase 5 評価対象とする。事前指定外のサブグループ別推定値は Phase 5 評価対象にしない]
- 解析単位 (unit of analysis): §3.3.1 で指定した単位に該当する 2×2 表のみを Phase 5 評価対象とする。

> Note: 1 つの研究から複数の候補ペアが上記ルールに同等に整合する場合、どれを Phase 5 評価対象とするかは case-by-case の判断となる。判断要素としては precision (95% CI 幅)、reference standard の risk of bias、target condition 定義の臨床的整合性、unit of analysis の妥当性などがある（QUADAS-3 [@whiting2026quadas3] は順位付けを規定していない）。複数候補がある場合はメンターと協議のうえ決定し、選択した推定値と判断根拠を記録する。

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
> Note: DTA レビューでは、MEDLINE/EMBASE 向けに公開されている 診断研究フィルター (diagnostic filter) は感度が不十分とされており、Cochrane DTA Handbook v2 [@deeks2023dtahandbook] は使用しないことを推奨しています。したがって本レビューでは検索フィルターを使わず、Participants（または Target condition）と Index test のブロックを AND で組み合わせる検索式とします。

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

組み入れ研究のリファレンスリスト、国際的な診療ガイドライン ([guideline names or organizations / 確認する診療ガイドライン名・作成組織])、ならびに組み入れ研究を引用している論文のリファレンスリストもチェックする。必要に応じて原著者には、未出版データや追加データ の提供を依頼する。

## 3.5 Selection of studies

2 人の独立したレビュアー ([screening reviewers / スクリーニング担当者のイニシャル: initials of two reviewers]) が、Tiab Review plugin [@Kataoka2026-tb] を用いてタイトルおよび抄録のスクリーニングを行い、続いてフルテキストに基づき適格性を評価する。関連するデータが欠けている場合は原著者に問い合わせる。2 人のレビュアー間の不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアーのイニシャル: initials]) が裁定者として加わる。

> note: 3 人以上で screening を行う場合は "two of three independent reviewers..." と記載してください。

## 3.6 Risk of bias assessment

2 人のレビュアー ([risk of bias reviewers / RoB 評価担当者: initials of two reviewers]) が QUADAS-3 [@whiting2026quadas3] を用いて独立にバイアスリスクおよび適用可能性 (applicability) を評価する。不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアー: initials]) が裁定者として加わる。

QUADAS-3 は 6 フェーズで構成される。本プロトコルでは:

- Phase 1 (synthesis questions) を §2 で、
- Phase 2 (ideal test accuracy trial) の構成要素を §3.2.2 (Participants)、§3.2.3 (Index test)、§3.2.5 (Reference standard)、§3.2.6 (Target condition)、§3.3.1 (unit of analysis) に分散して事前定義済み

としている。レビュアーは Phase 3 (組み入れ一次研究のflow diagram の確認)、Phase 4 (評価対象とする accuracy estimate の特定)、Phase 5 (各 signaling question の判定とドメイン判定)、Phase 6 (推定値ごとの overall judgment) を担当する。

ドメイン判定 (Low / High / Insufficient information) は、§3.2 で事前定義した "ideal" な条件からの逸脱が臨床的に意味のある程度に sensitivity または specificity を過大・過小評価しうる場合に High と判定する。signaling question の "PN" / "N" 回答が 1 つあっても、自動的にドメイン High となるわけではない（QUADAS-3 phase 5 指針 [@whiting2026quadas3]）。


> Note (比較精度レビュー): 同一被験者に複数の Index test を適用した、もしくは Index test 群にランダム化された比較精度デザインを組み入れる場合は、QUADAS-3 に加え QUADAS-C [@yang2021quadasc] を用いて pair 単位での比較バイアスを評価してください。
>
> Note (AI ベース Index test): Index test が AI/ML モデルの場合、QUADAS-AI（開発中、Sounderajah 2021 [@sounderajah2021quadasaiposition]、Guni 2024 [@guni2024quadasai]）、STARD-AI [@sounderajah2025stardai] の枠組みを参照しつつsignaling questionの更新を検討してください。

## 3.7 Synthesis of results

### 3.7.1 Data extraction

組み入れ基準を満たした研究について、対象者の demographic、サンプルサイズ、Index test の詳細、Reference standard の詳細、閾値、2×2 表 (TP / FP / FN / TN)、QUADAS-3 ドメイン別判定を 2 人のレビュアー ([data extraction reviewers / データ抽出担当者: initials of two reviewers]) が独立して抽出する。
不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアー: initials]) が裁定者として加わる。
効率向上のため、必要に応じて AI をデータ抽出の補助に用いる [@Gartlehner2025-cm;@Kataoka2025-kq]。AI を実際にどう用いたかは、Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru] に従って報告する。

### 3.7.2 Meta-analysis

結果の統合は Cochrane DTA Handbook v2 [@deeks2023dtahandbook] の推奨に従う。

研究ごとに 2×2 表から感度・特異度およびその 95% CI を算出し、paired forest plot (sensitivity と specificity を並べて表示) で提示する。あわせて SROC 平面 に各研究の感度・特異度プロットし、その分布を記述する。
一次研究の結果の統合には階層モデルを用いる。
組み入れ研究で同じ閾値が採用されているとみなせる場合、bivariate modelを用いて、ROC平面上にsummary pointと95%信頼区間、95%予測区間を提示する。
組み入れ研究で同じ閾値が採用されていないとみなされた場合、HSROC modelを用いてROC平面上に統合結果を提示する。
すべての解析は MetaDTA [@patel2021metadta]（[https://crsu-metadta.le.ac.uk/MetaDTA/](https://crsu-metadta.le.ac.uk/MetaDTA/)）を用いて行う。

> Note: MetaDTA は bivariate モデルを主に実装しています。HSROC を必要とする閾値混在ケースで MetaDTA の機能で不十分な場合は、R `mada` パッケージ (CRAN) または Stata `metandi` / `metadta` の併用を検討してください。その場合、使用ソフトウェアとバージョンを §3.7.2 に追記してください。

有害事象については、原著の定義に従いまとめるが、メタアナリシスは行わない。

## 3.8 Heterogeneity

感度・特異度の研究間ばらつきは、SROC 平面および paired forest plot の目視、ならびに bivariate / HSROC モデルから得られる予測区間の幅により評価する。DTA メタアナリシスでは `I²` 統計量のカットオフは推奨されていない [@deeks2023dtahandbook] ため使用しない。

実質的な異質性が認められる場合、その原因を以下の事前定義したサブグループまたは共変量によるメタ回帰で検討する。

1. [participant subgroup / 対象者サブグループ: 例, 年齢層 (小児 vs 成人)、有病率、症状の有無、セッティング (一次/二次/三次医療)]
2. [index test subgroup / Index test サブグループ: 例, 機器メーカー、モデルバージョン、判定者の専門資格、閾値カテゴリ]
3. [reference standard subgroup / Reference standard サブグループ: 例, 単一 reference standard vs 複合 reference standard、フォロー期間]
4. [methodological subgroup / 方法論的サブグループ: 例, QUADAS-3 で「Low risk」のみの研究 vs 全研究、前向き vs 後ろ向き]

## 3.9 Sensitivity analysis

プライマリアウトカムについて、レビュー過程の判断に対する結果の頑健性を評価するため、以下の感度分析を行う。

1. QUADAS-3 で 1 つ以上のドメインが High risk と判定された研究を除外しての再解析（特に [most influential domain / 最も結果に影響しそうな QUADAS-3 ドメイン番号: 例, Patient selection (D1)]）
2. [other sensitivity analysis / その他の感度分析: 例, 学会抄録のみの研究の除外、データ補完を行った研究の除外、最大規模の研究の除外]

## 3.10 Reporting bias

臨床試験登録 (ClinicalTrials.gov および ICTRP) を検索するとともに、完了しているにも関わらず出版されていない研究を探す。Cochrane DTA Handbook v2 [@deeks2023dtahandbook] に従い、ファンネルプロットおよび Egger 検定などの統計学的な出版バイアス検定は行わない。

# 4. Summary of findings table

Summary of Findings テーブルは Cochrane DTA Handbook v2 [@deeks2023dtahandbook] に基づき、以下のアウトカムについて作成する: [outcomes for SoF table / SoF テーブルに含めるアウトカム: 例, 感度・特異度、想定有病率における TP/FP/FN/TN per 1,000、推定患者影響]。

# 5. Conflict of Interest

著者らは利益相反を有しない。

# 6. Funding

自己資金。

> Note: 金銭的支援（英文校正費・データベース利用料・解析支援費など）に加え、人手の支援（例: 司書による検索式作成支援、AI ツールの提供、所属機関のサポート等）があれば記載してください。資金提供者やスポンサーがいる場合は、その名称と、本研究のデザイン・データ収集・解析・結果解釈・出版判断のいずれに関与/不関与かも併記してください。いずれもなければ「自己資金。」のままで構いません。

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