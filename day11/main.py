from copy import deepcopy
from functools import reduce
from operator import mul, add

fname = 'example_input'
fname = 'input'


def get_operation_func(lh, op_str, rh):
    op = {'+': add, '*': mul}[op_str]
    if rh == 'old':
        return lambda x: op(x, x)
    rh = int(rh)
    return lambda x: op(x, rh)


monkeys = []
with open(fname, 'r') as fd:
    while (line := fd.readline()):
        monkeys.append({
            'items': list(map(int, fd.readline().split(':')[1].replace(' ', '').split(','))),
            'operation': get_operation_func(*fd.readline().split('=')[1].split()),
            'divisor': int(fd.readline().split()[-1]),
            'dest': {
                True: int(fd.readline().split()[-1]),
                False: int(fd.readline().split()[-1]),
            }
        })
        fd.readline()

common_div = reduce(mul, [monkey['divisor'] for monkey in monkeys])


def solve_it(monkeys, rounds, reduce_worry):
    inspections = [0] * len(monkeys)
    for x in range(rounds):
        for i, monkey in enumerate(monkeys):
            for item in monkey['items']:
                item = monkey['operation'](item)
                if reduce_worry:
                    item = item // 3
                dest = monkey['dest'][item % monkey['divisor'] == 0]
                monkeys[dest]['items'].append(item % common_div)

            inspections[i] += len(monkey['items'])
            monkey['items'] = []

    return mul(*sorted(inspections)[-2:])


print('Part 1:', solve_it(deepcopy(monkeys), 20, True))
print('Part 2:', solve_it(deepcopy(monkeys), 10000, False))
