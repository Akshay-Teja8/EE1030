import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


P = np.array([-2, 3, 5])
Q = np.array([1, 2, 3])
R = np.array([7, 0, -1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*P, color='r', label='P(-2, 3, 5)')
ax.scatter(*Q, color='g', label='Q(1, 2, 3)')
ax.scatter(*R, color='b', label='R(7, 0, -1)')

ax.text(*P,'P(-2, 3, 5)',color='black', ha='left')
ax.text(*Q,'Q(1, 2, 3)',color='black', ha='left')
ax.text(*R,'R(7, 0, -1)',color='black', ha='left')
line_x = np.linspace(-2, 7, 100)
line_y = np.linspace(3, 0, 100)
line_z = np.linspace(5, -1, 100)
ax.plot(line_x, line_y, line_z, color='k', label='Line through P, Q, R')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Points P, Q and R')
plt.grid(True)
plt.savefig('fig/fig.png')
