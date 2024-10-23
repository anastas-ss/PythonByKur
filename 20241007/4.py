from decimal import Decimal, getcontext

def calc_pi(n=2000):
    getcontext().prec = n
    pi = Decimal(0)
    k = Decimal(0)
    while True:
        term = (Decimal(1) / (16 ** k)) * ((Decimal(4) / (8 * k + 1)) -
                                           (Decimal(2) / (8 * k + 4)) -
                                           (Decimal(1) / (8 * k + 5)) -
                                           (Decimal(1) / (8 * k + 6)))
        pi += Decimal(term)
        if k >= 1000:
            break
        k += 1
    return pi

def sin(x, acc=2000):
    sine = Decimal(x)
    x_squared = Decimal(x * x)
    term = Decimal(x)
    sign = Decimal(-1)
    for n in range(3, acc * 2, 2):
        term *= Decimal(x_squared / Decimal((n - 1) * n))
        sine += Decimal(sign * term)
        sign = -sign
    return sine

def cos(x, acc=2000):
    cosine = Decimal(1)
    x_squared = Decimal(x * x)
    term = Decimal(1)
    sign = Decimal(-1)
    for n in range(2, acc * 2, 2):
        term *= Decimal(x_squared / Decimal((n - 1) * n))
        cosine += Decimal(sign * term)
        sign = -sign
    return cosine

def tan(x, n, acc):
    sinus = Decimal(sin(x, n))
    cosinus = Decimal(cos(x, n))
    getcontext().prec = acc
    return Decimal(sinus / cosinus)

alpha_rad = Decimal(input())
t = int(input())
alpha = alpha_rad*Decimal(calc_pi()/200)
getcontext().prec = 2000
print(tan(alpha, 2000, t))
