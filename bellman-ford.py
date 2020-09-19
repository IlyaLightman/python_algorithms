graph = {
    0: {
        1: 6, 2: 2
    },
    1: {
        3: 1
    },
    2: {
        1: -3, 3: 5
    },
    3: {}
}

infinity = float('inf')
n = 4  # Для graph

F = [infinity] * n
F[0] = 0

print(graph)

print(F)

for k in range(1, n):  # Количество рёбер от start до ноды
    for i in graph.keys():
        for j in graph[i]:
            # print(i, j)
            if F[i] + graph[i][j] < F[j]:
                F[j] = F[i] + graph[i][j]

print(F)
