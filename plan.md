# Protocol template — GitHub + Zenodo 公開計画

作成日: 2026-05-16
最終更新: 2026-05-16
目的: 既存の protocols.io ベースのプロトコルテンプレートを **GitHub + Zenodo** に移行し、バージョン管理・citability・Google Scholar 収録のすべてを改善する。

## 1. 全体方針

**役割分担（新アーキテクチャ）:**

| 役割 | 置き場所 | 目的 |
|---|---|---|
| テンプレート本体（編集対象） | **GitHub repository** (Markdown + BibTeX) | 単一の真実、フルバージョン管理、PR/Issueによる共同編集 |
| バージョンごとのDOI | **Zenodo (GitHub連携)** | release を切るたびに version DOI が自動発行、concept DOI が "latest" を常に指す |
| テンプレートの解説論文 | **Zenodo Article/Preprint** | Google Scholar に拾わせる citable な解説文献 |
| 旧テンプレートの凍結アーカイブ | **protocols.io V.2** (既存) | 既存引用（Okamura 2026）を死なせない。概要欄に GitHub への redirect 1行追記 |

**この構成のメリット:**

- GitHub は完全無料・ロックインなし
- Zenodo の GitHub 連携は研究ソフトウェア公開の事実上の標準
- pandoc + BibTeX 構成がそのまま生かせる
- バージョン管理は git に任せられる
- protocols.io 上の既存引用は壊さない

参考:
- https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- https://support.zenodo.org/help/en-gb/19-uploading/65-how-do-i-link-my-github-repository-to-zenodo
- https://scholar.google.com/intl/en/scholar/inclusion.html
- https://support.zenodo.org/help/en-gb/18-general/61-is-zenodo-indexed-by-google-scholar

### 1.1 Step 4 (Zenodo Article preprint) を残す根拠

Zenodo の **GitHub 自動 deposit は software-type** で deposit される。Zenodo 公式 FAQ にて以下が明記されている:

