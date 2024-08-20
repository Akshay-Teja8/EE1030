import numpy as np
import matplotlib.pyplot as plt

def dir_vec(A,B):
    return B-A

def line_gen(A,B):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB

A = np.array([-2, -2])
B = np.array([2, -4])


AB = dir_vec(A, B)

ratio = 3 / 7
P = A + ratio * AB

x_AB = line_gen(A, B)

plt.plot(x_AB[0,:], x_AB[1,:], label="Line AB", color='blue')
plt.scatter(A[0], A[1], color='red', label="Point A (-2,-2)")
plt.scatter(B[0], B[1], color='green', label="Point B (2,-4)")
plt.scatter(P[0], P[1], color='magenta', label=f"Point P ({P[0]:.2f},{P[1]:.2f})")

plt.text(A[0] - 0.1, A[1] + 0.1, 'A=(-2,-2)', fontsize=12)
plt.text(B[0] - 0.4, B[1] + 0.2, 'B=(2,-4)', fontsize=12)
plt.text(P[0] , P[1] + 0.1, 'P=(-2/7,-20/7)', fontsize=12)

plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.title('Point P on Line Segment AB')
plt.savefig('/home/akshay-teja-kondi/gvv/Assignment2/Figs/Fig.png')
