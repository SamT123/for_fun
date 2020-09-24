'''
Digital Dice problem 10
'''

import numpy as np
from collections import Counter
from copy import copy
import matplotlib.pyplot as plt


def swap(n):
    assert n in [0,1]
    if n == 0:
        return 1
    else:
        return 0

def do_walk(curr, umbrellas, p_rain):
    rain = np.random.uniform() < p_rain

    if rain:
        umbrellas[curr] += -1
        umbrellas[swap(curr)] += 1
    
    return swap(curr), umbrellas


def do_run(location, umbrellas, p_rain):
    n_walks = 0

    while not -1 in umbrellas:
        location, umbrellas_ = do_walk(location, umbrellas, p_rain)
        n_walks += 1

    return n_walks - 1

umbrellas = [1,1]
location = 0
repeats = 1000
ps = np.arange(0.01,1,0.01)

# x,y = 1,1
xy11 = []
for p_rain in ps:
    xy11.append(np.mean( [do_run(location, [1,1], p_rain) for r in range(repeats)] ))

# x,y = 2,2
xy22 = []
for p_rain in ps:
    xy22.append(np.mean( [do_run(location, [2,2], p_rain) for r in range(repeats)] ))


plt.plot(ps,xy11)
plt.show()
plt.plot(ps,xy22)
plt.show()