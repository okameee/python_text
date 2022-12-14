

#in: 比較演算子
#listに要素が含まれているかを調べることができる
if "find me" in ["hello world", "good morning", "find me", "good bye"]:
    print("Gocha!")


"""-------------------------------------------------------------------------------------------"""
#and, or: ブール演算子
#いわずもがな。
nums = [3, 6, 9]
print(min(nums)==3 and max(nums)==9) #->True


"""-------------------------------------------------------------------------------------------"""
#not
#いわずもがな。論理値を反転する
age = 20
if not age == 20: #if age != 20 とも書ける
    print("you are not 20")


"""-------------------------------------------------------------------------------------------"""
#is, ==
#"is"はオブジェクトの同一性の比較、"=="はオブジェクトが等価であるかの比較をする
#例:
l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 is l2) # -> False
print(l1 == l2) # -> True

#isはid(obj)によるid番号を比較している
#==はオブジェクトの__eq__()による評価を行っている