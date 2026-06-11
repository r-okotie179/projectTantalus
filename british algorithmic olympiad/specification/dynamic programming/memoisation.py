# based on the numberphile introduction to memoisation
import numpy as np
'''
input: n, steps (where steps is a set of the different combinations of steps that could be taken)
'''
n = 5
steps = [1, 2, 4]

def naive(n, steps):
  # this function will return how many times the given combination will rest at 0
  # these problems are better to visualise so i will think of a way to visualise this
  if n == 0: 
    return 1
  if n < 0:
    return 0 
  return sum(naive(n-s, steps) for s in steps)
  
def plotting(n, steps)
  # this will return the branch entirely
  steps = np.array(steps)
  m = np.array([n] * len(steps)) # matrix of len(steps) each of value of n
  coordinates = [m]
  for i in range(n/2):
    m -= steps
    coordinates.append(m)
  return coordinates
