import numpy as np
import matplotlib.pyplot as plt
import subprocess

result=subprocess.run(['./code'],stdout = subprocess.PIPE,text=True)
output=result.stdout.strip().split('\n')

direction_vector = np.array(list(map(float,output[0].split())))
normal_vector = np.array(list(map(float,output[1].split())))

data = np.loadtxt(output[2:],dtype=float)
x_values = data[:,0]
y_values = data[:,1]

direction_vector = direction_vector/np.linalg.norm(direction_vector)
normal_vector = normal_vector/np.linalg.norm(normal_vector)

plt.figure(figsize=(8,8))
plt.plot(x_values,y_values,'k--',label='y=x',alpha=0.5)
plt.quiver(0,0,*direction_vector,scale=3,color='green',label='Direction Vector')
plt.quiver(0,0,*normal_vector,scale=3,color='red',label='Normal Vector')

plt.xlim([min(x_values)-1, max(x_values)+1])
plt.ylim([min(y_values)-1, max(y_values)+1])
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Line with Direction and Normal Vectors')
plt.grid(True)
plt.savefig('/home/akshay-teja-kondi/gvv/Assignment4/Fig/fig.png')

