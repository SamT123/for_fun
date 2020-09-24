'''
Digital Dice problem 11
'''

import numpy as np
import random
import matplotlib.pyplot as plt

def get_est(n_obs, max_obs):
    return max_obs * (n_obs+1) / n_obs - 1

def get_err(N, obs_percentage):
    obs = random.sample(list(range(1,N+1)), int(round(N*obs_percentage)))
    return (N - get_est(len(obs), max(obs))) / N

repeats = 100000
Ns = np.random.randint(100, 1001, repeats)


# 2% 
fig, axs = plt.subplots(3,1)

results_2 = [get_err(Ns[i], 0.02) for i in range(repeats)]
axs[0].hist(results_2, rwidth = 1, bins = np.arange(-1,1,0.005))

# 5% 
results_5 = [get_err(Ns[i], 0.05) for i in range(repeats)]
axs[1].hist(results_5, rwidth = 1, bins = np.arange(-1,1,0.005))

# 10% 
results_10 = [get_err(Ns[i], 0.10) for i in range(repeats)]
axs[2].hist(results_10, rwidth = 1, bins = np.arange(-1,1,0.005))

plt.show()