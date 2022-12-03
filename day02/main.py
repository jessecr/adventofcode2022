MOVE_MAP_LEFT = {'A': 0, 'B': 1, 'C': 2}
MOVE_MAP_RIGHT = {'X': 0, 'Y': 1, 'Z': 2}


def get_outcome(l_val, r_val):
    if l_val == r_val:
        return 3
    if (r_val - 1) % 3 == l_val:
        return 6
    return 0


fname = 'example_input'
fname = 'input'

with open(fname, 'r') as fd:
    pairs = [line.split() for line in fd]

part1_scores = []
part2_scores = []
for opp, my in pairs:
    opp_val = choice = MOVE_MAP_LEFT[opp]
    my_val = MOVE_MAP_RIGHT[my]
    part1_scores.append(get_outcome(opp_val, my_val) + my_val + 1)

    if my == 'X':
        choice = (opp_val - 1) % 3
        outcome = 0
    elif my == 'Z':
        choice = (opp_val + 1) % 3
        outcome = 6
    else:
        outcome = 3

    part2_scores.append(outcome + choice + 1)

print(sum(part1_scores))
print(sum(part2_scores))
