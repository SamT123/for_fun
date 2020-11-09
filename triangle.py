'''
What is the probability that a line cut at random points can form a triangle?

Ans: a triangle can be formed iff. the longest segment is less than 0.5 in length
'''

import numpy as np

repeats = 100000
successes = 0


for r in range(repeats):
    cuts = np.sort(np.random.uniform(0,1,2))
    segs = [cuts[0], cuts[1]- cuts[0], 1 - cuts[1]]

    if max(segs) > 0.5:
        successes += 1

print(successes/repeats)

