'''
Digital Dice problem 10
'''

import random
import numpy as np


def sim(total, against, missing):
    all_senators = [0 for _ in range(against)] + [1 for _ in range(total - against)]
    voters = random.sample(all_senators, total-missing)
    return sum(voters)/len(voters) < 0.5

TOTAL = 100
AGAINST = 49
MISSING = 3
repeats = 100000

results = [sim(TOTAL, AGAINST, MISSING) for r in range(repeats)]
print(np.mean(results))