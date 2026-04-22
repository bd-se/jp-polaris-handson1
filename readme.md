# Polaris Hands-on セミナー用 Python アプリケーション

このリポジトリは、Polaris Hands-on セミナーで用いるPythonアプリケーションを管理しています。
このアプリケーションは、SAST/SCA 解析の対象として用いられ、意図的にセキュリティ・品質に問題のあるコードの書き方や、古いOSSコンポーネントを必要としています。

## 必要な環境

- Python 3.x

## インストール方法

1. このリポジトリをクローンします。
   ```
   git clone <repository-url>
   cd jp-polaris-handson1
   ```

2. 依存関係をインストールします。
仮想環境として venv を使用する例です。
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip list
   ```

終了の際には、```deactivate``` を使用します。


## 使い方

1. `config.yaml` ファイルを作成し、以下の形式でURLを指定します。
   ```yaml
   url: "https://example.com"
   ```

2. アプリケーションを実行します。
   ```
   python3 injection.py
   ```

## 注意事項

このアプリケーションは、セキュリティ解析の学習目的で作成されており、セキュリティ問題を意図的に含んでいます。

## ライセンス

このプロジェクトは学習目的で使用してください。
