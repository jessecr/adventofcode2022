fname = 'example_input'
fname = 'input'

with open(fname, 'r') as fd:
    grid = [list(map(int, line.strip())) for line in fd]

rows, cols = len(grid), len(grid[0])
score = 0
visible = (rows + cols - 2) * 2
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        value = grid[r][c]
        above_clear = [grid[r1][c] < value for r1 in range(r)]
        below_clear = [grid[r1][c] < value for r1 in range(r + 1, rows)]
        left_clear = [grid[r][c1] < value for c1 in range(c)]
        right_clear = [grid[r][c1] < value for c1 in range(c + 1, cols)]
        visible += any(map(all, [above_clear, right_clear, below_clear, left_clear]))

        above_viz = above_clear[::-1].index(0) + 1 if 0 in above_clear else len(above_clear)
        left_viz = left_clear[::-1].index(0) + 1 if 0 in left_clear else len(left_clear)
        right_viz = right_clear.index(0) + 1 if 0 in right_clear else len(right_clear)
        below_viz = below_clear.index(0) + 1 if 0 in below_clear else len(below_clear)
        score = max(score, above_viz * left_viz * right_viz * below_viz)

print('Part 1:', visible)
print('Part 2:', score)
