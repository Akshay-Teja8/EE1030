import numpy as np
import matplotlib.pyplot as plt
from funcs import * 

A = np.array([-2, -2])
B = np.array([2, -4])

AB = dir_vec(A, B)
P = A + (3 / 7) * AB

x_AB = line_gen(A, B)

plt.plot(x_AB[0,:], x_AB[1,:], label="Line AB", color='blue')
plt.scatter(A[0], A[1], color='red', label="Point A (-2,-2)")
plt.scatter(B[0], B[1], color='green', label="Point B (2,-4)")
plt.scatter(P[0], P[1], color='magenta', label=f"Point P ({P[0]:.2f},{P[1]:.2f})")
plt.text(A[0] + 0.2, A[1], 'A=(-2,-2)',color='black', ha='left')
plt.text(B[0] - 0.2, B[1], 'B=(2,-4)',color='black',ha='right')
plt.text(P[0], P[1] + 0.1, f'P=({P[0]:.2f},{P[1]:.2f})',color='black', ha='left')

plt.title('Point P on line AB')
plt.grid(True)
plt.savefig('/home/akshay-teja-kondi/gvv/Assignment2/Figs/Fig.png')

