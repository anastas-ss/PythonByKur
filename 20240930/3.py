def BinPow(a, n, f):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        b = BinPow(a, n // 2, f)
        return f(b, b)
    else:
        return f(a, BinPow(a, n - 1, f))


