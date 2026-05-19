---
title: "スコーピングレビュー プロトコルテンプレート"
author:
  - SRWS-PSG Mentors
date: 2026-05-19
version: 1.0.0 (draft)
lang: ja
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
> この文書はスコーピングレビュー (scoping review) の プロトコルテンプレートです。`[English label / 日本語ラベル: 記入する内容]` で示した箇所を、自分たちのレビュー内容に置き換えてください。
>
> まず `2. Research question` で PCC (Population / Concept / Context) を決め、次に `3.3 Eligibility criteria` の各サブセクション、`Appendices` の検索式、`3.5 Charting the data` の抽出項目を埋めると進めやすいです。固定文は原則そのまま使えますが、レビュー内容に合わない場合はメンターに確認して修正してください。
>
> Note は作成中の補助説明です。提出版や登録版では、必要に応じて削除してください。
> メンターの所属は `https://docs.google.com/document/d/1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA/edit?usp=sharing` を参照してください。

# Title

Title: [review title / レビュータイトル: 対象者 (Population)、コンセプト (Concept)、文脈 (Context) が分かる短い英語表現]: a scoping review protocol

> Note: 過去版の更新としてプロトコルを公開する場合は、本タイトル末尾に "(update)" を付け、YAML front-matter の `is-update` を `true` に変更してください。

## Registration

Registration: [OSF registration / OSF 登録: 例) osf.io/xxxxx]

