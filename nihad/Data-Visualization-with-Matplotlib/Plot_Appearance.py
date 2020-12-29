import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color='PURPLE',lw=2,ls='--')

ax.set_xlim([0,1])
ax.set_ylim([0,2])
plt.show()

x

len(x)


