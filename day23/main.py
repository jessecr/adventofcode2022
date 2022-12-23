from itertools import chain

grouped_offsets = [
    [(-1, 0), (-1, -1), (-1, 1)],  # north
    [(1, 0), (1, -1), (1, 1)],  # south
    [(0, -1), (-1, -1), (1, -1)],  # west
    [(0, 1), (-1, 1),  (1, 1)],  # east
]


def get_grouped_offsets(cell):
    return [
        [(cell[0] + r, cell[1] + c) for r, c in offsets]
        for offsets in grouped_offsets
    ]


with open('input.txt', 'r') as fd:
    ex_lines = fd.read().splitlines()

elf_positions = set()
for r, line in enumerate(ex_lines):
    for c, v in enumerate(line):
        if v == '#':
            elf_positions.add((r, c))

moved = True
i = 0
while moved:
    i += 1
    moved = False

    proposals = {}
    for elf in elf_positions:
        elf_surrounding = get_grouped_offsets(elf)
        if not elf_positions.intersection(chain(*elf_surrounding)):
            # No surrounding elves
            continue

        for positions in elf_surrounding:
            if not elf_positions.intersection(positions):
                proposals.setdefault(positions[0], []).append(elf)
                moved = True
                break

    for proposed_pos, src_positions in proposals.items():
        if len(src_positions) == 1:
            elf_positions.remove(src_positions[0])
            elf_positions.add(proposed_pos)

    grouped_offsets.append(grouped_offsets.pop(0))

    if i == 10:
        r_positions = sorted(pos[0] for pos in elf_positions)
        c_positions = sorted(pos[1] for pos in elf_positions)
        num_cells = (r_positions[-1] - r_positions[0] + 1) * (c_positions[-1] - c_positions[0] + 1)
        print('Part 1:', num_cells - len(elf_positions))

print('Part 2:', i)
