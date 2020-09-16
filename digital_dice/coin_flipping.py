'''
Digital Dice Problem 4
'''

import numpy as np

def modify_coins(coins, outcomes):
    coins = coins - np.ones_like(coins)
    win = np.argmax(outcomes)
    coins[win] += 3
    return coins



def do_round(coins, p):
    outcomes = np.random.uniform(0,1,3) < p
    if len(np.unique(outcomes)) == 1:
        return coins
    elif sum(outcomes) == 1:
        coins = modify_coins(coins, outcomes)
    else:
        coins = modify_coins(coins, ~outcomes)
    return coins

def do_game(coins, p):
    n_rounds = 0
    while not (0 in coins):
        coins = do_round(coins, p)
        n_rounds += 1
    return coins, n_rounds

def get_mean_length(coins, p, repeats = 10000):
    game_lengths = np.zeros(repeats)
    for r in range(repeats):
        _, n_rounds = do_game(coins, p)
        game_lengths[r] = n_rounds
    return np.mean(game_lengths)

# 1,2,3
coins = np.array([1, 2, 3])
print(get_mean_length(coins, 0.5))
print(get_mean_length(coins, 0.4))
print('\n')

# 2,3,4
coins = np.array([2, 3, 4])
print(get_mean_length(coins, 0.5))
print(get_mean_length(coins, 0.4))
print('\n')

# 3,3,3
coins = np.array([3, 3, 3])
print(get_mean_length(coins, 0.5))
print(get_mean_length(coins, 0.4))
print('\n')

# 4,7,9
coins = np.array([4, 7, 9])
print(get_mean_length(coins, 0.5))
print(get_mean_length(coins, 0.4))