> Note: スコーピングレビューのプロトコル登録には Open Science Framework (OSF, [https://osf.io/](https://osf.io/)) を使ってください（PROSPERO はスコーピングレビューを受け付けません）[@peters2022bestpractice]。

## Authors:

> メンターの名前もお忘れなく

Corresponding author: [corresponding author / 連絡著者（メンティー）: full name]

Address: [address / 連絡著者の所属先住所: department, institution, postal address]

E-mail: [e-mail / 連絡著者の連絡先メールアドレス]

Author contributions:

[guarantor initials / 連絡責任者のイニシャル] が本研究の保証人 (guarantor) を務めた。[drafting author initials / 原稿ドラフト担当者のイニシャル] が原稿を執筆した。すべての著者が組み入れ基準 (PCC)、チャーティング項目の策定に貢献した。[search strategy author initials / 検索式担当者のイニシャル] が検索式を作成した。[content expert initials / 臨床・方法論の専門家のイニシャル] が [expertise area / 専門領域: 対象疾患、コンセプト、方法論など] についての専門的助言を提供した。すべての著者が最終原稿を読み、フィードバックを行い、承認した。

\newpage

# 1. Introduction

> Note: 背景の書き方
>
> すべての記述にリファレンスを付けてください。3 パラグラフ構成を推奨します。
>
> 第一パラグラフ — テーマ (Population) について 4–5 文。例:
>
> 1. テーマの臨床的・社会的重要性
> 2. 対象集団の規模と影響
> 3. これまでに知られている標準的アプローチ
> 4. 現状の課題・知識のギャップ
>
> 第二パラグラフ — Concept について 4–5 文。例:
>
> 1. 関心のあるコンセプト (介入、アセスメント、アウトカム、定義など) の説明
> 2. このコンセプトに関する報告のばらつきや用語の不統一の現状
> 3. レビューで明らかにしたい範囲・側面
>
> 第三パラグラフ — なぜスコーピングレビューを行うのか 3–4 文。例:
>
> 1. このテーマに関する既存の systematic review / scoping review の検索結果（無ければ「未発見」、有れば本レビューがどう違うかを 1 文）
> 2. 文献の幅 (scope) や利用可能なエビデンスの広がりを把握することが必要な理由
> 3. そのため本研究ではこのテーマにおけるスコーピングレビューを行う
>
> 背景を対話で指導してくれる GPTs: [https://chatgpt.com/g/g-YF7pcAKdG-background-editor](https://chatgpt.com/g/g-YF7pcAKdG-background-editor)
> すべての記述に必要に応じてリファレンスを付ける

# 2. Research question

PCC (Population, Concept, Context) フレームワークを用いて、本スコーピングレビューが答えようとする疑問を以下のように記述する。

- P (Population): [participants / 対象者: 疾患、状態、年齢層、診療場面など]
- C (Concept): [concept / コンセプト: 介入・アセスメント・現象・経験など、レビューで網羅したい中核概念。用語 (terminology) で定義するか、概念 (concept) で定義するかを明確に]
- C (Context): [context / 文脈: セッティング、地域、期間、文化的背景など、関心を限定する文脈]

レビュークエスチョン:

1. [research question 1 / リサーチクエスチョン 1: PCC を用いた具体的な疑問文]
2. [research question 2 / リサーチクエスチョン 2: 必要に応じて複数列挙]
3. [research question 3 / リサーチクエスチョン 3]

## Keywords

アルファベット順に 5 つまで、セミコロンとスペースで区切って記載する（タイトルやアブストラクトに現れる語と異なることが理想的）。

[keywords / キーワード: 例) concept; intervention; population; scoping review; setting]

# 3. Method

## 3.1 Protocol

本レビューは Peters らが示したスコーピングレビュープロトコルの best practice ガイダンス [@peters2022bestpractice] 、Joanna Briggs Institute (JBI) の scoping review 実施ガイダンス [@peters2020jbi;@peters2020jbimanual] 、PRISMA Extension for Scoping Reviews (PRISMA-ScR) [@tricco2018prismascr] を参考にプロトコルの準備を行った。本プロトコルは SRWS-PSG が管理するスコーピングレビュー プロトコルテンプレート（リポジトリ: [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates)、Zenodo concept DOI: 10.5281/zenodo.&lt;TBD&gt;）を使用した。本プロトコルは OSF.io ([https://osf.io/](https://osf.io/)) に公開する予定である。

JBI の 5 ステージフレームワーク (Stage 1: リサーチクエスチョンの特定 / Stage 2: 関連する研究の特定 / Stage 3: 研究の選定 / Stage 4: データのチャーティング / Stage 5: 結果の照合・要約・報告) を採用する [@peters2020jbi;@arksey2005scoping;@levac2010scoping]。

## 3.2 Stage 1: Identifying the research question

Stage 1 は §2 で記述した PCC に基づくリサーチクエスチョンの特定を指す。詳細は §2 を参照のこと。

## 3.3 Stage 2: Identifying relevant studies (eligibility criteria)

PCC フレームワーク [@peters2020jbi] に基づき、組み入れ基準を以下のように定義する。

### 3.3.1 Participants

[participants overview / 対象者の概要: 疾患・状態、年齢層、診療場面などを文章で記入]

組み入れ基準: [participant inclusion criteria / 対象者の組入基準: 対象疾患、診断基準、年齢、性別、重症度、セッティングなど]

除外基準: [participant exclusion criteria / 対象者の除外基準: 除外する併存疾患、既治療、特定集団など]

### 3.3.2 Concept

[concept overview / コンセプトの概要: レビューの中核概念を文章で説明]

![スコーピングレビューにおけるコンセプトの定義: 用語 (Terminology, 例: 「木」) で定義するのか、概念 (Concept, 例: 林・森・林業) で定義するのかを Stage 2 設計時に明示する。](media/scoping_concept_focus.png){#fig:concept-focus width=100%}

> Note: 上図のように、Concept を狭く特定の **用語 (terminology)** で定義するのか、関連する語や派生語を含む広い **概念 (concept)** として定義するのかを明示してください（これが検索式・組み入れ判断の幅を決めます）。

組み入れ基準: [concept inclusion criteria / コンセプトの組入基準: 採用する用語の範囲、関連概念の扱いなど]

除外基準: [concept exclusion criteria / コンセプトの除外基準: 採用しない用語、関連しないと判断する概念など]

### 3.3.3 Context

[context overview / 文脈の概要: セッティング、地域、期間、文化的背景など]

組み入れ基準: [context inclusion criteria / 文脈の組入基準: 例) 急性期病院、在宅、高所得国、特定の医療制度下など]

除外基準: [context exclusion criteria / 文脈の除外基準: 例) 動物実験、特定の文化的設定の除外など]

### 3.3.4 Types of sources

[study designs / 組み入れる研究デザイン: 例) 量的研究 (RCT・非RCT・前後比較・コホート・症例対照・横断・症例シリーズ・症例報告)、質的研究、システマティックレビュー、灰色文献など。研究設問に必要なものを列挙]

> Note: 学会抄録は情報量が少ないため除外することも多いです。組み入れる/除外する場合は理由をメンターに相談のうえ明示してください。

### 3.3.5 Search method

> Note: 初回プロトコル作成時は、まず MEDLINE のみを完成させ、CENTRAL・Embase・各レジストリの検索式は後回しにして構いません（フォーム入力後、メンターの確認を経てから他データベース・レジストリの検索式を整えます）。

検索期間: [search date range / 検索対象期間: 例) inception to YYYY-MM-DD]

#### 3.3.5.1 Electronic search

以下のデータベースを検索する。

1. MEDLINE (PubMed)
2. the Cochrane Central Register of Controlled Trials (Cochrane Library)
3. Embase (Dialog)

検索式は Appendix 1、2、3 を参照のこと。

#### 3.3.5.2 Other resources

進行中または未出版の研究について、以下のレジストリも検索する。

1. the World Health Organization International Clinical Trials Registry Platform (ICTRP)
2. ClinicalTrials.gov

検索式は Appendix 4 および 5 を参照のこと。

組み入れ研究のリファレンスリスト、ならびに組み入れ研究を引用している論文のリファレンスリストもチェックする。原著者には、未出版データや追加データの提供を依頼する。灰色文献 (政府報告書、学位論文、団体の白書など) を含める場合は、対象とする情報源を以下に明示する: [grey literature sources / 灰色文献の情報源: 例) WHO database, OpenGrey, 学位論文DB など]。

