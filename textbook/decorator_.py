#デコレータ(decorator)
#関数の一行上に@デコレータ名とすることで関数を修飾することができる

def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('--end--')
    return wrapper


@deco
def sayhello():
    print("Hello")

sayhello()
print(sayhello.__name__) # -> "wrapper"に置き換わっていることが分かる

"""-------------------------------------------------------------------------------------------"""
#classmethodとstaticmethod
#classmethod：Util.メソッドでアクセスできる(インスタンス化しないで呼び出せる)。慣例的にクラス変数はclsと記述する
#staticmethod；メソッド内ではインスタンス変数にはアクセスしないときに使う。(classmethod同様インスタンス化しないで呼び出せる)

#色々な関数をまとめたUtilクラス
class Util:
    cls_var = "cls_var"

    @classmethod
    def show_clsvar(cls):
        print(cls.cls_var)

    @staticmethod
    def util1():
        print("util1")

    @staticmethod
    def util2():
        print("util2")

    def util3(self):
        print("util3")

#全部正しい
Util.show_clsvar()
Util().show_clsvar()
Util().util1()
Util.util2()

#staticmethodのメリット
#メソッド呼び出し時にインタプリタによって生成されるBoundオブジェクトを作らないため、高速
#実際はあまり使いどころのないデコレータ

def util2(): pass
print(type(Util.util2))
print(type(Util().util3))
print(type(util2))