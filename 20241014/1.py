s = input()
sett = set()
a = set()
end_elem = ''

while s:
    a = s.split()
    if end_elem:
        sett.add(frozenset((end_elem, a[0])))
    for i in range(0, len(a)-1):
        sett.add(frozenset((a[i], a[i+1])))
    else:
        end_elem = a[-1]
    s = input()

print(len(sett))