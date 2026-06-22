# A
import math

f_max = 60

# store the values in a list that incrementally gets added onto
## review the solution to this, however.
def T(edc, f_max):
    T = [2,2]
    for i in range(f_max-2):
        u = i + 1
        n = u * edc
        pos = i + 2
        val = math.ceil(math.log(n ** 4)) + T[pos-1] + math.ceil((7/20000)*T[pos-2])
        T.append(val)
    return T[33-1], T[(f_max-1)] # 33rd pos and final position

part_A = T(23, 498)
print(part_A)
