from itertools import islice
from functools import reduce
from string import ascii_letters

fname = 'example_input'
fname = 'input'

priorities = []
with open(fname, 'r') as fd:
    for line in fd:
        line = line.strip()
        mid_idx = len(line) // 2
        left, right = line[:mid_idx], line[mid_idx:]
        common = set(left).intersection(right)
        for item in common:
            priority = ascii_letters.index(item) + 1
            priorities.append(priority)

print('Part 1:', sum(priorities))

priorities = []
with open(fname, 'r') as fd:
    while (lines := [line.strip() for line in islice(fd, 3)]):
        common = reduce(lambda x, y: set(x).intersection(y), lines)
        item = list(common)[0]
        priority = ascii_letters.index(item) + 1
        priorities.append(priority)

print('Part 2:', sum(priorities))
