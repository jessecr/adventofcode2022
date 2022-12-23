DIRECTIONS = 'RDLU'
DIRECTION_OFFSETS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}


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


def get_next_cell_in_direction(board, cell, direction):
    r_offset, c_offset = DIRECTION_OFFSETS[direction]
    next_cell = cell[0] + r_offset, cell[1] + c_offset
    if next_cell not in board:
        r, c = cell
        if direction == 'R':
            c = col_bounds[r][0]
        elif direction == 'L':
            c = col_bounds[r][1]
        elif direction == 'U':
            r = row_bounds[c][1]
        else:
            r = row_bounds[c][0]
        next_cell = (r, c)

    return next_cell


board = {}
row_bounds = {}
col_bounds = {}
with open('input.txt', 'r') as fd:
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


movement = []
pos = [0, col_bounds[0][0]]
facing = 'R'

for step in get_steps(steps_str.strip()):
    if step in ('R', 'L'):
        facing = get_next_direction(facing, step)
    else:
        for _ in range(step):
            next_cell = get_next_cell_in_direction(board, pos, facing)
            if board[next_cell] == '#':
                break
            pos = next_cell
            movement.append((pos, facing))

print(pos, facing, (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + DIRECTIONS.index(facing))
