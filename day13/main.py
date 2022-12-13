from functools import cmp_to_key
from itertools import zip_longest


def compare(left, right):
    for l_item, r_item in zip_longest(left, right):
        if l_item is None:
            return -1
        elif r_item is None:
            return 1

        l_is_list = isinstance(l_item, list)
        r_is_list = isinstance(r_item, list)

        if l_is_list or r_is_list:
            if not l_is_list:
                l_item = [l_item]
            elif not r_is_list:
                r_item = [r_item]

            res = compare(l_item, r_item)
            if res != 0:
                return res
        else:
            if l_item < r_item:
                return -1
            elif l_item > r_item:
                return 1

    return 0


fname = 'example_input.txt'
fname = 'input.txt'
corrects = []
signals = [[[2]], [[6]]]
with open(fname, 'r') as fd:
    for i, lines in enumerate(fd.read().split('\n\n')):
        left, right = map(eval, lines.splitlines())
        signals.append(left)
        signals.append(right)
        if compare(left, right) == -1:
            corrects.append(i + 1)


print('Part 1:', sum(corrects))

signals_str = list(map(str, sorted(signals, key=cmp_to_key(compare))))
i1 = signals_str.index('[[2]]') + 1
i2 = signals_str.index('[[6]]') + 1
print('Part 2:', i1 * i2)
