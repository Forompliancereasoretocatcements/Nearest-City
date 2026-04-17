from heapq import *

def find_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) ** 2 + abs(pos1[1] - pos2[1]) ** 2

def find_nearest_cities(truck, cities, k):
    city_list = []
    for city in cities:
        distance = find_distance(truck, cities[city])
        if len(city_list) < k:
            heappush_max(city_list, (distance, city))
        elif city_list[0][0] > distance:
            heapreplace_max(city_list, (distance, city))
    return [i[1] for i in city_list]

tests = [[[3, 5], {'a': [54, 32]}, 1],
         [[4, 2], {'a': [35, 35], 'b': [4, -23]}, 1],
         [[0, 0], {'H': [0, 2], 'J': [-2, 0]}, 2],
         [[8, 1], {'a': [9, 3], 'f': [7, -1], 'g': [10, 423], 'q': [8, 2]}, 3],
         [[534, 535], {'1': [34, 432], '2': [303, 985], '3': [0, 2]}, 2],
         [[-1, -3], {'A': [-2, -2], 'B': [-3, -5], 'C': [0, 0], 'D': [-1, -2], 'E': [-4, -5], 'F': [0, -3]}, 4],
         ]

for test in tests:
    print(find_nearest_cities(test[0], test[1], test[2]))
