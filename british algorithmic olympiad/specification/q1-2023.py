import math
def T(f_max, edc=1, ind=0):
    iter = edc * f_max
    T_null = [2,2] # the long, brute force list
    for i in range(iter):
        j = len(T_null) 
        next_T = math.ceil(4 * math.log((j + 1), 10)) + T_null[j-1] + math.ceil(((7/20000)*(T_null[j-2])))
        T_null.append(next_T)
        
    T = []
    if edc != 1:
        for i in range(len(T_null)):
            k = i + 1
            if k%edc == 0:
                T.append(T_null[i])
    if len(T) == 0:
        return T_null
    else:
        return T
    
a = T(498, 23)
print(a[(33-1)])
print(a[498-1])

"""
>>> %Run -c $EDITOR_CONTENT
9333
2122215
>>> 
"""
