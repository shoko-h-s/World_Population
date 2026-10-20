# 世界人口データビューア (1960 – 2025)

世界人口データ（1960〜2025年）をベースに、Streamlit を活用してブラウザ上で人口推移を直感的に比較・確認できるインタラクティブな Web アプリの実装リポジトリです。

- [🌐 世界人口データビューア](https://world-population-65years.streamlit.app/ "🌐 世界人口データビューア")
- [📝 開発の裏話やこだわり（note）](https://note.com/shoko_hs89/n/n86b31f835110)

## 📊 アプリ概要

Kaggle で公開されている [World Population: 65 years Demographics(1960–2025)](https://www.kaggle.com/datasets/mnkaggler/world-population-65-years-demographics19602025) のデータセットから必要な数値を抽出し、ブラウザ上で国別の人口推移を比較できるツールとして構築しました。

主な機能:

- サイドバーによる複数国のマルチセレクト比較（初期設定: 日本 ＋ 人口上位 3 国）
- 1960 年から 2025 年までの5年ごとの人口データを折れ線グラフでリアルタイム描画
- 詳細データの数値テーブル表示（トグル切替式）

## 🛠️ 技術スタック / 使用ライブラリ

- Python
- Pandas（データの読み込み・整形処理）
- Streamlit（UI 構築・Web アプリのローカル & クラウドホスティング）

## 🚀 ローカルでの実行方法

1. リポジトリのクローンまたはファイルのダウンロード
1. 依存ライブラリのインストールとアプリの起動

```bash
pip install -r requirements.txt
streamlit run app.py
```
