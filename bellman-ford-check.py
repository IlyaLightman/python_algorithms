graph1 = {
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


def bellman_ford(graph):
    n = len(graph)
    infinity = float('inf')
    F = [0] + [infinity] * (n - 1)
    for k in range(1, n):
        for i in graph.keys():
            for j in graph[i]:
                if F[i] + graph[i][j] < F[j]:
                    F[j] = F[i] + graph[i][j]
    print(F)


bellman_ford(graph1)