> "Google Scholar only indexes text content (articles) and thus other resource types in Zenodo is out of scope for Google Scholar."
> ([source](https://support.zenodo.org/help/en-gb/18-general/61-is-zenodo-indexed-by-google-scholar))

つまり GitHub-Zenodo 連携で発行される DOI は permanent citation の役には立つが、**Scholar での discoverability には寄与しない**。Scholar に拾わせたい場合は別途 publication-type の deposit （Article / Preprint）が必要。これが Step 4 を残す唯一の理由。

## 2. リポジトリ構成（現状）

GitHub では `srws-psg/protocol-templates` に置く前提。ローカルディレクトリ名 `protocol-srwspsg` のままだが GitHub 上のリポジトリ名は `protocol-templates`。

```
protocol-templates/                     (local dir: protocol-srwspsg/)
├── README.md                  # プロジェクトの顔。GitHub上で最初に表示される
├── LICENSE                    # CC BY 4.0
├── CHANGELOG.md               # バージョン履歴（リポジトリ全体で1つに統一）
├── CITATION.cff               # GitHubの "Cite this repository" ボタン用
├── .zenodo.json               # Zenodo連携メタデータ（GitHub release時にZenodoが参照）
├── .gitignore
├── CLAUDE.md                  # Claude Code 用作業メモ（リポジトリ固有指示）
├── plan.md                    # この計画書
├── resources/                 # 歴史的参照（V.2 PDF, 元docx）。リポジトリには含めるが編集はしない
│   ├── protocol_template_for_intervention_review.docx
│   ├── protocol_template_for_intervention_review-onedrive.pdf
│   └── protocol-template-for-intervention-review-protocolio.pdf
└── templates/
    └── intervention-review/                                  # ★ V.3 本体
        ├── protocol_template_for_intervention_review.md     # 編集対象 Markdown
        ├── references.bib                                   # BibTeX
        ├── build.ps1                                        # Pandocビルドスクリプト
        └── build/                                           # 生成物（gitignore）
```

将来 `templates/scoping-review/`, `templates/dta-review/` などを追加する想定。

## 3. Step 1: テンプレート本体の Markdown 化（完了）

V.2 docx + protocols.io V.2 PDF を起点に、Markdown ベースの V.3 を作成し、Pandoc レンダリングが通ることを検証済み。

### 3.1 V.3 で取り込んだ変更点

| 項目 | V.2 の状態 | V.3 での扱い |
|---|---|---|
| Abstract | 誤字あり ("procol template") | PRISMA 2020 abstract checklist (Item 2) のサブセクションに置換 |
| Keywords | "procol template" 誤字 | "systematic review protocol", "intervention review", "PRISMA 2020", "Cochrane Handbook" |
| Section 3.1 自己引用URL | 旧DOI `biqrkdv6` が残存 | **GitHub URL + Zenodo concept DOI** に変更 |
| Appendix 3 EMBASE 検索式 | V.2では空、docxでは S1-S35 | V.3では空欄でよい（ユーザーが埋める） |
| `[片岡4][片岡5][片岡6]` の本文混入 | V.2本文に校正コメントが残存 | Pandoc footnoteに切り出し |
| 本文行内の脚注番号 `[2][3]` | mis-rendered | citeproc が `[@key]` を正しく番号付与 |
| Introduction の緑内障+VEGF サンプル | docxに残存 | 削除、`??????` のみ |
| Address/E-mail プレースホルダ | 埋め忘れ ("yyy") | 「テンプレ利用者が記入してください」明記 |
| References フォーマット | docx/V.2でばらつき | BibTeX + Vancouver CSL で一元化 |
| Cochrane Handbook | v6.0 (2019) | **v6.5 (Aug 2024)** |
| PRISMA 2020 citation | なし | Page MJ et al. BMJ 2021;372:n71 を追加 |
| RevMan 5.4.2 | 古い | **PMA tools** (<https://yukifurukawa.jp/pmatools/>) に変更 |
| 著者リスト・所属 | 7名+所属付き | JMIR 2025 ([PMID:41263436](https://pubmed.ncbi.nlm.nih.gov/41263436/)) と同形式: Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors。所属はテンプレに入れない |

### 3.2 ドラフト成果物（リポジトリ内）

- ソース: [templates/intervention-review/protocol_template_for_intervention_review.md](templates/intervention-review/protocol_template_for_intervention_review.md)
- 文献データ: [templates/intervention-review/references.bib](templates/intervention-review/references.bib)
- ビルドスクリプト: [templates/intervention-review/build.ps1](templates/intervention-review/build.ps1)
- 生成docx例: [templates/intervention-review/build/protocol_template_for_intervention_review.docx](templates/intervention-review/build/protocol_template_for_intervention_review.docx)

### 3.3 V.3 ドラフトに対するレビュー依頼

[templates/intervention-review/build/protocol_template_for_intervention_review.docx](templates/intervention-review/build/protocol_template_for_intervention_review.docx) を Word で開いて以下を確認してください。

1. **著者リスト** が "Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors" でよいか
2. **PRISMA 2020 abstract サブセクション** の粒度
3. **Cochrane Handbook v6.5 (Aug 2024)** が現時点で最新であることの確認（[公式](https://training.cochrane.org/handbook)で要再確認）

## 4. Step 2: GitHub リポジトリの公開

リポジトリ scaffolding（LICENSE / README / CITATION.cff / .zenodo.json / CHANGELOG / .gitignore）は作成済み。残りはユーザー作業。

### 4.1 ユーザー側で実施

リポジトリ名 `srws-psg/protocol-templates` で確定済み。scaffolding ファイル内の URL は反映済み。

1. **git init して GitHub に push**
    ```powershell
    git init
    git add .
    git commit -m "Initial commit: v3.0.0 draft"
    git branch -M main
    git remote add origin https://github.com/srws-psg/protocol-templates.git
    git push -u origin main
    ```
2. **著者の ORCID を [CITATION.cff](CITATION.cff) に追記**（各自の ORCID iD を埋めるとZenodo側でも著者プロファイルが正しく紐づく）
3. **必要なら GitHub repo の Description / Topics / About を整える**（Topics 例: `systematic-review`, `protocol`, `template`, `cochrane`, `prisma`）

## 5. Step 3: Zenodo GitHub連携と初回 release

### 5.1 ユーザー側で実施

1. **Zenodo にログイン**（<https://zenodo.org/login>）→ ORCIDかGitHubでサインイン
2. **GitHub連携を有効化**: Zenodo の「GitHub」設定画面で該当 repository のトグルを ON
3. **GitHub で v3.0.0 release を作成**
   - tag: `v3.0.0`
   - title: "SRWS-PSG protocol templates v3.0.0"
   - description: CHANGELOG.md の `[Unreleased]` セクションをコピー
4. **release が作られた瞬間に Zenodo が snapshot + version DOI を自動発行**
5. **発行された DOI を反映**:
   - [.zenodo.json](.zenodo.json) は次回以降の release 用にもう更新不要
   - [README.md](README.md) の `10.5281/zenodo.<TBD>` を **concept DOI** に置換
   - [CITATION.cff](CITATION.cff) の identifiers にも concept DOI を記入
   - [CHANGELOG.md](CHANGELOG.md) の `[Unreleased]` を `[3.0.0] – 2026-MM-DD` に書き換え、version DOI も併記
   - [templates/intervention-review/protocol_template_for_intervention_review.md](templates/intervention-review/protocol_template_for_intervention_review.md) の YAML `zenodo-concept-doi:` と Section 3.1 のテキストを置換
6. **DOI 反映の commit を main に push（release本体は v3.0.0 のままで OK。次に v3.0.1 等を切るのは大きな修正時のみ）**

### 5.2 Concept DOI vs Version DOI

Zenodoは2種類のDOIを発行する:

- **Version DOI**: 各 release 専用。`10.5281/zenodo.1234567` のような形。論文等で「使った版」を引用するときに使う。
- **Concept DOI**: リポジトリ単位の "umbrella" DOI。常に最新版 release に resolve する。`10.5281/zenodo.1234566` のような形（version DOI と1違いになることが多い）。READMEや一般的な「このテンプレートを使った」の引用に使う。

テンプレ内の自己引用は **version DOI** を SR 著者が選んで埋める前提。READMEは **concept DOI** で十分。

## 6. Step 4: Zenodo Article（テンプレ解説論文）

**目的**: Google Scholar に拾わせる。GitHub-Zenodo の自動 deposit は software-type で出るため Scholar 対象外（[§1.1](#11-step-4-zenodo-article-preprint-を残す根拠)）。Scholar に載るためにはpublication-type の deposit が必要なので、**解説文献を Zenodo Article として別途出す**。

### 6.1 内容構成（案）

- Background: 既存のSR protocol templateの状況、なぜ独自テンプレートを作ったか
- Design principles: PRISMA 2020 + Cochrane Handbook ベース、SRWS-PSG メンタリング flow での使用想定
- Section-by-section guide: テンプレ各セクションの意図と典型的な書き方
- How to cite: version DOI を使う運用の説明
- Versioning policy: SemVerの解釈、breaking change の定義
- Acknowledgements / Funding / COI

### 6.2 制作フロー

1. `article/` ディレクトリを新設、Markdownで原稿執筆
2. 同じ pandoc + BibTeX 構成でPDFに変換
3. Zenodo に **upload_type=publication, publication_type=article** で手動デポジット（GitHub連携経由ではなく手動 upload）
4. 解説論文側はテンプレ本体の concept DOI を引用、テンプレ本体（READMEと CHANGELOG）から解説論文の DOI を相互参照

### 6.3 メンテナンス方針

- 解説論文は **頻繁な版上げは不要**。テンプレ本体は SemVer で v3.x.x → v4.x.x と進めるが、解説論文は構造的な大改変（major bump）のときだけ更新を検討する。
- 細かな改訂は GitHub の README/CHANGELOG で吸収する。

### 6.4 ユーザー側で実施

- 筆頭著者の確定（推奨: 片岡先生）
- 共著者リストの確定（テンプレ本体と同じ Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors でよい想定）
- 執筆開始のタイミング（Step 3 完了後、concept DOI が確定してから書き出すのが楽）

## 7. Step 5: protocols.io V.2 への redirect 追記

新しい GitHub repo + Zenodo concept DOI が確定したら、protocols.io V.2 の概要欄に redirect 案内を追記して凍結する。

### 7.1 ユーザー側で実施

1. **protocols.io にログイン**
2. **V.2 ページの "Description / Abstract" を編集**して、以下のような1行を末尾に追記:
   ```
   NOTE: This template is now maintained on GitHub at <REPO_URL>.
   The Zenodo DOI for the latest release is 10.5281/zenodo.<CONCEPT_DOI>.
   Versions on protocols.io are no longer updated.
   ```
3. **V.3 を protocols.io 上では作らない**（V.2 のまま凍結。version 履歴は GitHub + Zenodo 側で管理）
4. **既存引用への影響**: Okamura 2026 が引用している `/v2` はそのまま resolve するので **影響なし**

## 8. ユーザー側で残っているタスク（一覧）

優先度順:

1. **V.3 ドラフトのレビュー** ([§3.3](#33-v3-ドラフトに対するレビュー依頼))
2. **git init + GitHub push** ([§4.1](#41-ユーザー側で実施)) — repo は `srws-psg/protocol-templates` で確定
3. **ORCID を CITATION.cff に追記** ([§4.1](#41-ユーザー側で実施))
4. **Zenodo GitHub 連携 + v3.0.0 release** ([§5.1](#51-ユーザー側で実施))
5. **DOI が確定したら scaffolding ファイル内の `<TBD>` を置換** ([§5.1-5](#51-ユーザー側で実施))
6. **解説論文の執筆方針確定** ([§6.4](#64-ユーザー側で実施))
7. **protocols.io V.2 への redirect 追記** ([§7.1](#71-ユーザー側で実施))

---

## 付録 A: V.2 メタデータ（凍結アーカイブ）

protocols.io V.2 のPDFバックアップから抽出（[resources/protocol-template-for-intervention-review-protocolio.pdf](resources/protocol-template-for-intervention-review-protocolio.pdf)）。今後も resolvable。

```text
Title:                      protocol_template_for_intervention_review V.2
URL:                        https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw
DOI:                        https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2
External link:              https://doi.org/10.2490/prm.20260012  (Okamura M 2026)
Created / Last Modified:    2022-08-26
License:                    CC BY
Authors (V.2):              Kataoka(1), Tsujimoto(2), Banno(3), Taito(2), So(2), Watanabe(2), Shiroshita(2)
Affiliations (V.2):         (1) Department of Internal Medicine, Kyoto Min-Iren Asukai Hospital
                            (2) Systematic Review Work Shop-Peer Support Group
                            (3) Department of Psychiatry, Seichiryo Hospital
```

公式 citation (V.2, 凍結):

> Yuki Kataoka, Yasushi Tsujimoto, Masahiro Banno, Shunsuke Taito, Ryuhei So, Jun Watanabe, Akihiro Shiroshita 2022. protocol_template_for_intervention_review. protocols.io https://dx.doi.org/10.17504/protocols.io.81wgbpb41vpk/v2

## 付録 B: V.2 と docx 原本の差分（参考）

詳細な差分は git 履歴に残るのでここでは要点のみ。

- docx (最終更新 2021-10-30) は protocols.io V.2 (2022-08-26) より古いが、Appendix 3 EMBASE 検索式や Introduction サンプル本文を含んでいた。
- protocols.io V.2 は表紙メタデータ・DOI・公開citationを持つが、本文に `[片岡4][片岡5][片岡6]` の校正コメントや脚注番号の混入などの問題があった。
- V.3 では両者の良い部分を統合し、上記すべてを Markdown + BibTeX に整理し直した。
