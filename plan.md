# Protocol template update and Google Scholar indexing plan

作成日: 2026-05-16
目的: 既存のprotocols.io上のプロトコルテンプレートをアップデートし、その更新を契機に、Google Scholarで文献・引用として拾われやすい形に整える。

## 1. 基本方針

今回の目的は、査読論文として出版することではなく、以下を満たすこと。

- 実際にチームが使うテンプレートを最新版として公開する
- SR執筆時に引用しやすい形にする
- Google Scholarで文献として認識されやすい形にする
- 将来の更新・version管理ができるようにする

役割分担は以下のようにする。

| 役割                                 | 置き場所                           | 目的                                    |
| ------------------------------------ | ---------------------------------- | --------------------------------------- |
| 実際に使う最新版テンプレート         | protocols.io                       | 手順・テンプレート本体・version管理     |
| Google Scholarで拾わせたい引用用文献 | ZenodoのArticleまたはPreprint      | DOI付きPDFとして文献化                  |
| 補助ファイル置き場                   | ZenodoまたはOSF Project            | Word版、Markdown版、使用例、更新履歴    |
| 必要に応じたpreprint置き場           | OSF系community preprint serverなど | 分野に合うpreprint serverがある場合のみ |

protocols.ioは公開プロトコルにDOIを付けられるため、実際に使うテンプレートの置き場として有用である。一方、Google Scholar対策としては、検索可能なPDF、タイトル、著者、出版日、メタデータが重要なので、ZenodoにArticleまたはPreprintとして短い説明文献を置く。Google Scholarの収録には著者・出版日などのメタデータが必要とされている。Zenodo側も、Google Scholarは主にtext content、つまりarticle系を対象にしやすいと説明している。
参考: https://www.protocols.io/
参考: https://scholar.google.com/intl/en/scholar/inclusion.html
参考: https://support.zenodo.org/help/en-gb/18-general/61-is-zenodo-indexed-by-google-scholar

## 2. Step 1: 既存のprotocols.ioテンプレートをアップデートする

最初に、すでに使っているprotocols.io上のテンプレートを更新する。今回更新対象は以下の2つで、両方を整合させる必要がある。

- protocols.io上の公開テンプレート（ライブ版・DOI付与の対象）
  - URL: https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw
  - 既知のバージョン表記: V.2
