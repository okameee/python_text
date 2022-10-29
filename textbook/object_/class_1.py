#pythonにおいて全てのオブジェクトは何かしらのクラスのインスタンスである
#100はint型のインスタンスであり、"hello"はstr型のインスタンスである


"""-------------------------------------------------------------------------------------------"""
#オブジェクト指向
#オブジェクト指向とは、オブジェクトが持つデータとメッセージのやり取りで世界を表現しようとするプログラミングパラダイムである
#クラスとインスタンスの概念はオブジェクト指向の根幹となる重要な考え方
#特にpythonでは全てをオブジェクトとして捉えているため、クラスについての理解は非常に重要である

#ちなみにpythonはオブジェクト指向型言語だが他には
#宣言型言語
#関数型言語
#手続き型言語
#などがある


"""-------------------------------------------------------------------------------------------"""
#class: 自分で定義するオブジェクトのこと
#通常クラス名はキャメルケースで命名する

class TestClass:
    def say_smthing(self, msg):
        print("I say {}".format(msg))

testclass = TestClass() #TestClassのインスタンスを生成
testclass.say_smthing("Bullshit") #TestClassのsay_smthingメソッドを呼び出す


"""-------------------------------------------------------------------------------------------"""
#self
#pythonではclassのメソッドの第一引数には必ず「オブジェクト自身(self)」を指定することになっている
#オブジェクト自身を表す変数名として慣習的にselfが使われている。(つまりs_e_l_fだろうがmeだろうが動作はする)

class Ship:
    #メソッド内でselfを使わない場合もselfを書く必要がある(ただしデコレータを使う方法がある)
    def run(self):
        print("brrrrrr")

    def set_color(self, color):
        self.color = color

    def show_color(self):
        print(f"this ship's color is {self.color}")

ship = Ship()
ship.set_color("red")
ship.show_color()


"""-------------------------------------------------------------------------------------------"""
#継承
#親クラスのメソッド、変数を引き継ぐことができる
#super()で親クラスのメソッドにアクセスできる
#ちなみに全てのクラスはobjectクラスの子クラス

class Worker(object): #class Worker: と同じ
    def __init__(self, money):
        self.money = money

    def do_work(self):
        self.money += 1

    def show_money(self):
        print(f"I have {self.money} bucks.")

class CEO(Worker):
    def __init__(self, money):
        super().__init__(money)
        self.money += 100 #Bonus!

    def do_work(self):
        self.money += 10

サラリーマン = Worker(10) #ちなみに日本語も変数名に使ってよい
サラリーマン.do_work()
サラリーマン.show_money()

ceo = CEO(10)
ceo.do_work()
ceo.do_work()
ceo.show_money() #CEOクラス内ではshow_money()は定義していないが呼び出すことができる



"""-------------------------------------------------------------------------------------------"""
#ダンダ―メソッド
#double under -> ダンダー
#__init__(): インスタンス生成時に一番最初に呼ばれるメソッド
#__eq__(): ==によって比較されたときに呼ばれるメソッド
#__call__(): self()を実行しようとしたときに呼ばれるメソッド
#__del__(): del文でオブジェクトが破壊されたときに呼ばれる。
#__len__(): len()が実行された時に呼ばれる
#__iter__(): iter()によって呼ばれる。iterableなオブジェクトを作るときはこのメソッドを書く必要がある
#__next__(): next()によって呼ばれる
#__repr__(): オブジェクトを説明する文字列を返す


class MyClass:
    def __init__(self, msg=""):
        self.msg = msg

    def __eq__(self, other):
        return True #このクラスのインスタンスは常に等価であると判断される

    def __len__(self):
        return len(self.msg)

obj1 = MyClass()
obj2 = "obj2"

print(obj1==obj2)


"""-------------------------------------------------------------------------------------------"""
#クラス変数とインスタンス変数

#クラス変数は全てのインスタンス間で共有される変数
#クラス名.クラス変数名 or インスタンス名.__class__.クラス変数名でアクセスできる

#インスタンス変数はインスタンス間で値を共有しない変数。
#self. で定義する

class SampleClass:
    class_var = "class variable not changed"

    def __init__(self):
        self.instance_var = "instance variable not chagned"

sample1 = SampleClass()
sample2 = SampleClass()

SampleClass.class_var = "class variable chagned" #全てのインスタンスに影響する
print(sample1.class_var)

sample1.instance_var = "instance variable changed" #sample1以外のインスタンスの値は変わらない
print(sample2.instance_var)