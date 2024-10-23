import re, sys

s = input()
flag = 0
maxx = -sys.maxsize - 1
while s:
    lst = re.split(r'\s+', s)
    for i in lst:
        if i and i[0] == '-' and i[1:].isnumeric() or i.isnumeric():
            maxx = max(maxx, int(i))
            flag = 1
    s = input()
if flag:
    print(maxx)
else:
    print(0)