# Import libraries
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

# Parameters
psi = 2
b = 0.5


# Creating vectors X and Y
w = np.linspace(0, 100, 1000)
n = (w/(b*psi))**(1/(psi-1))


fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(w, n)

# Show the plot
plt.show()

# Value function with respect to A and w

fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')

w = np.arange(-5, 5.1, 0.2)
A = np.arange(-5, 5.1, 0.2)

w, A = np.meshgrid(w, A)
v = w*(w/(b*psi))**(1/(psi-1)) + A - b*(w/(b*psi))**(psi/(psi-1))
surf = ax.plot_surface(w, A, v, cmap = plt.cm.cividis)

# Set axes label
ax.set_xlabel('w', labelpad=20)
ax.set_ylabel('A', labelpad=20)
ax.set_zlabel('v', labelpad=20)

fig.colorbar(surf, shrink=0.5, aspect=8)

plt.show()