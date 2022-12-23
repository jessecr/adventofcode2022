DIRECTIONS = 'RDLU'
OPPOSITE_DIRECTIONS = {'L': 'R', 'U': 'D', 'R': 'L', 'D': 'U'}
BOUNDARIES_MATCH = {'R': 'U', 'D': 'L', 'L': 'D', 'U': 'R'}
DIRECTION_OFFSETS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
SIDE_BOUNDS_EXAMPLE = (
    ((0, 8), (3, 11)),
    ((4, 0), (7, 3)),
    ((4, 4), (7, 7)),
    ((4, 8), (7, 11)),
    ((8, 8), (11, 11)),
    ((8, 12), (11, 15))
)
SIDE_BOUNDS = (
    ((0, 50), (49, 99)),
    ((0, 100), (49, 149)),
    ((50, 50), (99, 99)),
    ((100, 0), (149, 49)),
    ((100, 50), (149, 99)),
    ((150, 0), (199, 49)),
)
DIRECTION_CHANGES_EXAMPLE = {
    1: {'L': (3, 'D'), 'U': (2, 'D'), 'R': (6, 'L'), 'D': (4, 'D')},
    2: {'L': (6, 'U'), 'U': (1, 'D'), 'R': (3, 'R'), 'D': (5, 'U')},
    3: {'L': (2, 'L'), 'U': (1, 'R'), 'R': (4, 'R'), 'D': (5, 'R')},
    4: {'L': (3, 'L'), 'U': (1, 'U'), 'R': (6, 'D'), 'D': (5, 'D')},
    5: {'L': (3, 'U'), 'U': (4, 'U'), 'R': (6, 'R'), 'D': (2, 'U')},
    6: {'L': (5, 'L'), 'U': (4, 'L'), 'R': (1, 'L'), 'D': (2, 'R')}
}
DIRECTION_CHANGES = {
    1: {'L': (4, 'R'), 'U': (6, 'R'), 'R': (2, 'R'), 'D': (3, 'D')},
    2: {'L': (1, 'L'), 'U': (6, 'U'), 'R': (5, 'L'), 'D': (3, 'L')},
    3: {'L': (4, 'D'), 'U': (1, 'U'), 'R': (2, 'U'), 'D': (5, 'D')},
    4: {'L': (1, 'R'), 'U': (3, 'R'), 'R': (5, 'R'), 'D': (6, 'D')},
    5: {'L': (4, 'L'), 'U': (3, 'U'), 'R': (2, 'L'), 'D': (6, 'L')},
    6: {'L': (1, 'D'), 'U': (4, 'U'), 'R': (5, 'U'), 'D': (2, 'D')}
}

IS_EXAMPLE = False


def get_next_direction(facing, rotation):
    idx = DIRECTIONS.index(facing)
    offset = 1 if rotation == 'R' else -1
    return DIRECTIONS[(idx + offset) % 4]


def get_steps(step_str):
    s = e = 0
    while e < len(step_str):
        if step_str[s] in 'LR':
            yield step_str[s]
            s = e = e + 1
        elif step_str[e] in 'LR':
            yield int(step_str[s:e])
            s = e
        else:
            e += 1

    if e > s:
        yield int(step_str[s:e])


def get_side_if_on_boundary(cell, direction):
    side_bounds = SIDE_BOUNDS_EXAMPLE if IS_EXAMPLE else SIDE_BOUNDS
    r, c = cell
    for i, ((r0, c0), (r1, c1)) in enumerate(side_bounds):
        if direction == 'L' and c == c0 and r0 <= r <= r1:
            return i + 1
        elif direction == 'U' and r == r0 and c0 <= c <= c1:
            return i + 1
        elif direction == 'R' and c == c1 and r0 <= r <= r1:
            return i + 1
        elif direction == 'D' and r == r1 and c0 <= c <= c1:
            return i + 1

    return None


def get_boundary_cells(side, direction):
    side_bounds = SIDE_BOUNDS_EXAMPLE if IS_EXAMPLE else SIDE_BOUNDS
    (r0, c0), (r1, c1) = side_bounds[side - 1]
    if direction == 'U':
        return [(r0, c) for c in range(c0, c1 + 1)]
    if direction == 'R':
        return [(r, c1) for r in range(r0, r1 + 1)]
    if direction == 'D':
        return [(r1, c) for c in range(c0, c1 + 1)]
    if direction == 'L':
        return [(r, c0) for r in range(r0, r1 + 1)]


def get_cell_position_on_new_side(cell, side, direction, next_side, next_direction):
    src_boundary = get_boundary_cells(side, direction)
    dest_boundary = get_boundary_cells(next_side, OPPOSITE_DIRECTIONS[next_direction])
    if direction == next_direction or BOUNDARIES_MATCH[direction] == next_direction:
        return dest_boundary[src_boundary.index(cell)]
    return dest_boundary[len(dest_boundary) - src_boundary.index(cell) - 1]


def get_next_cell_and_direction(board, cell, direction):
    side = get_side_if_on_boundary(cell, direction)
    if not side:
        # Still on the same side so just move one cell
        r_offset, c_offset = DIRECTION_OFFSETS[direction]
        return (cell[0] + r_offset, cell[1] + c_offset), direction

    direction_changes = DIRECTION_CHANGES_EXAMPLE if IS_EXAMPLE else DIRECTION_CHANGES
    next_side, next_direction = direction_changes[side][direction]
    next_cell = get_cell_position_on_new_side(cell, side, direction, next_side, next_direction)

    return next_cell, next_direction


board = {}
row_bounds = {}
col_bounds = {}
fname = 'example_input.txt' if IS_EXAMPLE else 'input.txt'
with open(fname, 'r') as fd:
    board_str, steps_str = fd.read().split('\n\n')
    for r, row in enumerate(board_str.splitlines()):
        for c, v in enumerate(row):
            if v == ' ':
                continue
            cell = (r, c)
            if c not in row_bounds:
                row_bounds[c] = [r, r]
            else:
                row_bounds[c][1] = r
            if r not in col_bounds:
                col_bounds[r] = [c, c]
            else:
                col_bounds[r][1] = c
            board[cell] = v


pos = (0, col_bounds[0][0])
facing = 'R'
movement = [(pos, facing)]

for step in get_steps(steps_str.strip()):
    if step in ('R', 'L'):
        facing = get_next_direction(facing, step)
        movement.append((pos, facing))
    else:
        for _ in range(step):
            next_cell, next_facing = get_next_cell_and_direction(board, pos, facing)
            if board[next_cell] == '#':
                break
            pos = next_cell
            facing = next_facing
            movement.append((pos, facing))

print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + DIRECTIONS.index(facing))
