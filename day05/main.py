from collections import defaultdict

fname = 'example_input'
fname = 'input'


def main(part_2=False):
    stacks = defaultdict(list)
    with open(fname, 'r') as fd:
        while '[' in (line := fd.readline()):
            i = 1
            for chunk in line.rstrip().split('['):
                for subchunk in chunk.split(']'):
                    if subchunk.isalpha():
                        stacks[i].insert(0, subchunk)
                        i += 1
                    else:
                        i += subchunk.count(' ' * 4)

        for line in fd:
            if line.startswith('move'):
                _, count, _, src, _, dest = line.split()
                count, src, dest = map(int, (count, src, dest))
                picked = stacks[src][-count:]
                if not part_2:
                    picked = picked[::-1]
                stacks[dest].extend(picked)
                stacks[src] = stacks[src][:-count]

    for i, items in sorted(stacks.items()):
        print(items[-1], end='')

    print()


main()
main(part_2=True)
