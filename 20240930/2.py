def divdigit(N):
    box = [int(i) for i in str(N)]
    count = 0
    for elem in box:
        if elem and N % elem == 0:
            count += 1

    return count
