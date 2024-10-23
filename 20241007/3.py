def squares(w, h, *args):
    arr = [['.' for _ in range(w)] for _ in range(h)]

    for arg in args:
        x, y, s, c = arg
        for i in range(s):
            for j in range(s):
                if 0 <= x + i < h and 0 <= y + j < w:
                    arr[y + j][x + i] = c

    for row in arr:
        print(''.join(row))
