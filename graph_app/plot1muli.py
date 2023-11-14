#An array
import numpy as np
#Use of  matplot library to plot the Graph
import matplotlib.pyplot as plt

# Define the parameters a and b
a = 1
b = 0.25

# Define specific values of m and k for centering
m = 0.5
k = 0

# Generate values of θ
theta = np.linspace(0, 2*np.pi, 1000)



# Calculate x(θ) and y(θ)
x = a * np.exp(b * theta) * np.cos(theta) * m + k
y = a * np.exp(b * theta) * np.sin(theta) * m + k

m1 = 0.5
k1 = 0

a = -1
b = 0.25

a1 = a * np.exp(b * theta) * np.cos(theta) * m1 + k1
b1 = a * np.exp(b * theta) * np.sin(theta) * m1 + k1

a = -1.5
b = 0.25

a2 = a * np.exp(b * theta) * np.cos(theta) * m1 + k1
b2 = a * np.exp(b * theta) * np.sin(theta) * m1 + k1


# Create the plot
plt.figure(figsize=(8, 8))

plt.plot(x, y)
plt.plot(a1, b1)
plt.plot(a2,b2)

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

# Show the plot
plt.show()
