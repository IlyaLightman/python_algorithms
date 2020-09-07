graph = {
    0: {
        1: 2, 3: 12, 7: 10
    },
    1: {
        2: 3, 5: 4
    },
    2: {
        3: 2, 4: 1
    },
    3: {},
    4: {
        8: 1
    },
    5: {
        6: 1
    },
    6: {
        7: 2
    },
    7: {
        9: 8
    },
    8: {},
    9: {
        8: 3
    }
}

infinity = float('inf')
costs = {
    1: 2,
    3: 12,
    7: 10,
    2: infinity,
    4: infinity,
    5: infinity,
    6: infinity,
    8: infinity,
    9: infinity
}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra():
    print(costs)
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(costs)


dijkstra()
