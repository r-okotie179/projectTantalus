# I do not understand why this only works for smaller cases so I will run through the algorithm step by step (by hand) 
# to read some of the book today
def testing_func():
    n = int(input(""))
    s = [(i+1) for i in range(n)]
    u = [[n] * len(s)]
    q = [(n-st) for st in s]
    return (s, q)

def dd_cache(n, cache):
    # steps for each case will be the list of numbers up to (not including) n
    steps = [(i+1) for i in range(n+1)]
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in cache:
        return cache[n]
    
    total = sum(dd_cache(n-s, cache) for s in steps)
    cache[n] = total
    return total

def dd(n):
    return dd_cache(n, {})
    
n = int(input(""))
print(dd(n))


