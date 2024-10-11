import numpy as np
import matplotlib.pyplot as plt
import subprocess


result = subprocess.run(['./code'],stdout=subprocess.PIPE,text=True)
data = result.stdout.strip().split('\n')
from io import StringIO
data1 = StringIO("\n".join(data))
values = np.loadtxt(data1)
x = values[:,0]
y = values[:,1]

plt.plot(x,y,label=r'$y = x|x|$', color='blue')
plt.fill_between(x,y,where=(x>-1),color='lightblue',alpha=0.5)
plt.axvline(x=-1, color='red', linewidth=1)
plt.axvline(x=1, color='red', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x|x|')
plt.legend()
plt.grid(True)
plt.savefig('/home/akshay-teja-kondi/EE1030/Assignment7/Fig/fig.png')

