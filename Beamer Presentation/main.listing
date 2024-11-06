import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import subprocess

result = subprocess.run(['./code'],stdout = subprocess.PIPE,text=True)
output = result.stdout.strip().split('\n')

P = np.fromstring(output[0].replace('P ',''),sep=' ')
Q = np.fromstring(output[1].replace('Q ',''),sep=' ')
R = np.fromstring(output[2].replace('R ',''),sep=' ')

store=np.genfromtxt(output[3:],delimiter='')
x_values,y_values,z_values = store.T


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
