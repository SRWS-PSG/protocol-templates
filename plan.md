# Protocol template — GitHub + Zenodo 公開計画

作成日: 2026-05-16
最終更新: 2026-05-20
目的: 既存の protocols.io ベースのプロトコルテンプレートを **GitHub + Zenodo (version DOI) + MetaArXiv (Scholar 入口)** に移行し、バージョン管理・citability・Google Scholar 収録のすべてを改善する。

## 1. 全体方針

**役割分担（新アーキテクチャ）:**

| 役割 | 置き場所 | DOI | 自動化 | 目的 |
|---|---|---|---|---|
| テンプレート本体（編集対象） | **GitHub repository** (Markdown + BibTeX) | – | – | 単一の真実、フルバージョン管理、PR/Issueによる共同編集 |
| バージョンごとのDOI | **Zenodo (GitHub連携、`software`)** | `10.5281/zenodo.<n>` per release + concept DOI | ✅ 自動 | release を切るたびに version DOI が自動発行、concept DOI が "latest" を常に指す |
| テンプレートの解説論文 (Scholar 入口) | **MetaArXiv (OSF Preprints)** | `10.31222/osf.io/<id>` (+ `_v2`/`_v3` で版上げ) | ❌ 手動 | Google Scholar に確実にクロールされる publication-type preprint。引用可能・Scholar indexed |
| 旧テンプレートの凍結アーカイブ | **protocols.io V.2** (既存) | 既存 | – | 既存引用（Okamura 2026）を死なせない。概要欄に GitHub + MetaArXiv DOI への redirect 追記 |

**この構成のメリット:**

- GitHub は完全無料・ロックインなし
- Zenodo の GitHub 連携は研究ソフトウェア公開の事実上の標準、release毎の version DOI が手作業なく出る
- MetaArXiv は SR 方法論 preprint の専用サーバで、Scholar indexing 実績が大量にある（§1.1 参照）
- 役割分離：Zenodo は software / version DOI を担当、MetaArXiv は publication / Scholar 入口を担当。混線しない
- pandoc + BibTeX 構成がそのまま生かせる
- バージョン管理は git に任せられる
- protocols.io 上の既存引用は壊さない

参考:
- https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- https://support.zenodo.org/help/en-gb/19-uploading/65-how-do-i-link-my-github-repository-to-zenodo
- https://scholar.google.com/intl/en/scholar/inclusion.html
- https://support.zenodo.org/help/en-gb/18-general/61-is-zenodo-indexed-by-google-scholar
- https://osf.io/preprints/metaarxiv (MetaArXiv landing)
- https://help.osf.io/article/230-preprint-faqs (OSF preprints と Google Scholar)

### 1.1 Step 4 を MetaArXiv にする根拠（Zenodo Article は不採用、2026-05-20 訂正）

**Zenodo は upload_type に関わらず Google Scholar に拾われない**。Zenodo 公式 FAQ:

