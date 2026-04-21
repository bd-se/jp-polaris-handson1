import yaml

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.Loader)


import requests

r = requests.get(config["url"])

あまりたのしくない
