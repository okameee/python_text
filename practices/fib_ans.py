#1. 変数を変化させる
def fib1(a1, a2, n):
    if n == 1:
        return [a1]
    elif n == 2:
        return [a1, a2]

    result = [a1, a2]
    for _ in range(n-2):
        a1, a2 = a2, a1+a2
        result.append(a2)
    return result

#2. 再帰関数
def fib2(a1, a2, n):
    def func(a1, a2, n):
        result.append(a2)
        if n!=2:
            func(a2, a1+a2, n-1)

    if n == 1:
        result = [a1]
    elif n == 2:
        result = [a1, a2]
    else:
        result = [a1, a2]
        func(a2, a1+a2, n-1)

    return result

#3. 一般項の公式項
def fib3(a1, a2, n):
    result = []
    fai1 = (1+5**0.5)/2
    fai2 = (1-5**0.5)/2
    def general_term(a1, a2, n):
        return int(((a2-fai2*a1)*fai1**(n-1) - (a2-fai1*a1)*fai2**(n-1)) / 5**0.5)

    for i in range(1, n+1):
        result.append(general_term(a1, a2, i))
    return result