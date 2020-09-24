'''
Digital Dice Problem 7
'''

import numpy as np
import matplotlib.pyplot as plt

repeats = 10000
results = []

for r in range(repeats):
    n_draws = 0
    matches = [150, 150]
    while not (0 in matches):
        discard = np.random.randint(0,len(matches))
        matches[discard] -= 1
        n_draws += 1
    results.append(sum(matches))

print(np.mean(results))
