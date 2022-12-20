from queue import PriorityQueue


def get_input(example=False):
    valves = {}
    flow_rates = {}
    fname = 'example_input.txt' if example else 'input.txt'
    with open(fname, 'r') as fd:
        for line in fd:
            parts = line.replace('=', ' ').replace(';', '').replace(',', '').split()
            node = parts[1]
            rate = int(parts[5])
            children = parts[parts.index('to') + 2:]

            valves[node] = children
            flow_rates[node] = rate

    return valves, flow_rates


def get_valves_to_visit(flow_rates):
    non_zero_valves = [k for k, v in flow_rates.items() if v > 0]
    return non_zero_valves + ['AA']


def get_shortest_paths(graph, start):
    """Shortest path to each node in `graph` from `start`."""
    visited = set()
    distances = {}

    q = PriorityQueue()
    q.put((0, start))

    while not q.empty():
        node_cost, node = q.get()
        for nn in graph[node]:
            if nn not in visited:
                cost = node_cost + 1
                if nn not in distances or cost < distances[nn]:
                    distances[nn] = cost
                    q.put((cost, nn))

        visited.add(node)

    return distances


def get_shortest_paths_to_valves(graph, valves):
    distances = {}
    for valve in valves:
        shortest_paths = get_shortest_paths(graph, valve)
        distances[valve] = {k: v for k, v in shortest_paths.items() if k in valves}

    return distances


def compute_all_traversals(distances, start, minutes, flow_rates):
    """Compute the most pressure that can be released for each unique set of valves.

    Returns a mapping between a frozenset of the visited valves, and the highest
    pressure that can be released from visiting those valves.

    """
    stack = [(start, minutes, set(), 0)]
    scores = {}
    while stack:
        node, minutes, opened, score = stack.pop()

        # The order that the valves were visited doesn't matter for finding the
        # optimal route. We just want the highest score for any permutation of
        # each set of valves.
        _opened = frozenset(opened)
        scores[_opened] = max(scores.get(_opened, 0), score)

        # Don't visit valves we have already opened
        to_visit = set(distances[node]).difference(opened)
        for nn in to_visit:
            dist = distances[node][nn]
            new_minutes = minutes - dist - 1
            if new_minutes > 0:
                # We have time to travel to and open this valve
                new_score = score + new_minutes * flow_rates[nn]
                stack.append(
                    (nn, new_minutes, opened | {nn}, new_score)
                    )

    return scores


def part_1(distances, flow_rates):
    traversals = compute_all_traversals(distances, 'AA', 30, flow_rates)
    return sorted(traversals.values())[-1]


def part_2(distances, flow_rates):
    traversals = compute_all_traversals(distances, 'AA', 26, flow_rates)
    # Find largest score for two traversals with non-overlapping paths
    p2 = 0
    for path1, score1 in traversals.items():
        for path2, score2 in traversals.items():
            if path1 and path2 and not path1.intersection(path2):
                p2 = max(p2, score1 + score2)

    return p2


valves, flow_rates = get_input()
valves_to_visit = get_valves_to_visit(flow_rates)
valve_distances = get_shortest_paths_to_valves(valves, valves_to_visit)

print('Part 1:', part_1(valve_distances, flow_rates))
print('Part 2:', part_2(valve_distances, flow_rates))
