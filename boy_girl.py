'''
The classic boy girl paradox!
'''

import numpy as np


repeats = 100000
pairs = [list(np.random.randint(0,2,2)) for r in range(repeats)]
with_boy = [l for l in pairs if 1 in l]
first_boy = [l for l in pairs if l[0] == 1]

n_both_with = sum([1 if sum(l) == 2 else 0 for l in with_boy])
n_both_first = sum([1 if sum(l) == 2 else 0 for l in with_boy])
print(n_both_with/len(with_boy))
print(n_both_first/len(first_boy))

