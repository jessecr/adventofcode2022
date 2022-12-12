fname = 'example_input.txt'
# fname = 'input.txt'

with open(fname, 'r') as fd:
    for line in fd:
        vals = map(ord, line)
