direction_guide = {'R': (1, 1), 'L': (1, -1), 'U': (0, 1), 'D': (0, -1)}


def update_knot(to_update, target):
    adjacent = abs(target[0] - to_update[0]) <= 1 and abs(target[1] - to_update[1]) <= 1
    if target == to_update or adjacent:
        return

    row_diff = abs(target[0] - to_update[0])
    col_diff = abs(target[1] - to_update[1])

    # Align with the axis that the knot is offset once from, if any.
    if row_diff and col_diff:
        if row_diff == 1:
            to_update[0] = target[0]
        elif col_diff == 1:
            to_update[1] = target[1]

    # Move one towards target knot in any axis that the knot is offset twice from, if any.
    if row_diff == 2:
        offset = 1 if to_update[0] < target[0] else -1
        to_update[0] += offset
    if col_diff == 2:
        offset = 1 if to_update[1] < target[1] else -1
        to_update[1] += offset


def solve(num_knots, cmds):
    knots = [[0, 0] for _ in range(num_knots)]
    visited = {(0, 0)}
    for direction, count in cmds:
        for i in range(count):
            idx, amt = direction_guide[direction]
            knots[0][idx] += amt

            for i in range(1, len(knots)):
                update_knot(knots[i], knots[i - 1])

            visited.add(tuple(knots[-1]))

    return len(visited)


fname = 'example_input'
fname = 'input'

cmds = []
with open(fname, 'r') as fd:
    for line in fd:
        a, b = line.split()
        cmds.append((a, int(b)))

print('Part 1:', solve(2, cmds))
print('Part 2:', solve(10, cmds))
