"""
This should be returned to and improved since it is quite rudimentary and does not encompass all the code for how m is computed (which involved variance and covariance which is quite interesting).
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

x = np.linspace(0,10,15)
y = np.array([0.5, 13.6, 15.7, 18, 35, 23.5, 28, 25.6, 31, 30.98, 37, 38.76, 42, 44.5, 47])

# find the means of this data and then iterate different combinations of m and c
# the goal is to plot the same surface that andrew french plotted
## statistical means that are required
x_m = np.mean(x)
y_m = np.mean(y)
x_2m = np.mean(x**2)
xy_m = np.mean(x*y)

## not sure how the m and c values are determined so I will plot a surface with just random values
m = np.linspace(0, 5, 25)
c = np.linspace(-5,10, 25)

## not sure how to make the surface smooth 
for j in range(len(m)):
    for k in range(len(c)):
        S = []
        for l in range(len(y)):
            ind = (y[l] - (m[j]*x[l]) - c[k]) ** 2
            S.append(ind)
        S_sum = np.sum(np.array(S))
        ax.scatter(m[j], c[k], S_sum, marker = '+')
        
plt.show()