- 原本のdocxファイル（チームが編集している実体）
  - OneDrive上の原本: [protocol_template_for_intervention_review.docx](https://onedrive.live.com/:w:/g/personal/c48886b82268c3f3/UQDzw2giuIaIIIDEoh8AAAAAAOh7dYJ7YmFOrqE)（要認証）
  - リポジトリ内に同梱されたdocx: [resources/protocol_template_for_intervention_review.docx](resources/protocol_template_for_intervention_review.docx)
  - 内容確認用PDF: [resources/protocol_template_for_intervention_review-onedrive.pdf](resources/protocol_template_for_intervention_review-onedrive.pdf)
- protocols.io V.2 のPDFバックアップ: [resources/protocol-template-for-intervention-review-protocolio.pdf](resources/protocol-template-for-intervention-review-protocolio.pdf)

### 2.1 現在版の確認（自動取得済み）

protocols.io V.2 のPDFバックアップから抽出したメタデータ:

```text
Current title:              protocol_template_for_intervention_review V.2
Current protocols.io URL:   https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw
Current DOI:                https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2
External link (DOI):        https://doi.org/10.2490/prm.20260012   # Progress in Rehabilitation Medicine 掲載論文へ
Current version:            V.2  (Version 2)
Created:                    2022-08-26
Last Modified:              2022-08-26
Document Integer ID:        69212
License:                    Creative Commons Attribution (CC BY)
Journal association:        Progress in Rehabilitation Medicine
Authors:                    Yuki Kataoka(1), Yasushi Tsujimoto(2), Masahiro Banno(3), Shunsuke Taito(2), Ryuhei So(2), Jun Watanabe(2), Akihiro Shiroshita(2)
Affiliations:               (1) Department of Internal Medicine, Kyoto Min-Iren Asukai Hospital
                            (2) Systematic Review Work Shop-Peer Support Group
                            (3) Department of Psychiatry, Seichiryo Hospital
Keywords:                   protocol template-for-intervention review, procol template   # "procol" は誤字（V.3で修正対象）
Abstract:                   "This is a procol template."                                  # 同上、極端に短い・誤字あり
```

公式citation（protocols.io上の "Document Citation"）:

> Yuki Kataoka, Yasushi Tsujimoto, Masahiro Banno, Shunsuke Taito, Ryuhei So, Jun Watanabe, Akihiro Shiroshita 2022. protocol_template_for_intervention_review. protocols.io https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2

紐づけられているmanuscript citation（使用例として記載されている論文）:

> Okamura M, Shirado K, Shirai N, Yagi T, Inoue T, Ogawa M, Sullivan ES, haehling SV, Springer J, Anker SD, Momosaki R. 2026. Combined Nutritional and Exercise Interventions for Cachexia in Chronic Diseases: A Systematic Review and Meta-analysis Limited to Cancer Cachexia. Progress in Rehabilitation Medicine 11. doi:10.2490/prm.20260012

ユーザー側で追記が必要な項目:

```text
SRs already using this template (網羅的):    # 上記Okamura 2026以外で把握しているもの。なければ「Okamura 2026のみ把握」と記入
```

### 2.2 docx原本と公開版 V.2 の差分（自動取得済み）

両PDFを比較した結果のサマリ。

**メタデータ・形式の違い:**

| 項目                     | OneDrive docx                                          | protocols.io V.2                                        |
| ------------------------ | ------------------------------------------------------ | ------------------------------------------------------- |
| 内部に書かれた最終更新日 | 2021/10/30                                             | 2022/08/26 (Created/Last Modified)                      |
| 構成                     | 本文のみ（メタデータブロックなし）                     | protocols.ioによる表紙＋著者・DOI・citationブロック付き |
| 公開状態                 | OneDrive個人領域（チーム編集用の "ワーキング" コピー） | 公開・CC BY・DOI付与済み                                |

**本文の構成（章立て）は両者ほぼ一致**: Title → Last updated → メンターaffiliation案内 → Corresponding author → Author contributions → 1.Introduction → 2.Research question → 3.Method (3.1〜3.14) → 4.Summary of findings table → 5.Conflict of Interest → 6.Support → References → Appendix 1〜5。章番号レベルの相違はない。

**重要な内容差分（V.3で必ず取り扱う必要があるもの）:**

1. **Section 3.1 Protocol の自己引用URLが食い違う**
   - docx: `https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw`（現行URL）
   - protocols.io V.2: `dx.doi.org/10.17504/protocols.io.biqrkdv6`（**旧バージョンのDOI**を指している。V.2 自身の中で古い参照が残っている状態）
   - → **V.3 では V.2 自身のDOI（`10.17504/protocols.io.81wgbpb41vpk/v2`）または `https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw` を指すよう統一する必要がある。**
2. **Appendix 3: EMBASE search strategy の中身**
   - docx: S1〜S35の検索式が完全に記入されている
   - protocols.io V.2: 見出しのみで中身が空
   - → **V.3 では docx 側のS1-S35検索式を取り込んで公開版にも反映する。**
3. **Introduction のサンプル本文**
   - docx: 緑内障 + VEGF を題材にしたサンプル記述が残っている（"緑内障は眼科領域で最も失明に寄与する疾患である。"等）
   - protocols.io V.2: Introduction は空（プレースホルダのみ）
   - → サンプル本文はテンプレートとしてはノイズなので、**V.3 では削除 or "例:" として明示する**。
4. **メンターコメント（[片岡4][片岡5][片岡6]）の取扱い**
   - protocols.io V.2: 本文中に `[片岡4]` 等のWord校正コメントが残ったまま公開されている（GRADE評価担当・資金・CENTRALフィルターの注記）
   - docx: コメントマーカーは見当たらない（コメントとしてWord側に保持されている可能性あり）
   - → **V.3 では本文に混入している `[片岡N]` 記号を、注釈ブロックに切り出すか削除する。**
5. **Footnote脚注番号の混入（タイポ）**
   - V.2: "the eligibility based on the full texts.**[2]**We will contact original authors..." のように脚注番号が本文に挿入されてしまっている箇所が3.5.1, 3.5.2, 3.6 など複数あり
   - docx: 同等のテキストに脚注番号が混入していない
   - → **V.3 で番号を正しい上付き脚注に直すか削除する。**
6. **Abstract と Keywords の誤字**
   - V.2: Abstract が "This is a procol template." (procol → protocol)、Keywords も "procol template"
   - docx: Abstract / Keywords の指定なし
   - → **V.3 で Abstract と Keywords を書き直す（Google Scholar向けにも重要）。**
7. **Address / E-mail フィールドのプレースホルダ**
   - docx: "E-mail: yyy" のような明らかな埋め忘れ
   - V.2: Address/E-mail 自体が記載されていない
   - → これはテンプレート利用者が埋める前提なので、**V.3 でも空欄でよいが、注意書きを1行入れる**。

**結論（どちらを起点にするか）:**

- docxの方が本文・Appendix（特にEMBASE検索式）の完成度が高い箇所がある一方、protocols.io V.2 はメタデータ／DOI／公開citationを既に持っている。
- したがって **「docxを編集ベースとして使い、必要部分を反映した最終文書をprotocols.io V.3 として再公開」** という流れを推奨。

### 2.3 V.3 で取り込んだ変更点（ユーザー判断を反映済み）

| 項目 | 判断 | V.3 での扱い |
|---|---|---|
| Abstract を新規執筆 | **不要**。 別の Article として書く方が筋がよい | Abstract セクションは置くが、本文ではなく **PRISMA 2020 abstract checklist の項目（Item 2）をサブセクション**として並べる構造に変更 |
| Keywords 整理 | **やる** | "systematic review protocol", "intervention review", "PRISMA 2020", "Cochrane Handbook" に差し替え |
| Section 3.1 自己引用URL | **やる** | `10.17504/protocols.io.81wgbpb41vpk/v3` に統一 |
| Appendix 3 EMBASE 検索式 | **空欄でよい** | 見出しのみ、本文 `??????` |
| `[片岡4][片岡5][片岡6]` | **脚注化** | pandocフットノートに変換（mentor 関連注記をすべて footnote へ） |
| 脚注番号の本文行内混入 | やる | pandoc citeproc が `[@key]` を正しい番号引用に展開するので解決 |
| Intro のサンプル本文（緑内障+VEGF） | **削除** | 削除済み、`??????` のプレースホルダのみ |
| Address/E-mail プレースホルダ | やる | "テンプレ利用者が記入してください" を併記 |
| References フォーマット統一 | やる | BibTeX + Vancouver CSL（pandoc citeproc）で一元化 |
| Cochrane Handbook | **最新版に更新** | v6.5 (Aug 2024) に差し替え |
| PRISMA 2020 citation 追加 | やる | Page MJ et al. BMJ 2021;372:n71 を追加 |
| RevMan 5.4.2 | **PMA tools に動線変更** | `https://yukifurukawa.jp/pmatools/` を 3.12 で参照 |
| 著者欄の所属確認 | **テンプレートには入れない** | YAML front-matter に著者名のみ。JMIR 2025 ([PMID:41263436](https://pubmed.ncbi.nlm.nih.gov/41263436/)) と同形式: Yuki Kataoka / Ryuhei So / Masahiro Banno / Yasushi Tsujimoto / SRWS-PSG Mentors |

### 2.4 V.3 ドラフト成果物（リポジトリ内）

ユーザー判断に基づいて、V.3 ドラフトを Pandoc + BibTeX 構成で生成済み。

- ソース: [template/protocol_template_for_intervention_review.md](template/protocol_template_for_intervention_review.md)
- 文献データ: [template/references.bib](template/references.bib)
- ビルドスクリプト: [template/build.ps1](template/build.ps1) — `pwsh template/build.ps1 -Target docx|html|pdf`
- 自動生成（gitignore対象）: `template/build/` および `template/vancouver.csl`（初回ビルド時に Zotero スタイルリポジトリから取得）

ビルド済みdocx の例: [template/build/protocol_template_for_intervention_review.docx](template/build/protocol_template_for_intervention_review.docx)

レンダリング確認結果:

- 引用 `[@page2021prisma]` 等は Vancouver スタイルで `(1)`, `(2)` のように正しく番号付与
- 脚注（メンター注記）は文末にまとめて出力
- References 8件すべて整形済み

### 2.5 V.3 ドラフトに対するレビュー依頼

[template/build/protocol_template_for_intervention_review.docx](template/build/protocol_template_for_intervention_review.docx) を一度Wordで開いて、以下の3点を確認してください。

1. **著者リストは "Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors" でOKか**（V.2 にあった Taito / Watanabe / Shiroshita を外し、JMIR 2025 と揃えた）
2. **PRISMA 2020 abstract checklist のサブセクションの粒度**が想定通りか（Methods/Results/Discussion/Other 各2項目ずつ並べている）
3. **Cochrane Handbook v6.5 (Aug 2024) で確定でよいか**（バージョン番号は念のため公式サイトで最新確認した方が安全）

修正点があれば Markdown 側 ([template/protocol_template_for_intervention_review.md](template/protocol_template_for_intervention_review.md)) を直接編集するか、Claude に指示してください。

---

## 3. Step 2 以降（次にやる）

V.3 ドラフトのレビューが終わり次第:

1. **Step 1 完了**: protocols.io 上に V.3 を発行（既存引用は V.2 のまま残す方針確定済み）。
2. **Step 2: Zenodo article 化**
    - Markdown ベースで「テンプレートの説明」と「使い方ガイド」を書き、PDFを Zenodo にデポジット。
    - これが Google Scholar に拾われる引用用ドキュメントになる。
3. **Step 3: 補助ファイル置き場**（OSF or Zenodo に Word/Markdown/changelog をまとめる）。

## ユーザー側で残っている作業

1. ~~既存SRでの引用状況の追加確認~~ → 「Okamura 2026 のみ確実、他は記載はあるが実引用は実質ゼロ」で確定。
2. ~~V.3 変更点リストのレビュー~~ → 反映済み（[2.3](#23-v3-で取り込んだ変更点ユーザー判断を反映済み)）。
3. **新規: V.3 ドラフトのレビュー** → [2.5](#25-v3-ドラフトに対するレビュー依頼) の3点を確認してください。
4. **新規: protocols.io への V.3 アップロード手順の希望確認**
   - V.3 docx をそのまま protocols.io にインポート → 自動的に手順化される
   - または各セクションを protocols.io エディタで手動入力
   - protocols.io はdocxインポート機能を持つので前者推奨。ユーザー側で実際に試して見え方を確認してください。
5. ~~V.3 公開時のDOI運用~~ → 既存引用 `/v2` を残し V.3 は新DOIで発行、で確定。
