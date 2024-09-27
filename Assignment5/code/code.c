#include <stdio.h>
#include <stdlib.h>

// Function to generate points for the plane formed by two vectors
void generate_plane(float a[3], float b[3], float u_min, float u_max, float v_min, float v_max, int steps) {
    // Check if steps are non-negative
    if (steps < 0) {
        printf("Number of steps must be non-negative.\n");
        return;
    }

    float u_step = (u_max - u_min) / steps;
    float v_step = (v_max - v_min) / steps;

    // Generate points for the plane
    int total_points = (steps + 1) * (steps + 1);
    float (*points)[3] = malloc(total_points * sizeof(*points)); // Dynamically allocate memory
    if (points == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    int index = 0;

    for (int i = 0; i <= steps; i++) {
        for (int j = 0; j <= steps; j++) {
            float u = u_min + i * u_step;
            float v = v_min + j * v_step;
            // Linear combination of vectors a and b
            points[index][0] = u * a[0] + v * b[0];
            points[index][1] = u * a[1] + v * b[1];
            points[index][2] = u * a[2] + v * b[2];
            index++;
        }
    }

    // Print the generated points (x, y, z)
    for (int k = 0; k < total_points; k++) {
        printf("%.2f %.2f %.2f\n", points[k][0], points[k][1], points[k][2]);
    }

    free(points); // Free dynamically allocated memory
}

int main() {
    // Define the vectors a, b, and c
    float a[3] = {1, -2, 3};  // Vector a
    float b[3] = {2, 3, -4};  // Vector b
    float c[3] = {1, -3, 1};  // Vector c

    // Print vectors a, b, and c for reference
    printf("Vectors:\n");
    printf("%.2f %.2f %.2f\n", a[0], a[1], a[2]);
    printf("%.2f %.2f %.2f\n", b[0], b[1], b[2]);
    printf("%.2f %.2f %.2f\n", c[0], c[1], c[2]);

    // Define the range for u and v (parameters for linear combination)
    float u_min = -1, u_max = 1;  // Set limits for u
    float v_min = -1, v_max = 1;  // Set limits for v

    // Number of steps to divide the range (resolution)
    int steps = 10;

    // Generate points for the first plane using vectors a and b
    printf("\nPoints on the plane formed by vectors a and b:\n");
    generate_plane(a, b, u_min, u_max, v_min, v_max, steps);

    // Generate points for the second plane using vectors b and c
    printf("\nPoints on the plane formed by vectors b and c:\n");
    generate_plane(b, c, u_min, u_max, v_min, v_max, steps);

    return 0;
}

