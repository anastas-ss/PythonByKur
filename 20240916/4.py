max_count = count = 1
a = int(input())

while a != 0:
    b = int(input())
    if b != 0 and a <= b:
        count += 1
    else:
        max_count = max(count, max_count)
        count = 1
    a = b
print(max_count)