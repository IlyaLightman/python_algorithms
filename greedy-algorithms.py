# На каждом шаге выбирается локально-оптимальное решение,
# а в итоге получается глобально-оптимальное решение

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}


final_stations = set()


while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        print(states_needed, states)
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    print(best_station)
    states_needed -= states_covered
    final_stations.add(best_station)

print('\n', final_stations)
