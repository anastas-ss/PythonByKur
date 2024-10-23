def turtle(coord, direction):
    x, y = coord
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while True:
        command = yield (x, y)
        if command == 'f':
            dx, dy = directions[direction]
            x += dx
            y += dy
        elif command == 'l':
            direction = (direction + 1) % 4
        elif command == 'r':
            direction = (direction - 1) % 4