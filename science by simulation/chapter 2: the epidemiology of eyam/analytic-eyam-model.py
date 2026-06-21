import numpy as np
import matplotlib.pyplot as plt

# This model will use analytic integration to find the values for alpha and beta then perform linear regression
I = [14.5, 22, 29, 21, 8, 8, 0]
S = [235, 201, 153.5, 121, 108, 97, 83]

x_val = np.array([np.log(S/S[0]) for S in S])
y_val = np.array([(I + S - I[0] - S[0]) for I,S in I,S])

print(x_val, y_val)
# From finding the values, I can now to the Euler Method of discrete integration to find the final values