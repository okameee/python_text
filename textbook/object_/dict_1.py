#dict(辞書)型: keyとvalueによってデータを管理する
#アクセス: dictの後ろに[key]を使う
capitals = {
    "US":"Washington D.C.",
    "JP":"Tokyo",
    "KR":"Seoul"
}
#capitals["JP"] -> "Tokyo"


"""-------------------------------------------------------------------------------------------"""
user1 = {
    "name":"maezawa",
    "age":19,
    "nation":"Japan"
}

user2 = {
    "name":"baiden",
    "age":4,
    "nation":"USA"
}

color1 = {
    "red":(255, 0, 0),
    "green":(0, 255, 0),
    "blue":(0, 0, 255)
}

color2 = {
    "black":(0, 0, 0),
    "white":(255, 255, 255)
}


"""-------------------------------------------------------------------------------------------"""
#dictのメソッド
#---get(): dict[key]と同じ。keyが存在しなかった場合にNoneを返してくれる。第二引数にデフォルト値を設定することもできる

#---keys(): dictが持つ全てのkeyを配列にして返す。(注：返り値はdict_keys。list型ではない)
#---values(): dictが持つ全てのvalueを配列にして返す。(注：返り値はdict_values)
#---items(): dictが持つ全てのkeyとvaluenのtupleを要素とした配列を返す。 (注：返り値はditc_items)
#---update(): dict同士を結合する。


"""-------------------------------------------------------------------------------------------"""
#dict型による条件分岐
flag = True

#1. if文を使った条件分岐
if flag:
    print("YESSSS")
else:
    print("NOOOO")

#2. dictを使った条件分岐(条件式をkeyに、対応する値をvalueに格納したdictを用いた場合)
conditions = {
    True: "YESSS",
    False: "NOOOO",
}
print(conditions[flag])


"""-------------------------------------------------------------------------------------------"""
#内包表記は辞書型にもある


#https://note.nkmk.me/python-dict-create/