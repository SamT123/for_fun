'''
implement gradient descent
'''

import numpy as np
from inspect import signature
from copy import copy

def g(x, y):
    return (x-3)**2 + (x-13)*(y-47) + (y-7)**2


def get_grad(f, curr, n_param, delta = 0.001):

    grad_v = np.zeros(n_param)
    curr_val = f(*curr)
    for p in range(n_param):
        param_delta = copy(curr)
        param_delta[p] = param_delta[p] + delta
        grad_v[p] =  f(*param_delta) - curr_val
    return grad_v / delta


def solve(f, init = 'default' , lower = 'default', upper = 'default', step_size = 0.1, delta = 0.001, threshold = 0.000000000001):
    n_param = len(signature(f).parameters)
    if init == 'default':
        init = np.zeros(n_param)
    if lower == 'default':
        lower = np.repeat(-100, n_param)
    if upper == 'default':
        upper = np.repeat(100, n_param)
    curr_vals = init
    prev_val = np.inf
    while prev_val - f(*curr_vals) > threshold:
        prev_val  = f(*curr_vals)
        grad_v = get_grad(f, curr_vals, n_param, delta)
        curr_vals -= grad_v * step_size
    return curr_vals

print(solve(g))