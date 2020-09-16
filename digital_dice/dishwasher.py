'''
Digital Dice Problem 1
'''

import numpy as np
from collections import Counter

# probability of 4 dishes being broken by the same guy (out of 5 guys total)

n_5 = 5
n_4 = 5*4*5
n_tot = 5**5

print((n_5 + n_4)/ n_tot)


# monte carlo
repeats = 100000
event = 0
for r in range(repeats):
    identities = np.random.randint(1, 6, 5)
    if max(Counter(identities).values()) >= 4:
        event += 1

print(event / repeats)
