#オブジェクトのカプセル化
#関連するデータ、メソッドをまとめて一つ(カプセル)にすること
#外部に対して必要なデータやメソッドのみを提供すること


"""-------------------------------------------------------------------------------------------"""
#pythonでは内部のみで使う変数・メソッドは、慣習的に頭に_をつけて命名する
#ただし実際にはアクセスすることができる
#ちなみに_をつけた変数はfrom import * ではimportされない

#何かをダウンロードするクラス
class Downloader:
    def download(self, url):
        print(f"Download: {url}")
        self._cache = "cache" #何かのキャッシュ変数
        self._get_filename()
        self._write_file()

    def _get_filename(self):
        return "File Name"

    def _write_file(self):
        print("Writing File")

dl = Downloader()
dl.download("url url url")
# dl._get_filename() -> エラーにはならないが、プログラマはこのメソッドの外部利用を意図していない

"""-------------------------------------------------------------------------------------------"""
#ネームマングリング
#カプセル化に関して、pythonではネームマングリング(:名前修飾)という機能がある

class HogeHoge:
    _dummy_prv = "hoge"
    __almost_prv = "hoge"

hogehoge = HogeHoge()

# 丸見え
a = hogehoge._dummy_prv

# エラー
b = hogehoge.__almost_prv

# こうすると見えちゃう
c = hogehoge._HogeHoge__almost_prv

#https://qiita.com/mounntainn/items/e3fb1a5757c9cf7ded63