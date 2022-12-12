import numpy as np
from queue import PriorityQueue


def get_adjacent_cells(shape, row, col):
    for ro, co in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= row + ro < shape[0] and 0 <= col + co < shape[1]:
            yield row + ro, col + co


def get_cost(grid, src, dest, limit_direction):
    assert limit_direction in ('up', 'down')

    src_val = grid[src]
    dest_val = grid[dest]
    if limit_direction == 'up' and dest_val > src_val + 1:
        return np.inf
    elif limit_direction == 'down' and dest_val < src_val - 1:
        return np.inf
    return 1


def calculate_distances(grid, start, limit_direction):
    distances = np.ones(grid.shape) * np.inf
    distances[start] = 0

    visited = set()
    unvisited = PriorityQueue()
    unvisited.put((0, start))
    while not unvisited.empty():
        p, cell = unvisited.get()
        for neighbor in get_adjacent_cells(grid.shape, cell[0], cell[1]):
            if neighbor not in visited:
                new_dist = distances[cell] + get_cost(grid, cell, neighbor, limit_direction)
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    unvisited.put((new_dist, neighbor))

        visited.add(cell)

    return distances


fname = 'example_input.txt'
fname = 'input.txt'

rows = []
start = end = None
with open(fname, 'r') as fd:
    for i, line in enumerate(fd):
        if 'S' in line:
            start = (i, line.index('S'))
            line = line.replace('S', 'a')
        if 'E' in line:
            end = (i, line.index('E'))
            line = line.replace('E', 'z')
        rows.append(list(map(ord, line.strip())))

grid = np.array(rows)

print('Part 1:', int(calculate_distances(grid, start, 'up')[end]))
shortest = calculate_distances(grid, end, 'down')[grid == ord('a')].min()
print('Part 2:', int(shortest))
