def f(p1, p2, p):
    return 1 if (p1[0] - p[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p1[1] - p[1]) > 0 else -1

def in_triange(t, p):
    sign = f(t[0], t[1], p)
    return f(t[1], t[2], p) == sign and f(t[2], t[0], p) == sign

def check(points):
    n = len(points)
    for p1 in range(n):
        for p in range(n):
            if p == p1 or p == (p1 + 1) % n or p == (p1 + 2) % n:
                continue
            if in_triange((points[p1], points[(p1 + 1) % n], points[(p1 + 2) % n]), points[p]):
                return False
    return True


s = input()
lst = []
while s:
    lst.append(eval(s))
    s = input()
print(check(lst))

