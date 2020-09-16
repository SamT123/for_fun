'''
Digital Dice Problem 3
'''

import numpy as np

def get_nearest(car_idx, locations):
    N_CARS = len(locations)
    if car_idx == 0:
        nearest = 1
    elif car_idx == N_CARS - 1:
        nearest = N_CARS - 2
    else:
        nearest = [car_idx-1, car_idx+1][np.argmin( [locations[car_idx] - locations[car_idx-1] , locations[car_idx+1] - locations[car_idx]] )]
    return nearest

LENGTH = 1
N_CARS = 30

repeats = 10000
event = 0
for r in range(repeats):
    locations = np.sort(np.random.uniform(0, LENGTH, N_CARS))
    car_idx = np.random.randint(0, N_CARS)
    nearest_neighbour = get_nearest(car_idx, locations)
    nearest_neighbour_nearest = get_nearest(nearest_neighbour, locations)
    

    if nearest_neighbour_nearest == car_idx:
        event += 1

print(event / repeats)


event2 = []
for r in range(repeats):
    locations = np.sort(np.random.uniform(0, LENGTH, N_CARS))
    event_loc = 0

    for car_idx in range(0, N_CARS):
        nearest_neighbour = get_nearest(car_idx, locations)
        nearest_neighbour_nearest = get_nearest(nearest_neighbour, locations)
        if nearest_neighbour_nearest == car_idx:
            event_loc += 1
    event2.append(event_loc)


print(np.mean(event2)/ N_CARS)
print(event2[1:10])
