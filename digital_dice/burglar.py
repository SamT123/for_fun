'''
Digital Dice problem 9
'''

import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def get_step():
    return random.sample([-2, -1, 1, 2], 1)[0]


def do_run():
    visited = set()
    curr = 0
    n_homes = 0
    while not curr in visited:
        visited.add(curr)
        curr += get_step()
        n_homes += 1
    return n_homes
    

repeats = 100000
results = [do_run() for r in range(repeats)]

print(Counter(results)[1]/repeats)
print(Counter(results)[2]/repeats)
print(Counter(results)[3]/repeats)
print(Counter(results)[4]/repeats)
print(Counter(results)[5]/repeats)
print(Counter(results)[6]/repeats)
print(Counter(results)[7]/repeats)

plt.hist(results, rwidth = .5, bins = np.arange(1,15)-0.5)
plt.show()