directions = {'R': (1, 1), 'L': (1, -1), 'U': (0, 1), 'D': (0, -1)}


def update_knot(to_update, target):
    row_diff = target[0] - to_update[0]
    col_diff = target[1] - to_update[1]

    if abs(row_diff) > 1 or abs(col_diff) > 1:
        r = max(min(row_diff, 1), -1)
        c = max(min(col_diff, 1), -1)
        to_update[0] += r
        to_update[1] += c


def solve(num_knots, cmds):
    knots = [[0, 0] for _ in range(num_knots)]
    visited = {(0, 0)}
    for direction, count in cmds:
        for i in range(count):
            idx, amt = directions[direction]
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
