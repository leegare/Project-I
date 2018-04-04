import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Get n Bernoulli events
def bernoulli_trial(pb=0.5,nb=1000):
    return [pb<np.random.rand(1)[0] for tr in range(nb)]
# Returns the number of successes
def flip_coins(tr):
    successes = [x for x in tr if x == True]
    return len(successes)


m=5000       # Number of sets
n=1000       # Number of trials
p=0.5        # Probability of coin toss
binomial_dist=[]
random.seed(0)

# Binomial trial for m times
for t in range(m):
    # Get a set of n bernoulli trials and return with a list of True and False
    trial_set = bernoulli_trial(p,n)
    # Get the number of successes
    X = flip_coins(trial_set)
    binomial_dist.append(X)


# Plot histogramme
bd = pd.DataFrame(binomial_dist)
mini = bd.min()
maxi = bd.max()
plt.hist(binomial_dist, bins=np.arange(mini-1,maxi+1))
plt.xlabel('# of Successes')
plt.ylabel('# of Occurrences')
plt.show()