### 3.3.6 Report characteristics

組み入れる文献の特性を以下のように限定する。

- 言語: [language / 言語: 例) 英語と日本語、または言語の制限なし]
- 対象年: [years considered / 検索対象年: 例) 2000 年以降、または年の制限なし]
- 出版状態: [publication status / 出版状態: 例) 査読付き論文・プレプリント・学会抄録の扱いを明示]

## 3.4 Stage 3: Study selection

2 人の独立したレビュアー ([screening reviewers / スクリーニング担当者のイニシャル: initials of two reviewers]) が、Tiab Review plugin [@Kataoka2026-tb] を用いてタイトルおよび抄録のスクリーニングを行い、続いてフルテキストに基づき適格性を評価する。関連するデータが欠けている (例: 抄録のみで判定不能) 場合は原著者に問い合わせる。2 人のレビュアー間の不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアーのイニシャル: initials]) が裁定者として加わる。検索結果および研究の組み入れプロセスは、最終的なスコーピングレビューにおいて PRISMA-ScR フロー図 [@tricco2018prismascr] で報告する。

> Note: 3 人以上で screening を行う場合は "two of three independent reviewers..." と記載してください。

## 3.5 Stage 4: Charting the data

2 人のレビュアー ([data extraction reviewers / データ抽出担当者のイニシャル: initials of two reviewers]) が、標準化されたデータチャーティングフォーム (Appendix 6 参照) を用いて、組み入れ研究のデータを独立して抽出する。フォームの試行版を、ランダムに選択した 10 件の研究に対して事前にパイロットテストし、必要に応じてフォームを改訂する。

> Note: スコーピングレビューでは個別研究のアウトカム値を抽出して統合することは通常行いません [@peters2022bestpractice]。代わりに、レビュー設問に答えるために必要な「データ項目 (data items)」を Appendix 6 のチャーティングフォームに明示し、その優先順位 (必須項目 / 任意項目) を決めておきます。

不一致は議論により解決し、解決しない場合は第三のレビュアー ([third reviewer / 第三レビュアーのイニシャル: initials]) が裁定者として加わる。必要に応じて原著者に追加情報の提供を依頼する。

効率向上のため、必要に応じて AI をデータ抽出の補助に用いる [@Gartlehner2025-cm;@Kataoka2025-kq]。AI を実際にどう用いたかは、Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025 [@Flemyng2025-ru] に従って報告する。

