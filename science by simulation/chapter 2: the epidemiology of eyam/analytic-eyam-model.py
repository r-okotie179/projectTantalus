import numpy as np
import matplotlib.pyplot as plt

# This model will use analytic integration to find the values for alpha and beta
I = [14.5, 22, 29, 21, 8, 8, 0]
S = [235, 201, 153.5, 121, 108, 97, 83]

x_val = np.array([np.log(s/S[0]) for s in S])
y_val = []
for i in range(len(I)):
    if len(I) != len(S):
        raise ValueError
    val = I[i] + S[i] - I[0] - S[0]
    y_val.append(val)
y_val = np.array(y_val)
#print(x_val, y_val)

# Performing linear regression to find the value of the gradient (by reading the appendix)
## https://stats.stackexchange.com/questions/631540/from-a-theoretical-standpoint-why-is-linear-regression-useful
## Note to why looking into linear regression is useful for further progress with prediction.


## for this model, alpha is assumed to be 2.87 as I will not dwell on the adjacent linear regression 

# Iterate different values 

plt.scatter(x_val, y_val)
plt.show()

# From finding the values, I can now to the Euler Method of discrete integration to find the final values
