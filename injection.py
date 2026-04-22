# yaml ファイルを読み込み、そこに書かれたURLにアクセスする。
# ただし、yaml ファイルの内容は外部から変更可能であるため、攻撃者が悪意のあるコマンドを
# 挿入する可能性がある。
# データの取得は curl コマンドを使用して行う。

import yaml
import subprocess

def get_data_from_url():
    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.Loader)
    
    url = config["url"]
    # OSコマンドインジェクションの脆弱性: shell=True でコマンドを実行
    command = f"curl {url}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    get_data_from_url()
