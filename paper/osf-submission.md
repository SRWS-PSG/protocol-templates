# OSF Preprints 投稿シート（MetaArXiv）

このファイルは OSF Preprints の "Add a Preprint" フォームにそのままコピペするための投稿メタデータと手順書。

> **投稿先変更の経緯**: 当初は OSF の汎用カテゴリ（"OSF Preprints" / "Other"）を予定していたが、
> **OSF は 2025-08-25 付けで汎用サーバーへの新規投稿を停止**した
> （"suspending submissions to this generalist server hosted by OSF Preprints"）。
> コミュニティ運営サービスは影響を受けないため、本原稿（SR方法論ツールの解説）の
> scope に合致する **MetaArXiv**（BITSS運営、research transparency / reproducibility）に投稿する。
> これは plan.md §6 の元々の第一候補であり、van den Akker 2020
> "Inclusive systematic review registration form" という同型の前例が Scholar 収録済み。

投稿先: **MetaArXiv** <https://osf.io/preprints/metaarxiv>
DOI prefix: `10.31222/osf.io/<id>`

提出ファイル: [build/manuscript.pdf](build/manuscript.pdf)（pandoc → LibreOffice、約 241 KB、searchable、< 5 MB）

---

## 0. 提出前チェックリスト（投稿者）

- [X] **GitHub リポジトリ `SRWS-PSG/protocol-templates` が Public になっている**
  （原稿が repo URL を本文・Abstract で引用するため必須。Private のままだとリンク切れになる）
