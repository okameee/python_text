#スクレイピング(scraping)
#インターネットから必要な情報を大量に取得(そして整理)すること

#使うライブラリ
#requests httpリクエストをすることができる標準ライブラリ
#beautifulsoup4 requestsによって得られたhtmlスクリプトを解析できる
#selenium ブラウザ操作を自動化できる(bs4のように解析もできる)


#効果音ラボから素材ファイルをダウンロードするプログラムを作りたい
#とりあえず戦闘効果音を全てDLしてみる

import requests
from bs4 import BeautifulSoup
target_url = "https://soundeffect-lab.info/sound/battle/"
res = requests.get(target_url)
soup = BeautifulSoup(res.content.decode("utf-8"), "lxml") #parser(解析器)を選択、今回はlxmlを指定
sl = soup.find("div", id="sl")
sr = soup.find("div", id="sr")

li_list = sl.find_all("li") + sr.find_all("li")

url_list = [target_url+i.find("a")["href"] for i in li_list]
for url in url_list:
    print(url)
    #download this mp3 data


"""-------------------------------------------------------------------------------------------"""
#get, post


"""-------------------------------------------------------------------------------------------"""
#cookie