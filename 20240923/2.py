from collections import deque
def sravni(tup1, tup2):
    if (tup1[0] == tup2[0] and (tup1[1] == tup2[1] and tup1[2] == tup2[2] or
            tup1[1] == tup2[2] and tup1[2] == tup2[1])):
            return False
    elif (tup1[0] == tup2[1] and (tup1[1] == tup2[0] and tup1[2] == tup2[2] or
            tup1[1] == tup2[2] and tup1[2] == tup2[0])):
            return False
    elif (tup1[0] == tup2[2] and (tup1[1] == tup2[0] and tup1[2] == tup2[1] or
            tup1[1] == tup2[1] and tup1[2] == tup2[0])):
            return False

    if (tup1[0] <= tup2[0] and (tup1[1] <= tup2[1] and tup1[2] <= tup2[2] or
            tup1[1] <= tup2[2] and tup1[2] <= tup2[1])):
            return True
    elif (tup1[0] <= tup2[1] and (tup1[1] <= tup2[0] and tup1[2] <= tup2[2] or
            tup1[1] <= tup2[2] and tup1[2] <= tup2[0])):
            return True
    elif (tup1[0] <= tup2[2] and (tup1[1] <= tup2[0] and tup1[2] <= tup2[1] or
            tup1[1] <= tup2[1] and tup1[2] <= tup2[0])):
            return True
    else:
        return False

def found_max(ind_start):
    for i in range(ind_start, len(box)):
        for j in range(ind_start, len(box)):
            if i != j and sravni(box[i], box[j]):
                break
        else:
            return i

s = input()
box = []

while s:
    box.append(tuple(eval(s)))
    s = input()

for i in range(len(box)):
    ind = found_max(i)
    if ind:
        a = box[ind]
        del box[ind]
        box.insert(i, a)

for item in box:
    print (*item, sep=", ")