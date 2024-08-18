import matplotlib.pyplot as plt

A = (-2, -2)
B = (2, -4)
P = (-0.29, -2.86)

plt.figure(figsize=(6, 6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-', label="Line AB")
plt.plot(P[0], P[1], 'ro-',label="Point P")

plt.text(A[0], A[1], 'A=(-2,-2)', fontsize=12,ha='right')
plt.text(B[0], B[1], 'B=(2,-4)', fontsize=12, ha='right')
plt.text(P[0], P[1], 'P(-2/7,-20/7)', fontsize=12, ha='left')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of points A, B and P')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.savefig('Fig.pdf')

