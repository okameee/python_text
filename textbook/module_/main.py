#モジュールとパッケージ
#モジュール：ファイル
#パッケージ：フォルダ(モジュール群)
#パッケージをimportするときは__init__.pyを使うことができる

import module as m #as節で任意のモジュール名に

#packageからguiだけをimport
from package import gui

#moduleのadd関数を呼び出し
x = m.add(3, 9)
app = gui.App()


"""-------------------------------------------------------------------------------------------"""
#__init__.py