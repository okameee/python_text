#while文
#繰り返し処理をしたいときに使う
#条件式がTrueである間ずっと処理を繰り返す


"""-------------------------------------------------------------------------------------------"""
#例(1から100まで数字を表示)
n = 1
while n <= 100:
    print(n)
    n += 1

#1. n=100のとき、条件式はギリギリTrueなので処理が行われる
#2. 100が表示され、nは101になる
#3. n=101のとき、条件式はFalseになって処理が終了する(101は表示されない)


"""-------------------------------------------------------------------------------------------"""
#無限ループとbreak
# while True:
#     print("無限ループ")

#このように描くと条件式が常にTrueになる(当たり前)
#処理が終了せず、"無限ループ"が延々と表示される

#break文を使うと強制的にwhileループを抜け出すことができる
while True:
    ans = input("quitで終了します：\n> ")
    if ans == "quit":
        break
print("終了しました")

#ちなみにもっとコードを短くすると：
#1. ansを使わないで書く
while True:
    if input("quitで終了します：\n> ") == "quit":
        break
print("終了しました")

#2. quitでないならばずっとループする、に書き換える
while input("quitで終了します：\n> ") != "quit":
    pass
print("終了しました")