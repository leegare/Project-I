# Script that plots the time spent by the recursive, iterative and embeded
# function of factorial for different values ranging from $interval
# to $end_value

import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(5000)

# VARIABLES:
end_value=2000
interval = 50
N = np.arange(0, end_value, interval)   # 0,10,20,..,m
n_r = []                # List of time executed in recursive mode
n_i = []                # List of time executed in iterative mode
n_m = []                # List of time executed using the math.fact function

# METHODS:
# Recursive Method
def recursive_factorial(n):
    if n<=1:
        return 1
    return n * recursive_factorial(n-1)
# Iterative Method
def iterative_factorial(n):
    factorial = 1       # of type numpy.int64
    for i in range(n, 1, -1):
        #print('i:', i, 'f:', factorial)
        factorial *= n
        n -= 1
    return factorial

# PROCESS:
for x in N:
    start_time = time.time()
    iterative_factorial(x)
    n_i.append(time.time()-start_time)
    start_time = time.time()
    recursive_factorial(x)
    n_r.append(time.time()-start_time)
    start_time = time.time()
    math.factorial(x)
    n_m.append(time.time()-start_time)

# GRAPH
plt.plot(N, n_i, label='Iterative')
plt.plot(N, n_r, label='Recursive')
plt.plot(N, n_m, label='Embeded Func')
plt.legend(loc='best')
plt.ylim(ymin=0, ymax=0.003)
plt.show()
