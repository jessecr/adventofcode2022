fname = 'example_input'
fname = 'input'

val = 0
chars = []
cycle = 1
x = 1
pixel = 0
with open(fname, 'r') as fd:
    for line in fd:
        line = line.strip()
        if line.startswith('addx'):
            v = int(line.split()[1])
            c_incr = 2
        elif line == 'noop':
            v = 0
            c_incr = 1

        for _ in range(c_incr):
            if (cycle - 20) % 40 == 0:
                val += cycle * x

            if abs(pixel - x) < 2:
                chars.append('#')
            else:
                chars.append(' ')

            cycle += 1
            pixel = (cycle - 1) % 40

        x += v

print(val)

for i in range(0, 240, 40):
    print(' '.join(chars[i:i + 40]))
