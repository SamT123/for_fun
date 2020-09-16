'''
Digital Dice Problem 2
'''


import numpy as np

BILL_WAIT = 7
JILL_WAIT = 5

def interval_overlap(int1, int2):
    if min(int1) < max(int2) and max(int1) > min(int2):
        return True
    else:
        return False



repeats = 100000
event = 0

for r in range(repeats):
    bill_arrival = np.random.uniform(0,30)
    jill_arrival = np.random.uniform(0,30)

    bill_interval = [bill_arrival, min(bill_arrival + BILL_WAIT, 30)]
    jill_interval = [jill_arrival, min(jill_arrival + JILL_WAIT, 30)]


    if interval_overlap(bill_interval, jill_interval):
        event +=1


print(event/repeats)