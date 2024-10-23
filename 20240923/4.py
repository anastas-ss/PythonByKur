s = input().split(',')
n, a = len(s), []
a.append(s)

for _ in range(n-1):
    s = input().split(',')
    a.append(s)

for i in range(len(a)):
    column = []
    for j in range(i + 1):
        column.append(a[i - j][i])
    print(*a[i][:i], *column, sep=',')
