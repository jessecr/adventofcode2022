from collections import deque
from functools import reduce
from operator import le, lt, mul


def compare_lists(l1, l2, op):
    assert len(l1) == len(l2)
    return [op(l1[i], l2[i]) for i in range(len(l1))]


blueprints = []
with open('input.txt.', 'r') as fd:
    for i, line in enumerate(fd):
        bp = {}
        parts = line.split()
        bp['ore'] = (int(parts[6]), 0, 0)
        bp['clay'] = (int(parts[12]), 0, 0)
        bp['obsidian'] = (int(parts[18]), int(parts[21]), 0)
        bp['geode'] = (int(parts[27]), 0, int(parts[30]))
        bp['max'] = (
            max(c[0] for c in bp.values()),
            max(c[1] for c in bp.values()),
            max(c[2] for c in bp.values()),
            None
        )
        blueprints.append(bp)


def runit(blueprints, starting_minutes):
    types = ['ore', 'clay', 'obsidian', 'geode']
    geodes = []
    for bpi, bp in enumerate(blueprints):
        robots = [1, 0, 0, 0]
        stores = [0, 0, 0, 0]
        q = deque([(robots, stores, starting_minutes)])
        max_geodes = 0
        iters = 0
        while q:
            iters += 1
            robots, stores, minutes = q.popleft()

            # Resources collected by existing robots
            updated_stores = stores.copy()
            for i, v in enumerate(robots):
                updated_stores[i] += v

            minutes -= 1
            if minutes == 0:
                max_geodes = max(max_geodes, updated_stores[3])
                continue

            choices = []

            # If we can't afford all robot types yet, add a choice that just waits.
            if any(compare_lists(stores[:3], bp['max'][:3], lt)):
                choices.append((None, (0, 0, 0)))

            for i, typ in reversed(list(enumerate(types))):
                # If we are producing more of a resource than the most expensive robot requires,
                # don't build more robots that produce that resource.
                if bp['max'][i] is not None and robots[i] >= bp['max'][i]:
                    continue

                # If we could have built this robot last iteration, don't build it this time.
                # This is an approximation of our prior stores, and won't catch every instance.
                prior_stores = (max(stores[0] - robots[0], 0),
                                max(stores[1] - robots[1], 0),
                                max(stores[2] - robots[2], 0))
                if all(compare_lists(bp[typ], prior_stores, le)):
                    continue

                if all(compare_lists(bp[typ], stores[:3], le)):
                    choices.append((i, bp[typ]))
                    # If we can build an obsidian or geodo robot, always build it and no others.
                    if typ in ('obsidian', 'geode'):
                        break

            for robot_idx, costs in choices:
                new_stores = updated_stores.copy()
                new_robots = robots.copy()

                # If we're creating a new robot, remove its cost from the stores
                if robot_idx is not None:
                    new_stores[0] -= costs[0]
                    new_stores[1] -= costs[1]
                    new_stores[2] -= costs[2]

                    new_robots[robot_idx] += 1

                q.append((new_robots, new_stores, minutes))

        geodes.append((bpi + 1, max_geodes))

    return geodes


p1 = sum([bpi * geodes for bpi, geodes in runit(blueprints, 24)])
print('Part 1:', p1)

p2 = reduce(mul, [geodes for _, geodes in runit(blueprints[:3], 32)])
print('Part 2:', p2)
