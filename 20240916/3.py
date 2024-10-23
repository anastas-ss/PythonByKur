s = input()
x, y, z = eval(s)

xmin = xmax = x
ymin = ymax = y
zmin = zmax = z

s = input()
while s:
    x, y, z = eval(s)
    if x > xmax:
        xmax = x
    if x < xmin:
        xmin = x
    if y > ymax:
        ymax = y
    if y < ymin:
        ymin = y
    if z > zmax:
        zmax = z
    if z < zmin:
        zmin = z
    s = input()
print((xmax-xmin)*(ymax-ymin)*(zmax-zmin))

##