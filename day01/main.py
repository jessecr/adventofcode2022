# with open('example_input', 'r') as fd:
#     chunks = fd.read().split('\n\n')

with open('input', 'r') as fd:
    chunks = fd.read().split('\n\n')

calories = sorted(map(sum, [map(int, lines.splitlines()) for lines in chunks]))

print(calories[-1])

print(sum(calories[-3:]))