> Note (Risk of bias, optional): スコーピングレビューでは通常、個別研究のバイアスリスク評価 (critical appraisal) は実施しません [@peters2022bestpractice]。レビュー設問上必要と判断する場合は、評価する単位 (個別研究レベル / アウトカムレベル / 両方)、使用するツール、および評価結果を結果の統合でどう扱うかを以下に記載してください: [risk of bias plan / バイアスリスク評価計画: ツール名、評価レベル、結果の扱い方]。

## 3.6 Stage 5: Collating, summarizing, and reporting the results

抽出されたデータは質的に統合し、レビュー設問に直接答える形で提示する。提示方法は表・図・evidence and gap map など、データの性質に応じて選択する [@south2023visualisation;@fredlund2024egm]。本プロトコルでは以下を提示する予定である。

1. PRISMA-ScR フロー図 (組み入れプロセス)
2. 組み入れ研究の特性表 (Author / Year / Country / Population / Concept / Context / Methodology / Key findings の列、例 Appendix 6)
3. [planned visualisations / 提示予定の図表: 例) evidence gap map, bubble plot, matrix map, timeline, narrative summary など — どの可視化が当該テーマに適切かを `cesm.12096` Table 3 [@fredlund2024egm] や `s13643-023-02309-y` の実例 [@south2023visualisation] を参考に選ぶ]

> Note (Meta-bias, optional): スコーピングレビューでは通常、出版バイアス等のメタバイアス評価は実施しません [@peters2022bestpractice]。実施する場合はその方法を以下に記載してください: [meta-bias plan / メタバイアス評価計画]。

> Note (Confidence in cumulative evidence, optional): スコーピングレビュー用に確立された GRADE はまだ存在しません [@peters2022bestpractice]。エビデンスの確実性評価を行う場合はその方法と根拠を以下に記載してください: [confidence assessment plan / 確実性評価計画]。

# 4. Conflict of Interest

著者らは利益相反を有しない。

# 5. Funding

自己資金。

> Note: 金銭的支援（英文校正費・データベース利用料・解析支援費など）に加え、人手の支援（例: 司書による検索式作成支援、AI ツールの提供、所属機関のサポート等）があれば記載してください。資金提供者やスポンサーがいる場合は、その名称と、本研究のデザイン・データ収集・解析・結果解釈・出版判断のいずれに関与/不関与かも併記してください [@peters2022bestpractice]。いずれもなければ「自己資金。」のままで構いません。

# References

::: {#refs}
:::

&nbsp;

\newpage

# Appendices

## Appendix 1: MEDLINE (PubMed) search strategy

> 03_06、03_07 の検索式の課題については、フォームに入力し、その旨を URL とともに Slack でメンターに伝えてください。

> Note: 検索式作成のステップ
>
> 1. どういう検索ブロック（例: population、concept、context、study design など）に分けるかを決める
> 2. 各ブロックの統制語（MeSH 等）として何を使うかを考える
> 3. 各ブロックを自由語と統制語で展開する
> 4. ブロックを AND で組み合わせる
>
> 下書き支援ツール（要 Google アカウントの無料登録）。組み入れ基準を入力すると検索式の下書きを生成してくれます: [https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&amp;usp=sharing](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221xiXk7Zidc9bEyN__EPPIN3AbgpVRWo5A%22%5D,%22action%22:%22open%22,%22userId%22:%22107122855205791560725%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

[MEDLINE search strategy / MEDLINE の検索式: population・concept (・context) の検索語、MeSH、組み合わせ式を記入。スコーピングレビューでは RCT filter を付けない]

## Appendix 2: CENTRAL (Cochrane Library) search strategy

[CENTRAL search strategy / CENTRAL の検索式: population・concept の検索語、組み合わせ式を記入]

## Appendix 3: Embase (Dialog) search strategy

> Note: 初回プロトコル作成時はこの Appendix は空欄のままで構いません。MEDLINE の検索式が確定してから、対応する Emtree と自由語に置き換えて作成します。

[Embase search strategy / Embase の検索式: population・concept の検索語、Emtree、組み合わせ式を記入]

## Appendix 4: ICTRP search strategy

[ICTRP search strategy / ICTRP の検索式: population・concept、類義語、検索日を記入]

## Appendix 5: ClinicalTrials.gov search strategy

- Condition or disease: [condition or disease / 対象集団・状態: ClinicalTrials.gov に入力する集団名・状態名や類義語]
- Intervention / Other terms: [concept terms / コンセプト関連語: ClinicalTrials.gov に入力するコンセプト関連の介入名や類義語]

## Appendix 6: Data charting form (basic draft extraction tool)

下記は Peters らが示した basic draft extraction tool [@peters2022bestpractice] を出発点とした例である。レビュー設問に応じて列を増減してください。

| Author (Year)                   | Country        | Population                  | Concept                        | Context                        | Methodology / Study design | Key findings relevant to the review question |
| ------------------------------- | -------------- | --------------------------- | ------------------------------ | ------------------------------ | -------------------------- | -------------------------------------------- |
| [author1 year / 例: Smith 2020] | [country / 国] | [population / 対象者の特徴] | [concept / 該当する用語・概念] | [context / セッティング・期間] | [methodology / デザイン]   | [key findings / 主要な知見]                  |

抽出項目の優先順位: 必須項目 = [required items / 必須項目: 例) author, year, country, population, concept, context, study design]; 任意項目 = [optional items / 任意項目: 例) sample size, funding source, language]。

