import math

seq = set(eval(input()))

M = max(seq)

sums_of_three_squares = set()

for i in range(1, int(math.sqrt(M)) + 1):
    i2 = i * i
    for j in range(i, int(math.sqrt(M - i2)) + 1):
        j2 = j * j
        for k in range(j, int(math.sqrt(M - i2 - j2)) + 1):
            k2 = k * k
            sum_of_squares = i2 + j2 + k2
            if sum_of_squares <= M:
                sums_of_three_squares.add(sum_of_squares)

inter = seq.intersection(sums_of_three_squares)
print(len(inter))
