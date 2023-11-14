import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the first circle
radius1 = 1.5
center1 = (0, 0)

# Define the parameters for the second circle
radius2 = 3
center2 = (0, 0)

# Generate values of θ
theta = np.linspace(0, 2*np.pi, 1000)

# Calculate x and y coordinates for the circles
x_circle1 = center1[0] + radius1 * np.cos(theta)
y_circle1 = center1[1] + radius1 * np.sin(theta)

x_circle2 = center2[0] + radius2 * np.cos(theta)
y_circle2 = center2[1] + radius2 * np.sin(theta)

# Create the plot
plt.figure(figsize=(8, 8))

# Plot the circles
plt.plot(x_circle1, y_circle1, label='Circle 1')
plt.plot(x_circle2, y_circle2, label='Circle 2')

# Draw lines from the center axis
plt.axhline(0, color='black', linewidth=1.0)
plt.axvline(0, color='black', linewidth=1.0)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Two Circles')

# Show legend
plt.legend()

# Set aspect ratio to equal for better visualization
plt.gca().set_aspect('equal', adjustable='box')

# Add grid to the plot
plt.grid(True)

# Show the plot
plt.show()
