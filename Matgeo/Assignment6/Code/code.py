import subprocess
import numpy as np
import matplotlib.pyplot as plt

result = subprocess.run(['./code'], stdout=subprocess.PIPE, text=True)

lines = result.stdout.splitlines()

x_intersections = np.array([float(lines[0].split()[0]), float(lines[1].split()[0])])
y_intersections = np.array([float(lines[0].split()[1]), float(lines[1].split()[1])])
data = np.loadtxt(lines[2:], dtype=float)

x_parabola = data[:, 0] 
y_parabola = data[:, 1] 
x_line = data[:, 2]   
y_line = data[:, 3]     

plt.figure(figsize=(8, 6))
plt.plot(x_parabola, y_parabola, label=r'$x^2 = 4y$', color='blue')
plt.plot(x_line, y_line, label=r'$x = 4y - 2$', color='red')


plt.scatter(x_intersections, y_intersections, color='black', zorder=5, label="Intersections")


plt.fill_between(x_parabola, y_parabola, y_line[:len(y_parabola)],
                 where=(y_line[:len(y_parabola)] >= y_parabola),
                 color='green', alpha=0.3, label="Bounded Area")


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of $x^2 = 4y$ and $x = 4y - 2$ with Intersections')

np.vectorize(lambda x, y: plt.annotate(f'({x}, {y})', (x, y), 
                                       textcoords="offset points", 
                                       xytext=(5,5), ha='center'))(x_intersections, y_intersections)

plt.legend()
plt.axis('equal')
plt.grid(True)
plt.savefig('/home/akshay-teja-kondi/gvv/Assignment6/Fig/fig.png')
