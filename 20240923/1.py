s = input()

matrix = [[0 for _ in range(101)] for _ in range(101)]
#print(matrix)

while s:
    a, b = eval(s)
    matrix[a][b] += 1
    s = input()

for i in range(1, 101):
    for j in range(1, 101):
        for _ in range(matrix[i][j]):
            print(i, j, sep=', ')
