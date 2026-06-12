def stepcount(n, steps):
  if n == 0:
    return 1
  if n < 0: 
    return 0
  return sum(stepcount(n-s, steps) for s in steps)

## Creating a caching program for dynamic programming

def memsteps(n, steps):
    return  memsteps_cache(n, steps, {})

def memsteps_cache(n, steps, cache):
    if n == 0:
        return 1
    if n < 0: 
        return 0
    if n in cache:
        return cache[n]
    
    total = sum(memsteps_cache(n-s, steps, cache) for s in steps)
    cache[n] = total # for each step down in the tree, there is a stored cache
    return total
