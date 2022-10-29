#with文: 安全にファイルの読み書きをすることができる
#前処理(__enter__)、後処理(__exit__)を暗黙的に呼び出すことでファイルの閉じ忘れを防ぐ

#ワーキングディレクトリをこのファイルのディレクトリと同じにする
#相対パスを使えるようにする
import os
os.chdir(os.path.dirname(__file__))

#test.txtをreadモードでopenし、fという名前で変数を保持する
with open("test.txt", "r") as f:
    data = f.read()
    # print(data)

#エラー
# f.read()

with open("test.txt", "w") as f:
    text = "new text"
    f.write(text)

#"b"をつけることでバイナリファイルを扱えるようになる
with open("data.dat", "rb") as f:
    data = f.read()
    # print(data)


with open("data.dat", "wb") as f:
    data = bytes("new byte data", encoding="utf-8")
    f.write(data)