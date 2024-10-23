def SpiralDigits(n, m):
    matrix = [[-1 for _ in range(m)] for _ in range(n)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0
    x, y = 0, 0

    for num in range(n * m):
        matrix[x][y] = num % 10

        next_x = x + direction[dir_index][0]
        next_y = y + direction[dir_index][1]

        if (0 <= next_x < n and 0 <= next_y < m and matrix[next_x][next_y] == -1):
            x, y = next_x, next_y
        else:
            dir_index = (dir_index + 1) % 4
            x += direction[dir_index][0]
            y += direction[dir_index][1]

    return matrix

M, N = eval(input())
matrix = SpiralDigits(N, M)
for row in matrix:
    print(*row)