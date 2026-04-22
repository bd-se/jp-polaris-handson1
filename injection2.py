# yaml ファイルを読み込み、そこに書かれたURLにアクセスする。
# ただし、yaml ファイルの内容は外部から変更可能であるため、攻撃者が悪意のあるコマンドを
# 挿入する可能性がある。
# データの取得に curl を使わない

import yaml
import requests

def get_data_from_url_requests():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    url = config["url"]
    # requests ライブラリを使用
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_data_from_url_requests()