- [X] `build/manuscript.pdf` を最新ソースから再生成済み（`pwsh ./paper/build.ps1 -Target pdf`）
- [ ] PDF をブラウザ/Acrobat で開き、テキスト選択できる（スキャン画像でない）ことを目視確認
- [ ] PDF に **affiliations（上付き番号 1–11）と corresponding author の email** が表示されている
- [ ] PDF 末尾に **Appendix S1（SRWS-PSG Mentors 名簿）** がある（4 named author を含まない）
- [ ] OSF アカウント作成済み（ORCID 連携推奨: [https://osf.io/register](https://osf.io/register)）
- [ ] 著者順序の最終確認: Kataoka / So / Banno / Tsujimoto / SRWS-PSG Mentors

---

## 1. 投稿フォームに入れるメタデータ（コピペ用）

### Title

```
Increasing the transparency and reproducibility of systematic-review protocols: structure-enforced, version-controlled templates for intervention, scoping, and diagnostic test accuracy reviews
```

### Authors（OSF の Contributors に1人ずつ追加）

1. Yuki Kataoka（submitting / corresponding author、ORCID 0000-0001-7982-5213 連携推奨。
   連絡先 email: youkiti@gmail.com）
2. Ryuhei So
3. Masahiro Banno
4. Yasushi Tsujimoto
5. SRWS-PSG Mentors（グループ著者。OSF では未登録ユーザーとして名前のみ登録。
   ORCID は無し。役割は "Conceptualization / Writing – review & editing"）

> 注: named author 4名の所属は PDF の title block 近傍（Affiliations 1–11）に記載済み。
> グループ著者 SRWS-PSG Mentors の個人名・所属は **Appendix S1（本文 PDF 内）** に収録した
> （living roster は Google Doc で維持: 1v3R5iXCcbCAtpSlzbRUL09VJAFqseUaaiO61AQdxugA）。
> OSF の各 Contributor プロフィールの所属は PDF の記載と一致させること。
> corresponding は Kataoka（youkiti@gmail.com）。

### Abstract（コピペ）

```
Blank-document templates and chapter-length methodology handbooks are a high barrier for systematic-review (SR) teams new to protocol writing. We describe the SRWS-PSG protocol templates, designed so that completing the section structure itself produces a protocol compliant with the relevant reporting guideline. The Markdown-based, version-controlled collection covers three SR types: intervention reviews, scoping reviews (structured around the JBI five-stage methodology and the Peters et al. 2022 best-practice checklist), and diagnostic test accuracy (DTA) reviews (aligned with the Cochrane DTA Handbook v2.0 and QUADAS-3). Each template is reproducible (pandoc + BibTeX), citable (released on GitHub with version DOIs minted via Zenodo), and reusable (CC BY 4.0). Templates are maintained at https://github.com/SRWS-PSG/protocol-templates. We report the design principles, the methodological choices made for each review type, and the process by which the templates were developed.
```

### License

```
CC BY 4.0 (Creative Commons Attribution 4.0 International)
```

### Subjects（OSF は bepress taxonomy から選択）

- Medicine and Health Sciences
- Library and Information Science
  （必要に応じ "Medicine and Health Sciences > Public Health > Health Services Research" まで掘る）

### Keywords（OSF の Tags に1つずつ）

```
systematic review
protocol template
intervention review
scoping review
diagnostic test accuracy
PRISMA 2020
PRISMA-ScR
PRISMA-DTA
Cochrane Handbook
QUADAS-3
SRWS-PSG
reproducibility
research transparency
```

### Conflict of interest（OSF の専用フィールド）

```
The authors declare no conflicts of interest related to this work.
```

### Funding / Grant（OSF の専用フィールド）

```
This work received no external funding. SRWS-PSG operates as a peer-support community for SR methodology mentoring.
```

### Original publication / Peer-reviewed?

- "Has this work been published or peer-reviewed elsewhere?" → **No**（preprint なので未公開）
- License holder / copyright → 著者

---

## 2. 投稿手順（OSF Web UI、self-service / 自動化不可）

1. **MetaArXiv のページから投稿**: [https://osf.io/preprints/metaarxiv](https://osf.io/preprints/metaarxiv) → **Add a Preprint**
   （または [https://osf.io/preprints](https://osf.io/preprints) → Add a Preprint → provider 選択で **"MetaArXiv"**）
   ※ 汎用 "OSF Preprints"（Other）は 2025-08-25 で新規投稿停止のため選べない
2. **Upload**: `paper/build/manuscript.pdf` をアップロード（新規 OSF project が自動作成される）
3. **Basics**: License = CC BY 4.0、Abstract（上記）、Tags（上記）
4. **Discipline / Subjects**: 上記 Subjects を選択
5. **Authors / Contributors**: 上記5名を順序通りに追加
6. **Conflict of interest / Funding**: 上記文面を貼り付け
7. **Supplemental materials**（任意）: GitHub repo URL [https://github.com/SRWS-PSG/protocol-templates](https://github.com/SRWS-PSG/protocol-templates) を関連リンクとして登録
8. **Submit** → MetaArXiv は **scope 確認の moderation あり**（数日〜1週間）
9. 受理 → DOI 即時発行（`10.31222/osf.io/<id>`）

> **scope out で reject された場合**: MetaArXiv は「research transparency / reproducibility」が主眼。
> SR方法論ツールは in-scope（van den Akker 2020 前例）だが、万一弾かれたら
> OSF サポート（support@cos.io）に scope 相談、または OSF 外の generalist preprint server
> （例: Preprints.org, Research Square）を検討。Zenodo は Scholar 非収録のため不可（plan.md §1.1）。

---

## 3. DOI 取得後の反映（Claude に依頼可）

取得した `10.31222/osf.io/<id>` を以下に反映して commit（plan.md §6.3 step6 相当）:

- `paper/manuscript.md` の YAML `preprint-doi:` と §6 / §8 の self-citation
- `README.md`「Companion paper」セクション
- `CITATION.cff` の `identifiers`
- `templates/intervention-review/protocol_template_for_intervention_review.md` Section 3.1
- `templates/scoping-review/protocol_template_for_scoping_review.md` 同位置
- `templates/dta-review/protocol_template_for_dta_review.md` 同位置

---

## 4. 投稿後

- 2–6 週後に Google Scholar で preprint タイトル検索し index を確認
- されない場合は OSF support 経由で metadata 確認、または Scholar inclusion request
  ([https://scholar.google.com/intl/en/scholar/inclusion.html](https://scholar.google.com/intl/en/scholar/inclusion.html))
</content>
