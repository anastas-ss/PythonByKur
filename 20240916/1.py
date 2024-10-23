import math
a, b, c = eval(input())
box = []
#t = x^2

if a == 0:
    if b != 0:
        if -c / b < 0:
            print(0)
        elif -c / b == 0:
            print(0.0)
        else:
            print(-math.sqrt(-c / b), math.sqrt(-c / b))
    elif b == 0 and c == 0:
        print(-1)
    else:
        print(0)
else:
    d = b**2 - 4*a*c
    if d == 0:
        if -b / (2 * a) < 0:
            print(0)
        elif -b / (2 * a) == 0:
            print(0.0)
        else:
            print(-math.sqrt(-b / (2 * a)), math.sqrt(-b / (2 * a)))
    elif d > 0:
        t1 = (-b + math.sqrt(d))/(2 * a)
        t2 = (-b - math.sqrt(d))/(2 * a)
        if t1 > 0:
            box.append(-math.sqrt(t1))
            box.append(math.sqrt(t1))
        elif t1 == 0:
            box.append(0.0)
        if t2 > 0:
            box.append(-math.sqrt(t2))
            box.append(math.sqrt(t2))
        elif t2 == 0:
            box.append(0.0)
        if t1 < 0 and t2 < 0:
            print(0)
        box = list(set(box))
        box.sort()
        print(*box, sep=" ")
    else:
        print(0)