## Appendix 7: Scoping review protocol checklist (Peters 2022 Table 1)

本プロトコルが Peters らの best practice チェックリスト [@peters2022bestpractice] の各項目をどこで満たしているかを示す。投稿前のセルフチェックに使用すること。

| Item No | Section and topic                                                            | Where in this protocol                              |
| ------- | ---------------------------------------------------------------------------- | --------------------------------------------------- |
| 1a      | Title — Identification (scoping review protocol である旨)                   | # Title                                             |
| 1b      | Title — Update (過去版の更新かどうか)                                       | # Title の Note + YAML `is-update`                |
| 2       | Title — Registration (登録先と登録番号)                                     | ## Registration                                     |
| 3a      | Authors — Contact (氏名・所属・E-mail・住所)                                | ## Authors（Corresponding author, Address, E-mail） |
| 3b      | Authors — Contributions (guarantor を含む)                                  | ## Authors（Author contributions）                  |
| 4       | Amendments (改訂方針と履歴)                                                  | ## Amendments                                       |
| 5a      | Support — Sources of support                                                | # 5. Funding                                        |
| 5b      | Support — Funder/Sponsor name                                               | # 5. Funding（Note 内で記載）                       |
| 5c      | Support — Role of funder/sponsor                                            | # 5. Funding（Note 内で記載）                       |
| 6       | Rationale (レビューの根拠、scoping を選ぶ理由を含む)                         | # 1. Introduction                                   |
| 7       | Objectives (PCC を用いたレビュークエスチョン)                                | # 2. Research question                              |
| 8       | Eligibility criteria (PCC + 研究デザイン + 報告特性)                         | ## 3.3 Stage 2（3.3.1–3.3.6）                      |
| 9       | Information sources (DB・レジストリ・灰色文献・検索期間)                     | ## 3.3.5 Search method                              |
| 10      | Search strategy (少なくとも 1 DB のドラフト)                                 | Appendix 1–5                                       |
| 11a     | Study records — Data management                                             | ## 3.4 Stage 3（Tiab Review plugin での記録管理）   |
| 11b     | Study records — Selection process                                           | ## 3.4 Stage 3                                      |
| 11c     | Study records — Data collection process                                     | ## 3.5 Stage 4                                      |
| 12      | Data items (チャーティング項目)                                              | ## 3.5 Stage 4 + Appendix 6                         |
| 13      | Outcomes and prioritization (スコーピングではデータ項目の優先順位として記述) | ## 3.5 Stage 4 の Note + Appendix 6                 |
| 14      | Risk of bias in individual studies (optional)                                | ## 3.5 Stage 4 末尾の Note                          |
| 15a–d  | Data synthesis / presentation (図表・evidence gap map など)                  | ## 3.6 Stage 5                                      |
| 16      | Meta-bias(es) (optional)                                                     | ## 3.6 Stage 5 末尾の Note                          |
| 17      | Confidence in cumulative evidence (optional)                                 | ## 3.6 Stage 5 末尾の Note                          |
