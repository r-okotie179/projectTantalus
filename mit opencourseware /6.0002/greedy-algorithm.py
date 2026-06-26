'''
Greedy Algorithm Test (for fractional knapsack):
1. Calculate the ratio (value/weight) for each item.
2. Sort all the items in decreasing order of the ratio.
3. Iterate through items:
    - if the current item fully fits, add its full value and decrease capacity
    - otherwise, take the fractional part that fits and add proportional value.
4. Stop once the capacity becomes zero.
'''

val = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

def fractionalKnapsack(val, wt, cap):
    # find ratio of value to weight and sort in that sense
    ## how to do sorting algorithms??
    
    if len(val) != len(wt):
        raise ValueError
    
    ratio = []
    for i in range(len(val)):
        piece = val[i] / wt[i]
        ratio.append(piece)
    
    #ratio = ratio.sort()
    print(ratio)
    #return max_val # which has been determined by greedy algorithm

fractionalKnapsack(val, weight, capacity)
