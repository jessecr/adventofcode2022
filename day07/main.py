fname = 'example_input'
fname = 'input'

dirsizes = {}
curdirs = []
with open(fname, 'r') as fd:
    for line in fd:
        if line.startswith('$'):
            _, cmd, *args = line.split()
            if cmd == 'cd':
                if args[0] == '..':
                    curdirs.pop()
                else:
                    curdirs.append(args[0])
            elif cmd == 'ls':
                dirsizes[tuple(curdirs)] = 0
        else:
            type_or_size, _ = line.strip().split()
            if type_or_size != 'dir':
                dirsizes[tuple(curdirs)] += int(type_or_size)

for dirpath in sorted(dirsizes, key=lambda x: len(x), reverse=True):
    size = dirsizes[dirpath]
    if size and len(dirpath) > 1:
        parent = dirpath[:-1]
        dirsizes[parent] += size

taken = dirsizes.pop(('/',))
sizes = sorted(dirsizes.values())
total = sum([size for size in sizes if size <= 100000])

print('Part 1:', total)

remaining = 30000000 - (70000000 - taken)
to_del = [size for size in sizes if size > remaining][0]

print('Part 2:', to_del)
