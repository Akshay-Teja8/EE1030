import matplotlib.pyplot as plt

A = (-2, -2)
B = (2, -4)
P = (-0.29, -2.86)

plt.figure(figsize=(5, 5))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label="Line AB")
plt.plot(A[0], A[1], 'go', label='Point A')
plt.plot(B[0], B[1], 'co', label='Point B')
plt.plot(P[0], P[1], 'ro-',label="Point P")

plt.text(A[0], A[1], 'A=(-2,-2)', color='black', fontsize=12,ha='left', va='bottom')
plt.text(B[0], B[1], 'B=(2,-4)', color='black', fontsize=12, ha='right', va='top')
plt.text(P[0], P[1], 'P(-2/7,-20/7)', fontsize=12, ha='left', va='bottom')

plt.xlabel('Y')
plt.ylabel('X')
plt.title('Plot of points A, B and P')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)

plt.savefig('/home/akshay-teja-kondi/gvv/Assignment2/Figs/Fig.png')

