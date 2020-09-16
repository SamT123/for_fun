'''
Digital Dice Problem 5
'''

import numpy as np

# assume that the neasrest elevator comes to pick him up

TOTAL_FLOORS = 6
MY_FLOOR = 5
N_ELEVATORS = 3

repeats = 100000
events = 0

for r in range(repeats):
    elevator_positions = np.random.uniform(0,TOTAL_FLOORS, N_ELEVATORS)
    distances = abs(elevator_positions - MY_FLOOR)
    nearest_elevator = np.argmin(distances)
    above = elevator_positions[nearest_elevator] > MY_FLOOR
    events += above

print(1 - events / repeats)