#if文
#条件分岐をすることができる(状況に応じて処理を変える)
#条件式がTrueの場合にインデント以降の処理が行われる


"""-------------------------------------------------------------------------------------------"""
#例(おみくじの結果(result)が大吉なら"大当たり！大吉！"と表示)
result = "大吉"
if result == "大吉":
    print("大当たり！大吉！")

#resultが"中吉"や"凶"、"hogehoge"だとprintは実行されない


"""-------------------------------------------------------------------------------------------"""
#elif
#if文で条件を追加したいとき
result = "中吉"
if result == "大吉":
    print("大当たり！大吉！")
elif result == "中吉":
    print("当たり。中吉")

#こうすると大吉ではない場合に、さらに中吉かどうかの判定がされる
#elifは好きなだけ追加できる


"""-------------------------------------------------------------------------------------------"""
#else
#どの条件式にも当てはまらなかった場合の処理を追加したいとき(デフォルトの処理を追加したいとき)
result = "凶"
if result == "大吉":
    print("大当たり！大吉！")
elif result == "中吉":
    print("当たり。中吉")
else:
    print("来年に期待")
#こうすると大吉でも中吉でもなかった場合、"来年に期待"が表示される
#elseは条件文の一番最後に記述する