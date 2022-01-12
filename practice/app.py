import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():

# **** ここを実装します（基礎課題） ****

    """COINPOSTから記事を入手して、ランダムに1件返却します."""
# 1. はてブのホットエントリーページのHTMLを取得する
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
    return json.dumps({
        "content" : item1
        # "link": item.get('href')
    })


if __name__ == "__main__":
    app.run(debug=True, port=5004)
