'''
Digital Dice Problem 15, pg 78
Questions:
(1) average waiting time
(2) maximum waiting time
(3) average length of queue
(4) maximum length of waiting queue
(5) what if we hire another clerk
(6) what fraction of the day are the clerk(s) idle

ARRIVAL_RATE, SERVICE_RATE = (30, 40) or (30, 25)

'''


import numpy as np
import matplotlib.pyplot as plt

# numerical integration approach

# state:
queue = []
customer_number = 0
clerk_occupied_t = 0
queue_length = []
t = 0

# record:
arrival_times = []
service_times = []

# paramters
ARRIVAL_RATE = 30/60/60 # per hour -> per second
SERVICE_RATE = 40/60/60 # per hour -> per second
DAY_LENGTH = 60*60*10
DELTA = .1

while t < DAY_LENGTH or len(queue) > 0:

    arrive = (np.random.poisson(ARRIVAL_RATE * DELTA) > 0)

    if len(queue) > 0:
        serve = (np.random.poisson(SERVICE_RATE * DELTA) > 0)
    else:
        serve = False
        clerk_occupied_t += DELTA


    if arrive:
        queue.append(customer_number)
        customer_number += 1
        arrival_times.append(t)

    if serve:
        queue.pop(0)
        service_times.append(t)

    queue_length.append(len(queue))

    t = t+DELTA


print('\n')
print('num customers = {}'.format(len(arrival_times)))
waiting_times = [service_times[i] - arrival_times[i] for i in range(0, len(arrival_times)-1)]

print('mean wait = {}'.format(np.mean(waiting_times)))
print('max wait =  {}'.format(max(waiting_times)))
print('mean queue = {}'.format(np.mean(queue_length)))
print('max queue = {}'.format(max(queue_length)))
print('clerk occupied = {}'.format(clerk_occupied_t / t))
print('\n')

plt.hist(waiting_times)
plt.show()

# # usefuls fns

# def in_interval(l, lower, upper, inclusive = False):
#     n = 0
#     if inclusive:
#         for item in l:
#             if lower <= item and item <= upper:
#                 n += 1
#     if not inclusive:
#         for item in l:
#             if lower < item and item < upper:
#                 n += 1
#     return n

# # constants
# ARRIVAL_RATE = 30/60/60 # per hour -> per second
# SERVICE_RATE = 40/60/60 # per hour -> per second
# DAY_LENGTH = 60*60*10

# # state
# queue_length = 0
# t = 0

# # records
# service_times = []
# max_length = 0

# arrival_times = []
# while t < DAY_LENGTH:
#     interval = np.random.exponential(1/ARRIVAL_RATE)
#     arrival_times.append(t + interval)
#     t += interval


# t = 0
# last_customer = -1
# while last_customer < len(arrival_times)-1 or queue_length > 0:
#     if queue_length == 0:
#         t = arrival_times[last_customer + 1]
#         queue_length += 1
#         last_customer += 1
#         max_length = max(max_length, queue_length)
#     else:
#         service_time = np.random.exponential(1/SERVICE_RATE)
#         n_arrivals = in_interval(arrival_times, t, t+service_time, False)
#         queue_length += n_arrivals - 1
#         last_customer += n_arrivals
#         t = t + service_time
#         service_times.append(t)
#         max_length = max(max_length, queue_length+1)



# waiting_times = [service_times[i] - arrival_times[i] for i in range(0, len(arrival_times) - 1)]
# waiting_times

# np.mean(waiting_times)
# max(waiting_times)
# max_length
# plt.hist(waiting_times)
# plt.show()
# ####



# for interval in arrival_intervals:
#     t += interval
#     queue_length += 1
    
    
    




# while t < DAY_LENGTH:
#     if queue_length == 0:
#         t_arr = np.random.exponential(1/ARRIVAL_RATE)
#         t += t_arr
#         queue_length += 1
#     else:
#         t_arr = np.random.exponential(1/ARRIVAL_RATE)
#         t_ser = np.random.exponential(1/SERVICE_RATE)

#         if t_arr > t_ser:
#             queue_length += 1
#         elif t_arr < t_ser:
#             queue_length += -1

#         t += min(t_arr, t_ser)


