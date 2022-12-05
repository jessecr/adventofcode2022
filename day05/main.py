from collections import defaultdict
from copy import deepcopy

fname = 'example_input'
fname = 'input'

with open(fname, 'r') as fd:
    stacks_text, instructions_text = fd.read().split('\n\n')

stacks = defaultdict(list)
for line in stacks_text.splitlines()[:-1]:
    i = 1
    for chunk in line.split('['):
        for subchunk in chunk.split(']'):
            if subchunk.isalpha():
                stacks[i].insert(0, subchunk)
                i += 1
            else:
                i += subchunk.count(' ' * 4)

instructions = []
for line in instructions_text.splitlines():
    _, count, _, src, _, dest = line.split()
    instructions.append((int(count), int(src), int(dest)))


def solve(stacks, instructions, reverse_crates=False):
    for count, src, dest in instructions:
        picked = stacks[src][-count:]
        if reverse_crates:
            picked = picked[::-1]
        stacks[dest].extend(picked)
        stacks[src] = stacks[src][:-count]

    return ''.join([v[-1] for _, v in sorted(stacks.items())])


print(solve(deepcopy(stacks), instructions, reverse_crates=True))
print(solve(stacks, instructions))
