import math

def ssqrt(a):
    for i in range(2, int(math.sqrt(a))):
        for j in range(2, int(math.log2(a))):
            if i**j == a:
                return "YES"
    return "NO"

a = int(input())
print(ssqrt(a))

