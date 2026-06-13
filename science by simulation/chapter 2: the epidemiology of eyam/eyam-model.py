# below will be the use of William Mompessons's parish records, which effectively forms a closed system
import numpy as np 
import matplotlib.pyplot as plt

t = ([0, 0.51, 1.02, 1.53, 2.04, 2.55, 3.57]) # months
s = [235, 201, 153.5, 121, 108, 97, 83] # susceptible
i = [14.5, 22, 29, 21, 8, 8, 0] # infected
d = [0, 26.5, 67, 107.5, 133.5, 144.5, 166.5] # death
r = [0] * len(t) # recovered

sidr = [s,i,d,r]
for q in sidr:
    plt.scatter(t, q, marker = '+', alpha=0.9)
    plt.plot(t, q, alpha=0.3)

errx = (np.array(t).max() - 0) * 0.01
erry = (np.array(sidr).max() - 0) * 0.01
plt.xlim(0-errx, np.array(t).max()+errx)
plt.ylim(0-erry, np.array(sidr).max()+erry)
plt.grid(alpha=.35)

plt.xlabel("Time (months)")
plt.show()