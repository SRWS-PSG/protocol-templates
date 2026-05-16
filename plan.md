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
  - 既知のバージョン表記: V.2 （ページタイトルから確認、その他メタデータはログイン or 手動確認が必要）
- 原本のdocxファイル（チームが編集している実体）
  - 場所: [protocol_template_for_intervention_review.docx](https://onedrive.live.com/:w:/g/personal/c48886b82268c3f3/UQDzw2giuIaIIIDEoh8AAAAAAOh7dYJ7YmFOrqE)（OneDrive・要認証）

> 注: 上記2リソースは、いずれも本リポジトリからは自動アクセスできない（OneDriveは認証必須、protocols.ioはJSレンダリングでメタデータが取れない）。差分把握と現在版メタデータの取得は、ユーザー手作業で行う前提とする（後述「ユーザー側で実施が必要な作業」参照）。

### 2.1 現在版の確認

実施内容:

- 現在のprotocols.ioプロトコルのURL・タイトル・著者・説明文・DOI・version・公開日・推奨citationを確認する
- 現在の本文（手順・記載項目）をPDF or Word or Markdownでバックアップしておく（更新後の差分検証用）
- 既にSR論文等で引用されているURL/DOIがあれば、それを記録する（古いDOIを生かす運用か、新DOIへ差し替えるかの判断材料）

記録項目（埋めるのはユーザー、自動取得できたものは事前記入済み）:

```text
Current title: protocol_template_for_intervention_review V.2
Current protocols.io URL: https://www.protocols.io/view/protocol-template-for-intervention-review-cft4tnqw
Current DOI:                                  # protocols.ioの該当ページから取得（dx.doi.org/10.17504/... 形式）
Current version: V.2                          # 要確認: V.2 が最新公開版で間違いないか
Current publication date:                     # protocols.ioのページ右側に表示
Current citation format:                      # protocols.ioの "Cite this protocol" から取得
SRs already using this template:              # 把握しているSR論文 or 「未把握」と記入
Backup file (current version):                # バックアップ先のパス or リンク
```

### 2.2 docx原本と公開版の差分確認

protocols.io上の公開版（V.2）と、OneDrive上のdocx原本との間に既に差分があるかを確認する。

- どちらが「真の最新」か（docxを編集中で公開版に反映待ち、なのか、公開版が最新でdocxは古いコピーなのか）
- 構成・節タイトルレベルで差分があるか
- 文言レベルでの修正が含まれているか

記録項目:

```text
docx last modified date:
protocols.io last updated date:
Which is newer (docx / protocols.io / same):
Section-level differences (見出しレベル):
Text-level differences (要点のみ):
Decision: どちらを今回のアップデートの起点にするか
```

---

## ユーザー側で実施が必要な作業（自動化できないもの）

以下はClaude側から実行できないため、ユーザー（youkiti@gmail.com）が手動で行う必要がある。完了したらこのファイルの該当記録項目を埋めてもらえれば、以降の計画作りを続けられる。

1. **protocols.ioにログインして現在版（V.2）のメタデータを抽出**
   - DOI、公開日、推奨citation形式、著者一覧、abstractをコピーして [2.1の記録項目](#21-現在版の確認) に貼り付ける。
2. **protocols.io V.2 のバックアップ取得**
   - 「Export → PDF」もしくは印刷PDFで現在版を保存。ファイル名例: `backup/protocols-io_v2_2026-05-16.pdf`。
3. **OneDriveのdocx原本の中身を、このリポジトリで参照できる形にする**
   - 選択肢A: docxをこのリポジトリにコピーして同梱する（`templates/protocol_template_for_intervention_review.docx`）。
   - 選択肢B: docxをMarkdown化してリポジトリに置く（差分管理しやすい）。Pandoc等で `templates/protocol_template_for_intervention_review.md` を生成。
   - どちらでもよいが、選んだ方を教えてもらえれば以降の差分作業はClaude側で進められる。
4. **既存SRでの引用状況の棚卸し**
   - 既にこのテンプレートを引用しているSR論文（自分のもの・チームのもの）があれば、引用URL/DOIをリストアップ。なければ「未引用」と明記。これは「DOIを差し替えても影響あるか / 旧DOIを残すか」の判断に使う。
5. **次に進めてよいタイミングの合図**
   - 上記1〜4のうち最低限 1（メタデータ）と 3（docx取り込み）が済んだら、計画の Step 1 後半（実際の更新作業の章立て）と Step 2（Zenodo article作成）を書き進める。
