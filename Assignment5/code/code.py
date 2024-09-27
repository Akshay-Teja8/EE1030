import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Run the C program and capture its output
result = subprocess.run(['./code'], capture_output=True, text=True)

# Split the output into lines
data = result.stdout.splitlines()

# Read vectors a, b, c from the first three lines directly using np.fromstring
vector_a = np.fromstring(data[1], sep=' ')
vector_b = np.fromstring(data[2], sep=' ')
vector_c = np.fromstring(data[3], sep=' ')

# Read the points for the first and second planes directly from the output
points_a_b_str = '\n'.join(data[6:126])  # Adjust these indices based on the output
points_b_c_str = '\n'.join(data[127:])   # Adjust these indices based on the output


# Convert the points_a_b and points_b_c strings to arrays
points_a_b = np.fromstring(points_a_b_str, sep=' ')

# Reshape points_a_b into (-1, 3)
try:
    points_a_b = points_a_b.reshape(-1, 3)
except ValueError as e:
    print("Error reshaping points_a_b:", e)
    print("Shape of points_a_b before reshape:", points_a_b.shape)
    raise
# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first plane using vectors a and b
ax.plot_trisurf(points_a_b[:, 0], points_a_b[:, 1], points_a_b[:, 2], alpha=0.5, color='blue')
# Define colors for the vectors
colors = ['red', 'blue', 'green']

# Plot the vectors a, b, and c as arrows
ax.quiver(0, 0, 0, vector_a[0], vector_a[1], vector_a[2], color=colors[0], label='Vector a', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, vector_b[0], vector_b[1], vector_b[2], color=colors[1], label='Vector b', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, vector_c[0], vector_c[1], vector_c[2], color=colors[2], label='Vector c', arrow_length_ratio=0.1)

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Planes and Vectors Visualization')

# Set plot limits for better visualization
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Create legend entries for clarity
blue_surface = plt.Line2D([0], [0], color='blue', lw=10, label='Plane formed by a and b')
red_surface = plt.Line2D([0], [0], color='red', lw=10, label='Plane formed by b and c')

# Add legend
ax.legend(handles=[blue_surface, red_surface])

# Show the plot
plt.savefig('/home/akshay-teja-kondi/gvv/Assignment5/Fig/fig.png')

