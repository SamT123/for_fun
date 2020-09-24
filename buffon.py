'''
Buffon's Needle
'''
import numpy as np
import matplotlib.pyplot as plt


def contains_int(x, y):
    return np.floor(x) != np.floor(y)

def transpose_list(l):
    o = []
    for i in range(len(l[0])):
        o.append([])
        for j in range(len(l)):
            o[i].append(l[j][i])
    return o




LENGTH = 0.5
BOARD_HEIGHT = 10
BOARD_WIDTH = 10

repeats = 100000
pi_ests = []
n_cross = 0

for i in range(BOARD_WIDTH):
    plt.plot([i,i], [0, BOARD_HEIGHT], color = 'grey')

for r in range(repeats):
    needle = [[np.nan, np.nan], [np.nan, np.nan]]
    needle[0] = [np.random.uniform(0,BOARD_WIDTH), np.random.uniform(0,BOARD_HEIGHT)]
    theta = np.random.uniform(0,360)
    needle[1] = [needle[0][0] + LENGTH * np.cos(theta), needle[0][1] + LENGTH * np.sin(theta)]
    needle_coords = transpose_list(needle)
    #plt.plot(needle_coords[0], needle_coords[1], color = 'black')
    if contains_int(needle[0][0], needle[1][0]):
        n_cross += 1
    
    if n_cross > 0:
        pi_ests.append(2*LENGTH / (n_cross/r))
    else:
        pi_ests.append(np.nan)


print(2*LENGTH / (n_cross/repeats))
plt.show()
plt.plot(list(range(repeats))[10:], ((np.array(pi_ests)-3.14159))[10:])
plt.show()
plt.plot(list(range(repeats))[10:], np.log(abs(np.array(pi_ests)-3.14159))[10:])
plt.show()

