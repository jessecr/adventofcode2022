from copy import deepcopy
from operator import add, floordiv, mul, sub

operator_mapping = {'+': add, '*': mul, '-': sub, '/': floordiv}
with open('input.txt', 'r') as fd:
    monkeys = {}
    for line in fd:
        parts = line.replace(':', '').split()
        if len(parts) == 2:
            monkeys[parts[0]] = int(parts[1])
        else:
            monkeys[parts[0]] = parts[1:4]


def get_value(monkeys, node, variable=None):
    value = monkeys[node]
    if isinstance(value, int):
        return value
    elif isinstance(value, str):
        return f'({value})'

    lside, opstr, rside = value
    lval = variable if lside == variable else get_value(monkeys, lside, variable=variable)
    rval = variable if rside == variable else get_value(monkeys, rside, variable=variable)
    if isinstance(lval, str) or isinstance(rval, str):
        monkeys[node] = f'{lval} {opstr} {rval}'
    else:
        monkeys[node] = operator_mapping[opstr](lval, rval)

    return get_value(monkeys, node)


print('Part 1:', int(get_value(deepcopy(monkeys), 'root')))

m2 = deepcopy(monkeys)
m2['root'][1] = '='
equation = get_value(m2, 'root', variable='humn')

# By replacing 'humn' with an imaginary number, the expression evaluates to
# ax + b = 0 (where x in this case is the imginary number), which we can then solve
# using -b/a
lside, rside = equation.split(' = ')
expr = f'{lside} - ({rside})'
grouped = eval(expr.replace('humn', '1j'))
print('Part 2:', int(round(-grouped.real / grouped.imag)))
