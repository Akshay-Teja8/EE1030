import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import subprocess

result = subprocess.run(['./code'],stdout = subprocess.PIPE,text=True)
output = result.stdout.strip().split('\n')

P = np.array([-2, 3, 5])
Q = np.array([1, 2, 3])
R = np.array([7, 0, -1])

x_values,y_values,z_values=[],[],[]
for line in output:
    x,y,z=map(float,line.split())
    x_values.append(x)
    y_values.append(y)  
    z_values.append(z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*P, color='r', label='P')
ax.scatter(*Q, color='g', label='Q')
ax.scatter(*R, color='b', label='R')

ax.text(P[0]+0.2,P[1],P[2],'P(-2,3,5)',color='black', ha='left')
ax.text(Q[0]+0.2,Q[1],Q[2],'Q(1,2,3)',color='black', ha='left')
ax.text(R[0]+0.2,R[1],R[2],'R(7,0,-1)',color='black', ha='left')

ax.plot(x_values,y_values,z_values,color='k',label='Line through P,Q,R')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Points P, Q and R')
plt.grid(True)
plt.savefig('/home/akshay-teja-kondi/gvv/Assignment3/fig/fig.png')
