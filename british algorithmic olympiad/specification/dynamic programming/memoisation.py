# based on the numberphile introduction to memoisation
import numpy as np
import matplotlib.pyplot as plt
'''
input: n, steps (where steps is a set of the different combinations of steps that could be taken)
'''
n = 10
steps = [1, 2]

def naive(n, steps):
  # this function will return how many times the given combination will rest at 0
  # these problems are better to visualise so i will think of a way to visualise this
  if n == 0: 
    return 1
  if n < 0:
    return 0 
  return sum(naive(n-s, steps) for s in steps)
  
def func_coord(n, steps):
  # this will return the branch entirely
  steps = np.array(steps)
  m = np.array([n] * len(steps)) # matrix of len(steps) each of value of n
  u = m
  coordinates = [m]
  while m.all() > 0:
    coordinates.append(m)
    m -= steps
  return coordinates, u, steps

'''
There is something wrong with this iteration which means that there is not a useful output, just some bs (as shown below)
'''
def plotting():
    coordinates, u, s = func_coord(10, [1,2,4])
    print(f"{coordinates},\n{u},\n{s}")
    for i in range(len(coordinates)):
        for j in range(len(coordinates[i])):
            plt.scatter(i, coordinates[i][j])
    plt.show()

'''
>>> %Run memoisation.py
>>> plotting()
[array([  5,   0, -10]), array([  5,   0, -10]), array([  5,   0, -10]), array([  5,   0, -10]), array([  5,   0, -10]), array([  5,   0, -10])],
[  5   0 -10],
[1 2 4]
>>> 
'''
