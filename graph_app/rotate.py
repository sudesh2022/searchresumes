import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon

# Define the parameters for the circles
radius1 = 0.792
center1 = (0.306, 0.003)

radius2 = 1.752
center2 = (-0.6533, 0.0007)

# Generate values of θ for the circles
theta_circle = np.linspace(0, 2 * np.pi, 1000)

# Calculate x and y coordinates for the circles
x_circle1 = center1[0] + radius1 * np.cos(theta_circle)
y_circle1 = center1[1] + radius1 * np.sin(theta_circle)

x_circle2 = center2[0] + radius2 * np.cos(theta_circle)
y_circle2 = center2[1] + radius2 * np.sin(theta_circle)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the initial circles
circle1, = ax.plot(x_circle1, y_circle1, linestyle='--', label='Circle 1')
circle2, = ax.plot(x_circle2, y_circle2, linestyle='--', label='Circle 2')

# Draw lines from the center axis
ax.axhline(0, color='black', linewidth=1.0)
ax.axvline(0, color='black', linewidth=1.0)

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')

# Set aspect ratio to equal for better visualization
ax.set_aspect('equal', adjustable='box')

# Shade the region between the circles
polygon = Polygon(np.column_stack([x_circle1, y_circle1]), closed=True, edgecolor='none', facecolor='gray', alpha=0.5)
ax.add_patch(polygon)

# Show the legend
ax.legend()

# Function to update plot during animation
def update(frame):
    angle = np.deg2rad(frame)
    circle1.set_data(center1[0] + radius1 * np.cos(theta_circle + angle), center1[1] + radius1 * np.sin(theta_circle + angle))
    circle2.set_data(center2[0] + radius2 * np.cos(theta_circle + angle), center2[1] + radius2 * np.sin(theta_circle + angle))
    return circle1, circle2

# Number of frames (adjust as needed)
num_frames = 360

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

# Display the animation
plt.show()
