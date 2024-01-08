def lcirsh(n, p, k):
    """Circular bit shift left.

    Shift integer `n` to the left by `p` places, wrapping the leftmost `k` - `p` places
    back to be the rightmost bits.
    """
    return ((n << p) & (2 ** k - 1)) | (n >> (k - p))


def rcirsh(n, p, k):
    """Circular bit shift right."""
    return n >> p | (n & 2 ** p - 1) << k - p


def visualize(height, width, pos, lefts, rights, ups, downs):
    lefts = [bin(val)[2:].replace('1', '<').replace('0', '.') for val in lefts]
    rights = [bin(val)[2:].replace('1', '>').replace('0', '.') for val in rights]
    downs = [bin(val)[2:].replace('1', 'v').replace('0', '.') for val in downs]
    ups = [bin(val)[2:].replace('1', '^').replace('0', '.') for val in ups]
    start = '#E' if pos[0] == -1 else '#.'
    print(start + '#' * (width - 2))
    for r in range(height - 2):
        row = []
        for c in range(width - 2):


ex_lines = '''#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#'''.splitlines()

# ex_lines = '''#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#'''.splitlines()

height, width = len(ex_lines), len(ex_lines[0])

lefts = [0] * (height - 2)
rights = [0] * (height - 2)
ups = [0] * (width - 2)
downs = [0] * (width - 2)
for r, line in enumerate(ex_lines[1:-1]):
    for c, char in enumerate(line[1:-1]):
        lefts[r] = lefts[r] << 1 | (char == '<')
        rights[r] = rights[r] << 1 | (char == '>')
        ups[c] = ups[c] << 1 | (char == '^')
        downs[c] = downs[c] << 1 | (char == 'v')

print(lefts, rights, ups, downs)

start = (-1, 1)
goal = (height - 1, width - 2)
