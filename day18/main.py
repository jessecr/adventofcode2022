from collections import deque


def get_adjacent_cells(c):
    for offset in (-1, 0, 1):
        yield c[0] + offset, c[1], c[2]
        yield c[0], c[1] + offset, c[2]
        yield c[0], c[1], c[2] + offset


def part_1(coords):
    p1 = 0
    for coord in coords:
        for adj in get_adjacent_cells(coord):
            if adj not in coords:
                p1 += 1
    return p1


def part_2(coords):
    x_coords = sorted(c[0] for c in coords)
    y_coords = sorted(c[1] for c in coords)
    z_coords = sorted(c[2] for c in coords)
    min_x, max_x = x_coords[0] - 1, x_coords[-1] + 1
    min_y, max_y = y_coords[0] - 1, y_coords[-1] + 1
    min_z, max_z = z_coords[0] - 1, z_coords[-1] + 1

    q = deque([(min_x, min_y, min_z)])
    seen = set()
    p2 = 0
    while q:
        coord = q.popleft()
        if coord in seen:
            continue
        x, y, z = coord
        if min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z:
            for adj in get_adjacent_cells((x, y, z)):
                if adj in coords:
                    p2 += 1
                else:
                    q.append(adj)

        seen.add(coord)

    return p2


with open('input.txt', 'r') as fd:
    coords = [tuple(map(int, line.split(','))) for line in fd.read().splitlines()]

print('Part 1:', part_1(coords))
print('Part 2:', part_2(coords))
