import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
with urlopen("https://coinpost.jp/") as res:
        html = res.read().decode("utf-8")

# 2. BeautifulSoupでHTMLを読み込む
soup = BeautifulSoup(html, "html.parser")

# 3. 記事一覧を取得する class="htr-title"
items = soup.select(".htr-title")

# 4. ランダムに1件取得する
shuffle(items)
item = items[0]
item1 = item.get_text()
print(item1)
