def distance(coord1, coord2):
    return (coord1[0] - coord2[0]) * (coord1[0] - coord2[0]) + (coord1[1] - coord2[1]) * (coord1[1] - coord2[1]) + (coord1[2] - coord2[2]) * (coord1[2] - coord2[2])

galaxies = dict()
s = input()

while s and s != '.':
    parts = s.split()
    x, y, z = map(float, parts[:3])
    name = parts[3]
    galaxies[(x, y, z)] = name
    s = input()

galaxy_uniq = list(galaxies.keys())
max_distance = -1
farthest_pair = set()

for elem in galaxy_uniq:
    for elem2 in galaxy_uniq:
        name1 = galaxies[elem]
        name2 = galaxies[elem2]
        dist = distance(elem, elem2)
        if dist > max_distance:
            max_distance = dist
            farthest_pair = (name1, name2)

print(*sorted(farthest_pair))
