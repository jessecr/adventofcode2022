fname = 'example_input'
# fname = 'input'

subsets = intersections = 0
with open(fname, 'r') as fd:
    for line in fd:
        first, second = line.strip().split(',')
        first_start, first_end = first.split('-')
        first_set = set(range(int(first_start), int(first_end) + 1))

        second_start, second_end = second.split('-')
        second_set = set(range(int(second_start), int(second_end) + 1))

        if first_set.issubset(second_set) or second_set.issubset(first_set):
            subsets += 1
        if first_set.intersection(second_set):
            intersections += 1

print('Part 1:', subsets)
print('Part 2:', intersections)
