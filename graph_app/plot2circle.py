#An array
import numpy as np
#Use of  matplot library to plot the Graph
import matplotlib.pyplot as plt

# Generate values of θ
theta = np.linspace(0, 2*np.pi, 1000)

m1 = 0.5
k1 = 0
a = -1
b = 0.25

a1 = a * np.exp(b * theta) * np.cos(theta) * m1 + k1
b1 = a * np.exp(b * theta) * np.sin(theta) * m1 + k1
# Create the plot
plt.figure(figsize=(8, 8))

#plt.plot(x, y)
plt.plot(a1, b1)
# Draw lines from the center axis
plt.axhline(0, color='black',linewidth=1.0)
plt.axvline(0, color='black',linewidth=1.0)

# Add labels and title
plt.xlabel('x(θ)')
plt.ylabel('y(θ)')
#plt.title(f'Parametric Plot: x(θ) and y(θ) for m={m}, k={k}')

# Show legend
plt.legend()

# Set aspect ratio to equal for better visualization
plt.gca().set_aspect('equal', adjustable='box')

# Add grid to the plot
plt.grid(True)

# Define the parameters for the first circle
radius1 = 0.792
center1 = (0.306, 0.003)

radius2=1.752
center2=(-0.6533,0.0007)

# Generate values of θ
theta = np.linspace(0, 2*np.pi, 1000)

# Calculate x and y coordinates for the circles
x_circle1 = center1[0] + radius1 * np.cos(theta)
y_circle1 = center1[1] + radius1 * np.sin(theta)

x_circle2 = center2[0] + radius2 * np.cos(theta)
y_circle2 = center2[1] + radius2 * np.sin(theta)

# Create the plot
#plt.figure(figsize=(8, 8))

# Plot the circles
plt.plot(x_circle1, y_circle1, linestyle='--',label='Circle 1')
plt.plot(x_circle2, y_circle2, linestyle='--',label='Circle 2')

# Draw lines from the center axis
#plt.axhline(0, color='black', linewidth=1.0)
#plt.axvline(0, color='black', linewidth=1.0)

# Add labels and title
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Two Circles')

# Show legend
#plt.legend()
#plt.xlim(x_circle1, y_circle1)
#ßplt.ylim(x_circle2, y_circle2)



# Set aspect ratio to equal for better visualization
plt.gca().set_aspect('equal', adjustable='box')

# Add grid to the plot
plt.grid(True)

# Show the plot
plt.show()
