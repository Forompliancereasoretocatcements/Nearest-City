def nearest_city(truck_pos, cities, city_pos):
    distance = (truck_pos[0] - city_pos[0][0]) ** 2 + (truck_pos[1] - city_pos[0][1]) ** 2
    city = cities[0]
    for i in range(len(cities)):
        if (truck_pos[0] - city_pos[i][0]) ** 2 + (truck_pos[1] - city_pos[i][1]) ** 2 < distance:
            city = cities[i]
            distance = (truck_pos[0] - city_pos[i][0]) ** 2 + (truck_pos[1] - city_pos[i][1]) ** 2
    return city
            
tests = [[[3, 5], ['a', 'b', 'c'], [[4, 4], [3, 4], [5, 8]]],
         [[0, -3], ['E', 'Ee'], [[2, 243], [5, 8]]],
         [[0, 0], ['02', '3', '7'], [[0, 5], [0, 0], [0, 0]]],
         [[355, 345344], ['A', 'B', 'C'], [[-132, -3], [8339583, 4285], [-202, 294824]]],
         [[-42, 0], ['a', 'b', 'c'], [[-42, 3], [-42, -2], [-42, 2]]],
         [[3, 5], ['a', 'b', 'c', '1', '4'], [[4, 4], [3, 4], [5, 8], [9, 5], [3, 7]]]]

for test in tests:
    print(nearest_city(test[0], test[1], test[2]))
