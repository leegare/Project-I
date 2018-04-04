import time
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(2000)

# Iterative Method
def fib_it(n):
    f = [0,1]
    for a in range(n-2):
        f.append(f[-2]+f[-1])
    return f

# Recursive Method
def fib_rec(n, f=[]):
    if len(f)==0:
        return fib_rec(n, [0,1])
    if len(f)<n:
        f.append(f[-2]+f[-1])
        return fib_rec(n, f)
    else:
        return f

#m = int(input('n:'))
m=2000
N = np.arange(0, m, 50)   # 0,10,20,..,m
n_r = []                # List of time executed in recursive mode
n_i = []                # List of time executed in iterative mode
for x in N:
    #print(x)
    start_time = time.time()
    fib_it(x)
    n_i.append(time.time()-start_time)
    start_time = time.time()
    fib_rec(x)
    n_r.append(time.time()-start_time)

plt.plot(N, n_i, label='Iterative')
plt.plot(N, n_r, label='Recursive')
plt.legend(loc='best')
plt.ylim(ymin=0, ymax=0.004)
plt.xlabel('$n$')
plt.ylabel('$seconds$')
plt.show()