> "Google Scholar relies on patterns in the URL to determine the resource type ... Zenodo allows users to edit and change the resource type after publishing, which would mean the URL of records in Zenodo would change if you edited the resource type."
> "Google Scholar only indexes text content (articles) and thus other resource types in Zenodo is out of scope for Google Scholar."
> ([source](https://support.zenodo.org/help/en-gb/18-general/61-is-zenodo-indexed-by-google-scholar))

これは `upload_type=publication, publication_type=article` でも `preprint` でも同様。Zenodo と Google は構造上 Scholar クロールが噛み合わない状態が続いており、Article として deposit しても Scholar に載らない。**当初の plan §6（"Zenodo Article として deposit すれば Scholar に拾われる"）は誤認で、2026-05-20 に MetaArXiv に切り替えた**。

**代わりに MetaArXiv (OSF Preprints の meta-research / SR 方法論ブランチ) を採用する**:

- `site:osf.io metaarxiv` で Google Scholar に200本超の preprint が index されている（2026-05 確認）
- SR 方法論ツールの解説として直接同型の van den Akker 2020 [Inclusive systematic review registration form](https://scholar.google.com/scholar?q=%22Inclusive+systematic+review+registration+form%22+van+den+Akker) が MetaArXiv 経由で Scholar indexed
- OSF Preprints は Highwire 形式の `citation_title` / `citation_author` / `citation_publication_date` / `citation_publisher` / `citation_public_url` を Googlebot 向けに pre-render する。`citation_doi` と `citation_pdf_url` の meta tag は欠けているが、実証的に indexing は機能している
- scope: meta-research / SR methodology を明示的に扱う。プロトコルテンプレ解説は in-scope（precedent: van den Akker 2020）
- 無料、CC BY 4.0 可、DOI = `10.31222/osf.io/<id>` (Crossref経由で OpenAIRE/Scholar に発見される)
- 提出に moderator の scope 確認（数日）あり。peer-review ではない
- 提出後の version 管理あり (`<id>_v2`, `_v3` ...)
- 万一 MetaArXiv の moderator に scope outで弾かれた場合は **OSF Preprints の "Other" カテゴリ** にフォールバック（同じバックエンドで Scholar 挙動同一）

**結論：2-DOI 体制**

| 用途 | DOI | サービス | 自動化 |
|---|---|---|---|
| テンプレ本体の version DOI（「v3.0.0 を使った」を指す） | `10.5281/zenodo.<n>` | Zenodo (`software`, GitHub連携) | ✅ release 毎自動 |
| 解説論文の Scholar 入口、テンプレの設計思想を citable に | `10.31222/osf.io/<id>` | MetaArXiv (`publication`, 手動) | ❌ 手動 deposit |

Zenodo version DOI は Scholar には載らないが、permanent URL/引用識別子としては機能する（README/CITATION.cff/CHANGELOG に併記）。MetaArXiv DOI は Scholar 入口として機能する（テンプレ本体の Section 3.1 自己引用に併記）。

## 2. リポジトリ構成（現状）

GitHub では `SRWS-PSG/protocol-templates` に置く前提。ローカルディレクトリ名 `protocol-srwspsg` のままだが GitHub 上のリポジトリ名は `protocol-templates`。

```
protocol-templates/                     (local dir: protocol-srwspsg/)
├── README.md                  # プロジェクトの顔。GitHub上で最初に表示される
├── LICENSE                    # CC BY 4.0
├── CHANGELOG.md               # バージョン履歴（リポジトリ全体で1つに統一）
├── CITATION.cff               # GitHubの "Cite this repository" ボタン用
├── .zenodo.json               # Zenodo連携メタデータ（GitHub release時にZenodoが参照、software type）
├── .gitignore
├── CLAUDE.md                  # Claude Code 用作業メモ（リポジトリ固有指示）
├── plan.md                    # この計画書
├── resources/                 # 歴史的参照（V.2 PDF, 元docx）。リポジトリには含めるが編集はしない
│   ├── protocol_template_for_intervention_review.docx
│   ├── protocol_template_for_intervention_review-onedrive.pdf
│   ├── protocol-template-for-intervention-review-protocolio.pdf
│   ├── 2025-12-29スコーピングレビューのプロトコルテンプレ.docx
│   └── 20200304_診断精度SRのプロトコルテンプレ.docx
├── templates/
│   ├── intervention-review/                                  # V.3 本体
│   │   ├── protocol_template_for_intervention_review.md     # 編集対象 Markdown (en)
│   │   ├── protocol_template_for_intervention_review.ja.md  # JA
│   │   ├── references.bib                                   # BibTeX (intervention 専用)
│   │   ├── comments.yaml                                    # Google Docs メンタリングコメント
│   │   ├── build.ps1                                        # Pandocビルドスクリプト
│   │   └── build/                                           # 生成物（gitignore）
│   ├── scoping-review/                                       # v1.0
│   │   ├── protocol_template_for_scoping_review.md
│   │   ├── protocol_template_for_scoping_review.ja.md
│   │   ├── references.bib                                   # BibTeX (scoping 専用、独立)
│   │   ├── comments.yaml
│   │   ├── media/scoping_concept_focus.png                  # JBI Terminology-vs-Concept 図
│   │   ├── build.ps1
│   │   └── build/
│   └── dta-review/                                           # v1.0
│       ├── protocol_template_for_dta_review.md
│       ├── protocol_template_for_dta_review.ja.md
│       ├── references.bib                                   # BibTeX (DTA 専用、独立)
│       ├── build.ps1
│       └── build/
└── paper/                                                    # ★ NEW: Companion explanation paper (MetaArXiv 提出用)
    ├── manuscript.md                                         # 本文 (en)
    ├── manuscript.ja.md                                      # 本文 (ja, optional)
    ├── references.bib                                        # paper 専用 bib (3 templates の bib から methodology 親引用を抽出)
    ├── vancouver.csl
    ├── filters/                                              # pandoc filters (intervention-review から流用)
    ├── build.ps1                                             # pandoc → PDF
    └── build/                                                # 生成物（gitignore）
        └── manuscript.pdf                                    # MetaArXiv 提出用 PDF
```

**`paper/` の独立性に関する注意**：

- `paper/` は templates と independent な「解説論文」リポジトリ subtree。バージョンサイクルが分離している（templates は SemVer で頻繁、paper は major bump 時のみ更新）
- GitHub release 時 `paper/build/manuscript.pdf` は **release asset から除外**（Zenodo software deposit に paper PDF が混入するのを防ぐ）
- `paper/references.bib` は templates 各 bib から DOI-verified なエントリを抜粋して新規作成（cross-contamination 回避のため、templates の bib を直接 import しない）

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

リポジトリ名 `SRWS-PSG/protocol-templates` で確定済み。scaffolding ファイル内の URL は反映済み。

1. **git init して GitHub に push**
    ```powershell
    git init
    git add .
    git commit -m "Initial commit: v3.0.0 draft"
    git branch -M main
    git remote add origin https://github.com/SRWS-PSG/protocol-templates.git
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

## 6. Step 4: MetaArXiv preprint（テンプレ解説論文）

**目的**: Google Scholar に確実に拾われ、citable な解説 preprint として機能させる。Zenodo Article は Scholar 対象外のため不採用（[§1.1](#11-step-4-を-metaarxiv-にする根拠zenodo-article-は不採用2026-05-20-訂正)）。**MetaArXiv (OSF Preprints の meta-research / SR 方法論ブランチ) に手動 deposit する**。

### 6.1 提出先と判断根拠

| | 第一候補 | フォールバック |
|---|---|---|
| サービス | **MetaArXiv** | OSF Preprints "Other" |
| URL | <https://osf.io/preprints/metaarxiv> | <https://osf.io/preprints> |
| DOI 例 | `10.31222/osf.io/<id>` | `10.31219/osf.io/<id>` |
| scope | meta-research / SR methodology | 学術全般 |
| moderation | あり（数日、scope確認） | あり（scope確認） |
| Scholar indexing | 200+ preprint で実証済み | 同一バックエンドで挙動同等 |
| 費用 | 無料 | 無料 |
| license | CC BY 4.0 可 | CC BY 4.0 可 |

scope の precedent: van den Akker 2020 "Inclusive systematic review registration form" が MetaArXiv で publishされ Scholar indexed。本テンプレ解説論文は直接同型。

### 6.2 内容構成（最小構成、≈1800-2500 words）

PDF 1本に統合（intervention / scoping / DTA を別々ではなく1本にまとめる。moderation コストと cross-reference の容易さから）。

| セクション | 目安words | 必須要素 |
|---|---:|---|
| Title page | – | "SRWS-PSG protocol templates for systematic, scoping, and diagnostic test accuracy reviews"（仮）。24pt以上、ページ先頭 |
| Authors + affiliations | – | Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors、各 ORCID（取得済みの分）。16-23pt |
| Abstract | 200 | Background → 3 templates 概要 → repository URL → preprint DOI |
| 1. Background | 300 | 既存 SR protocol template の状況、protocols.io V.2 → GitHub+Zenodo+MetaArXiv 移行の理由 |
| 2. Design principles | 250 | PRISMA 系列準拠、Markdown + pandoc + BibTeX、SRWS-PSG メンタリング flow |
| 3. Intervention review template | 300 | PICO、Cochrane Handbook v6.5、PMA tools、PRISMA 2020、PRISMA-P 2015 |
| 4. Scoping review template | 300 | PCC、JBI 5-stage、PRISMA-ScR、Peters 2022、OSF 登録 |
| 5. DTA review template | 350 | PIRT、Cochrane DTA Handbook v2、QUADAS-3、PRISMA-DTA、MetaDTA |
| 6. Usage and citation | 200 | GitHub clone、release tag 指定、preprint DOI 引用、version DOI 引用 |
| 7. Versioning policy | 100 | SemVer 解釈、major/minor/patch の定義 |
| 8. Availability | 50 | GitHub URL、license、preprint DOI、Zenodo concept DOI |
| References | – | Vancouver、必須セクション、Scholar が "References" を識別できる体裁 |

Google Scholar の inclusion 要件（[公式](https://scholar.google.com/intl/en/scholar/inclusion.html)）を満たす：

- searchable-text PDF（pandoc標準で OK）、≤ 5 MB、no Type 3 fonts
- Title in largest font (≥ 24 pt) at top; authors below in 16–23 pt
- 識別可能な "References" / "Bibliography" セクション
- 5 MB 以下

OSF 側が Highwire 形式の `citation_*` meta tag を Googlebot 向けに pre-render するため、PDF 内 meta tag の埋め込みは不要（あれば bonus）。

### 6.3 制作フロー（リポジトリ内）

1. `paper/` ディレクトリを新設（§2 参照）
2. `paper/manuscript.md` を pandoc + BibTeX + Vancouver CSL で執筆（templates の build pipeline と同じスタック）
3. `paper/build.ps1` で `paper/build/manuscript.pdf` を生成
4. PDF を MetaArXiv に **手動 upload**（GitHub連携 ❌、これは Zenodo software deposit と完全分離）
5. moderation 通過後、`10.31222/osf.io/<id>` を取得
6. 発行された DOI を以下に反映 commit：
   - `paper/manuscript.md` の self-citation
   - `README.md`「Companion paper (Scholar-indexed)」セクション
   - `CITATION.cff` の identifiers
   - `templates/intervention-review/protocol_template_for_intervention_review.md` Section 3.1 自己引用
   - `templates/scoping-review/protocol_template_for_scoping_review.md` 同位置
   - `templates/dta-review/protocol_template_for_dta_review.md` 同位置

### 6.4 提出時メタデータ

| フィールド | 値 |
|---|---|
| Title | "SRWS-PSG protocol templates for systematic, scoping, and diagnostic test accuracy reviews"（仮） |
| Authors | Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors（順序確定要） |
| Abstract | manuscript.md の Abstract |
| Subjects | Medicine, Library and Information Science |
| Keywords | systematic review, protocol template, intervention review, scoping review, diagnostic test accuracy, PRISMA 2020, PRISMA-ScR, PRISMA-DTA, Cochrane Handbook, QUADAS-3, SRWS-PSG |
| License | CC BY 4.0 |
| Conflict of interest | テンプレ著者間に開示すべき COI なし（テンプレ運用の SRWS-PSG メンタリングのみ） |
| Funding | テンプレ運用は SRWS-PSG 内部運営、外部funding なし（要確認） |

### 6.5 メンテナンス方針

- preprint は **頻繁な版上げ不要**。テンプレ本体は SemVer で v3.x.x → v4.x.x と進めるが、preprint は構造的な大改変（テンプレの methodology framework 変更など）のときだけ MetaArXiv の version 機能（`<id>_v2`）で更新
- 細かな改訂は GitHub の README/CHANGELOG で吸収する
- preprint version は MetaArXiv 上で永続URL `<id>_v1`, `<id>_v2` ... と切り分けて発見可能

### 6.6 ユーザー側で実施

1. **著者リストと順序の確定**（推奨: Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors、テンプレ本体と同一順）
2. **各著者の ORCID iD 取得・確認**（提出時メタデータに必須ではないが Scholar 著者プロファイル紐付けに有用）
3. **OSF account 作成**（<https://osf.io/register>、ORCID 連携推奨）
4. paper ドラフト確定後、OSF "Add a Preprint" → "MetaArXiv" service 選択 → メタデータ + PDF upload
5. moderation 待ち（通常数日、最大1週間）→ accept されれば DOI 即時発行
6. **scope outで reject された場合のフォールバック**：OSF Preprints の "Other" カテゴリに再提出（同じ PDF とメタデータで OK、DOI prefix が `10.31219/...` に変わる）
7. DOI 反映 commit を main に push

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

優先度順（DOI 取得順を意識）:

1. **テンプレ 3 本のドラフトレビュー**
   - intervention-review V.3 ([§3.3](#33-v3-ドラフトに対するレビュー依頼))
   - scoping-review v1.0 ([§9.4](#94-ユーザー側で実施))
   - dta-review v1.0 ([§10.5](#105-ユーザー側で実施))
2. **paper/ ドラフトのレビュー**（Claude が Phase B-C で生成、確認は本ステップ）
3. **著者順序の確定と各著者 ORCID iD 取得**（[§6.6](#66-ユーザー側で実施)、CITATION.cff にも反映）
4. **git init + GitHub push** ([§4.1](#41-ユーザー側で実施)) — repo は `SRWS-PSG/protocol-templates` で確定
5. **MetaArXiv に paper を手動 deposit** ([§6.6](#66-ユーザー側で実施))
   - OSF account 作成 → "Add a Preprint" → MetaArXiv → PDF + metadata upload
   - moderation 通過 → DOI 取得 (`10.31222/osf.io/<id>`)
6. **MetaArXiv DOI を反映 commit** ([§6.3 step 6](#63-制作フローリポジトリ内))
   - README.md / CITATION.cff / paper/manuscript.md / templates/*/protocol_template_*.md Section 3.1
7. **Zenodo GitHub 連携を enable** ([§5.1](#51-ユーザー側で実施))
8. **GitHub v3.0.0 release 作成**（**paper/build/manuscript.pdf は release asset から除外**、Zenodo software deposit への混入回避）
9. **Zenodo concept/version DOI 自動発行を確認** → README / CITATION.cff / CHANGELOG に反映 commit ([§5.1-5](#51-ユーザー側で実施))
10. **protocols.io V.2 への redirect 追記**（GitHub URL + MetaArXiv DOI）([§7.1](#71-ユーザー側で実施))
11. **Scholar index 確認**（提出 2-6 週後、MetaArXiv preprint title で検索）— されない場合は OSF support 経由で metadata 確認 or [Scholar inclusion request](https://scholar.google.com/intl/en/scholar/inclusion.html)

---

## 9. Step 6: Scoping review template (v1.0)

### 9.1 スコープ

scoping review 用プロトコルテンプレートを新規追加。元 docx は [resources/2025-12-29スコーピングレビューのプロトコルテンプレ.docx](resources/2025-12-29スコーピングレビューのプロトコルテンプレ.docx)。テンプレ内容は、Joanna Briggs Institute (JBI) の 5 ステージ実施方法を骨格とし、protocol 文書の構造は Peters らの best practice ガイダンス（[JBI Evid Synth 2022;20(4):953-968](https://doi.org/10.11124/JBIES-21-00242), Table 1 = 17 項目チェックリスト）を満たすように欠落項目を補った。レビューの報告は PRISMA-ScR ([Tricco et al. Ann Intern Med 2018;169:467-473](https://doi.org/10.7326/M18-0850)) に従う。

intervention-review との重要な相違点:

- **PCC** (Population / Concept / Context) を eligibility のフレームワークに（PICO ではない）
- **CONCEPT FOCUS 図** ("terminology" vs "concept" の意思決定図) を §3.3.2 Concept に永続的に埋め込む — 元 docx の画像をそのまま流用 (`templates/scoping-review/media/scoping_concept_focus.png`)
- **量的合成は行わない**（Stage 5 は質的統合、evidence and gap map 含む可視化 — [Fredlund et al. 2024](https://doi.org/10.1002/cesm.12096), [South & Rodgers 2023](https://doi.org/10.1186/s13643-023-02309-y) を参照）
- **Risk of bias / Meta-bias / GRADE は optional**（行う場合のみ書く `> Note:` を当該位置に配置）
- **登録先は OSF**（PROSPERO は scoping を受け付けないため [@peters2022bestpractice]）
- **新規 Appendix 6**: Peters 2022 Table 2 ベースの charting form 例（Author/Year/Country/Population/Concept/Context/Methodology/Key findings）

### 9.2 成果物（リポジトリ内）

- ソース (ja): [templates/scoping-review/protocol_template_for_scoping_review.ja.md](templates/scoping-review/protocol_template_for_scoping_review.ja.md)
- ソース (en): [templates/scoping-review/protocol_template_for_scoping_review.md](templates/scoping-review/protocol_template_for_scoping_review.md)
- 文献データ: [templates/scoping-review/references.bib](templates/scoping-review/references.bib) — **intervention 版とは独立した別ファイル**。各エントリは PubMed/DOI 起点で検証済み。
- ビルドスクリプト: [templates/scoping-review/build.ps1](templates/scoping-review/build.ps1)
- Google Docs 投入用コメント定義: [templates/scoping-review/comments.yaml](templates/scoping-review/comments.yaml) — 元 docx 由来の Word コメントを section heading に再アンカリングし、新規スコーピング特有のコメントを追加（計 17 件）
- CONCEPT FOCUS 図: [templates/scoping-review/media/scoping_concept_focus.png](templates/scoping-review/media/scoping_concept_focus.png)
- 生成 docx 例: `templates/scoping-review/build/protocol_template_for_scoping_review.{ja,}.with-comments.docx` （gitignore、`pwsh templates/scoping-review/build.ps1` または `python tools/build_gdoc.py --template scoping-review --lang ja --dry-run` で再生成）

### 9.3 共通ツールの汎用化

[tools/build_gdoc.py](tools/build_gdoc.py) に `--template intervention-review|scoping-review` を追加し、テンプレ間で共有。アップロード state のキーは `<template>:<lang>` に変更（旧 `ja`/`en` キーは初回読み込み時に `intervention-review:<lang>` へ自動移行）。

### 9.4 ユーザー側で実施

1. 生成 docx を Word で開いて以下を確認:
   - CONCEPT FOCUS 図が §3.3.2 Concept 直下に表示されているか
   - 17 件の Word コメントが期待した見出し位置に付いているか
2. 必要なら `comments.yaml` のアンカー文字列を修正
3. Google Docs にアップロードしてレビュー: `python tools/build_gdoc.py --template scoping-review --lang ja`

---

## 10. Step 7: Diagnostic test accuracy (DTA) review template (v1.0)

### 10.1 スコープ

診断精度 (Diagnostic Test Accuracy; DTA) 系統的レビュー用プロトコルテンプレートを新規追加。元 docx は [resources/20200304_診断精度SRのプロトコルテンプレ.docx](resources/20200304_診断精度SRのプロトコルテンプレ.docx)（2020-03-04 版、A4 で約 4 ページの簡易テンプレ）。当該 docx は当時の旧版で、以下が古いまたは欠落している:

- 方法論引用が **Cochrane DTA Handbook v1.0 (2013)** で止まっている → v2.0 (2023, Deeks/Bossuyt/Leeflang/Takwoingi 編 [@deeks2023dtahandbook]) に更新
- バイアスリスク評価が **QUADAS-2 (2011)** のみ → 2026 年 2 月公開の **QUADAS-3** [@whiting2026quadas3]（および比較精度レビュー用 **QUADAS-C** [@yang2021quadasc]、AI 検査用 **QUADAS-AI** development [@guni2024quadasai]）に拡張
- **PRISMA-DTA** [@mcinnes2018prismadta] および E&E [@salameh2020prismadtaee] への準拠が明示されていない
- **GRADE for DTA** が "SoF テーブルを作る" としか書かれておらず、GRADE 21 part 1/2 (2020) [@schunemann2020grade21p1;@schunemann2020grade21p2] への参照がない
- 解析ソフトが **RevMan 5.1 + Stata 16.1** で止まっている → **MetaDTA** ([https://crsu-metadta.le.ac.uk/MetaDTA/](https://crsu-metadta.le.ac.uk/MetaDTA/)) [@patel2021metadta] に変更。University of Leicester CRSU が提供する無料のブラウザ Shiny アプリで、bivariate モデルによる pooled sensitivity/specificity、SROC、forest plot、対話的な感度分析を生成できる。R/Stata のインストール不要
- イントロ・著者欄・付録の体裁が intervention/scoping 版と揃っていない（YAML front-matter、`[English label / 日本語ラベル: ...]` プレースホルダ、`> Note:` 構造などが存在しない）

intervention-review / scoping-review との重要な相違点:

- **フレームワーク**: PICO ではなく **Participants / Index test / (Comparator) / Reference standard / Target condition** (DTA Handbook v2 ch.4)。`§2 Research question` および `§3.2 Inclusion criteria` のサブセクション構成をこれに合わせる。元 docx の "PICOT" 表記は廃止
- **アウトカム**: 2×2 セル数 (TP / FP / TN / FN) から導かれる **感度・特異度** が primary。有害事象は intervention 版同様 secondary として残す。
- **研究デザイン**: コホート研究、RCT の二次解析、case-control 研究を組み入れる（case series / case report は除外）。**paired vs unpaired comparative design** の扱いを `> Note:` で明示（QUADAS-C の前提）
- **検索戦略**: MEDLINE での **DTA フィルター不採用**（感度が低く Cochrane DTA Handbook v2 ch.6 で非推奨）。代わりに condition + index test ブロックの AND 検索のみ。RCT フィルターは付けない（介入版 Appendix 3 の Dialog RCT filter ブロックも DTA 版では削除）
- **バイアスリスク評価**: 既定で **QUADAS-3**（2026-02 公開、QUADAS-2 を置換）。Comparative accuracy review の場合は **QUADAS-C** を併用する `> Note:` を §3.5 に置く。Index test が AI/ML モデルの場合は **QUADAS-AI**（development) + STARD-AI 2025 [@sounderajah2025stardai] を併用する `> Note:` を追記
- **合成方法**: フォレストプロット（感度・特異度ペア表示）、SROC、**bivariate model** [@reitsma2005bivariate] / **HSROC model** [@rutter2001hsroc] を併記。同一閾値とみなせる場合は bivariate、閾値ばらつく場合は HSROC、研究数が少なすぎる（典型的に < 4）場合は記述統合のみ、という分岐を `> Note:` で明示
- **異質性評価**: SROC・forest plot 目視 + メタ回帰（閾値、対象集団、index test バージョンなど）。`I²` の数値カットオフは DTA では推奨されていないため、intervention 版 §3.10 の "I² 0–40%..." 文言は使わない
- **出版バイアス**: ファンネル非対称検定 (Egger 等) は DTA では非推奨 [@deeks2023dtahandbook]。臨床試験登録 / レジストリ検索 + 未出版データへの著者問い合わせのみ
- **登録先**: PROSPERO は DTA レビューを受け付ける（intervention 版と同様）。`§3.1 Protocol` で PROSPERO 登録予定とする
- **解析ソフト**: **MetaDTA** [@patel2021metadta] をデフォルトとする。bivariate モデルのフィット・forest plot・SROC・感度分析がブラウザ上で完結し、R/Stata のセットアップが不要なため SRWS-PSG メンティの初学者にも導入しやすい。HSROC が必要な場合は R `mada` 等の併用を Note で言及。Cochrane DTA Handbook v2 [@deeks2023dtahandbook] でも MetaDTA は推奨ツールとして掲載されている
- **新規 Appendix 6**: 2×2 表 + 研究特性チャーティング例（Author/Year/Country/Population/Setting/Index test/Reference standard/Target condition/TP/FP/FN/TN/Threshold/QUADAS-3 ratings）
- セルフチェック表は付けない: scoping 版の Appendix 7 (Peters 2022 17 項目チェックリスト) に相当する PRISMA-DTA + QUADAS-3 マッピング表は **採用しない**。テンプレ本体の見出し構造に従って書けば PRISMA-DTA / QUADAS-3 の主要項目は自動的にカバーされるため、自己チェック表は冗長と判断した

### 10.2 成果物（リポジトリ内）

v1.0 ドラフトの 1 周目を生成済み（2026-05-20）。`pwsh ./templates/dta-review/build.ps1` で ja/en の docx + html が再生成できることを確認済み（citeproc warning なし）。

- ソース (ja): [templates/dta-review/protocol_template_for_dta_review.ja.md](templates/dta-review/protocol_template_for_dta_review.ja.md)
- ソース (en): [templates/dta-review/protocol_template_for_dta_review.md](templates/dta-review/protocol_template_for_dta_review.md)
- 文献データ: [templates/dta-review/references.bib](templates/dta-review/references.bib) — **intervention / scoping 版とは独立した別ファイル**。`[§9.2](#92-成果物リポジトリ内)` のポリシーに従い、各エントリは PubMed/DOI 起点で検証済み（§10.4 のリスト参照）
- ビルドスクリプト: [templates/dta-review/build.ps1](templates/dta-review/build.ps1) — scoping 版をコピーし、`$sources` のパスを差し替えた（reference.docx は intervention 版を共有）
- フィルター: [templates/dta-review/filters/highlight.lua](templates/dta-review/filters/highlight.lua), [templates/dta-review/filters/style.css](templates/dta-review/filters/style.css) — scoping 版から流用
- Vancouver CSL: [templates/dta-review/vancouver.csl](templates/dta-review/vancouver.csl) — scoping 版からコピー
- 生成 docx 例: `templates/dta-review/build/protocol_template_for_dta_review.{ja,}.docx`（gitignore、`pwsh templates/dta-review/build.ps1` で再生成）

未着手（次回タスク）:

- Google Docs 投入用コメント定義: `templates/dta-review/comments.yaml` — 元 docx の青字コメント（"絶対に直接編集しないこと！" などのテンプレ運用注記、`03_05` 等のメンタリングセッション番号アンカー）はほとんどがレビュー運用上の注意事項で、本テンプレでは `> Note:` ブロックに吸収済み。DTA 特有の Google Docs コメント（"QUADAS-3 のドメイン別判定をどこに書くか" "閾値が混在する場合の解析方針の選び方" "MetaDTA でのデータ入力フォーマット" など 3–5 件）を新規に書き起こす予定
- [tools/build_gdoc.py](tools/build_gdoc.py) の `--template` 選択肢に `dta-review` を追加（§10.3 参照、コメント YAML 完成後）

### 10.3 共通ツールの追従

[tools/build_gdoc.py](tools/build_gdoc.py) の `--template` 選択肢に `dta-review` を追加。`§9.3` で導入済みの `<template>:<lang>` キー方式にそのまま乗る（追加マイグレーションは不要）。

### 10.4 references.bib の主要エントリ（投入予定、Web で検証済み — 2026-05-20 時点）

> Note: いずれも DTA テンプレに必須。`@page2021prisma`, `@Kataoka2026-tb`, `@Kataoka2025-kq`, `@Gartlehner2025-cm`, `@Flemyng2025-ru` は intervention/scoping 版 bib からそのまま再録する。

| BibTeX key | 引用 | 用途 |
|---|---|---|
| `deeks2023dtahandbook` | Deeks JJ, Bossuyt PM, Leeflang MM, Takwoingi Y (eds). *Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy* v2.0 (Jul 2023). [training.cochrane.org/handbook-diagnostic-test-accuracy](https://training.cochrane.org/handbook-diagnostic-test-accuracy) | §3.1 Protocol, §3.6 解析, §3.12 出版バイアス |
| `mcinnes2018prismadta` | McInnes MDF et al. JAMA 2018;319(4):388-396. doi:10.1001/jama.2017.19163. PMID 29362800 | §3.1 Protocol（報告ガイドライン）、§3.4 PRISMA-DTA フロー図 |
| `salameh2020prismadtaee` | Salameh JP et al. BMJ 2020;370:m2632. doi:10.1136/bmj.m2632 | §3.1 Protocol（PRISMA-DTA E&E）|
| `whiting2011quadas2` | Whiting PF et al. Ann Intern Med 2011;155(8):529-36. doi:10.7326/0003-4819-155-8-201110180-00009. PMID 22007046 | §3.5 RoB（移行期の参照）|
| `whiting2026quadas3` | Whiting PF et al. Ann Intern Med 2026;179(4):548-555. doi:10.7326/ANNALS-25-02104 | §3.5 RoB（既定ツール）|
| `yang2021quadasc` | Yang B et al. Ann Intern Med 2021;174(11):1592-1599. doi:10.7326/M21-2234. PMID 34698503 | §3.5 RoB（比較精度レビュー用 Note）|
| `guni2024quadasai` | Guni A, Sounderajah V, Whiting P, et al. JMIR Res Protoc 2024;13:e58202. doi:10.2196/58202. PMID 39293047 | §3.5 RoB（AI 検査用 Note、development protocol）|
| `sounderajah2021quadasaiposition` | Sounderajah V et al. Nat Med 2021;27(10):1663-1665. doi:10.1038/s41591-021-01517-0. PMID 34635854 | §3.5 RoB（AI 検査用 Note、position statement）|
| `bossuyt2015stard` | Bossuyt PM et al. BMJ 2015;351:h5527. doi:10.1136/bmj.h5527. PMID 26511519 | §3.4.2 データ抽出（一次研究の reporting 基準として）|
| `sounderajah2025stardai` | Sounderajah V et al. STARD-AI. Nat Med 2025. doi:10.1038/s41591-025-03953-8 | §3.5 RoB（AI 検査用 Note）|
| `reitsma2005bivariate` | Reitsma JB et al. J Clin Epidemiol 2005;58(10):982-990. doi:10.1016/j.jclinepi.2005.02.022. PMID 16168343 | §3.6 解析（同一閾値時）|
| `rutter2001hsroc` | Rutter CM, Gatsonis CA. Stat Med 2001;20(19):2865-2884. doi:10.1002/sim.942. PMID 11568945 | §3.6 解析（閾値ばらつき時）|
| `schunemann2020grade21p1` | Schünemann HJ et al. J Clin Epidemiol 2020;122:129-141. doi:10.1016/j.jclinepi.2019.12.020. PMID 32058070 | §4 Summary of findings（GRADE 21 part 1）|
| `schunemann2020grade21p2` | Schünemann HJ et al. J Clin Epidemiol 2020;122:142-152. doi:10.1016/j.jclinepi.2019.12.021. PMID 32058069 | §4 Summary of findings（GRADE 21 part 2）|
| `patel2021metadta` | Patel A, Cooper N, Freeman S, Sutton A. *Res Synth Methods* 2021;12(1):34-44. doi:10.1002/jrsm.1439. PMID 32706182 | §3.12 解析ソフト（MetaDTA、bivariate モデルの web 実装）|

QUADAS-AI は 2026-05-20 時点で正式版コンセンサスステートメントは未公開。テンプレでは "in development" と注記し、Sounderajah 2021 position + Guni 2024 protocol の 2 本を併記する。

### 10.5 ユーザー側で実施

1. 上記の方針で良いか確認（特に §10.1 の「QUADAS-3 を既定に、QUADAS-2 は移行期参照のみ」「DTA フィルター不採用」「出版バイアス検定なし」の 3 点）
2. 上記決定が固まったら Claude にテンプレ本体（`.ja.md` / `.md` / `references.bib` / `build.ps1` / `comments.yaml` / `filters/`）の生成を依頼
3. 生成 docx を Word で開いて以下を確認:
   - QUADAS-3 のドメイン構造に関する `> Note:` が §3.5 に収まっているか
   - Appendix 6 の 2×2 表テンプレが崩れていないか
   - Appendix 7 のチェックリスト表が崩れていないか
   - 移植したコメントが期待した見出し位置に付いているか
4. 必要なら `comments.yaml` のアンカー文字列を修正
5. Google Docs にアップロードしてレビュー: `python tools/build_gdoc.py --template dta-review --lang ja`
6. レビュー完了後、CHANGELOG.md に `dta-review v1.0` の項目を追加

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
