states_needed = set([1,2,3,4,5])

stations = {}
stations['k1'] = set([1,2])
stations['k2'] = set([3])
stations['k3'] = set([2,3,4])
stations['k4'] = set([6,1])
stations['k5'] = set([9,2])
stations['k6'] = set([2,3,4,5])
stations['k7'] = set([5])


final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

            states_needed -= states
            final_stations.add(station)

print(final_stations)

