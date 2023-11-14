import numpy as np
import matplotlib.pyplot as plt

# Define the range of m and k
m_values = np.linspace(1, -1, 5)
k_values = np.linspace(0, 0.25, 5)

# Define the parameters a and b
a = 1
b = 0.1

# Generate values of θ
theta = np.linspace(0, 2*np.pi, 1000)

# Create the plot
plt.figure(figsize=(8, 8))

for m in m_values:
    for k in k_values:
        # Calculate x(θ) and y(θ) for the current m and k
        x = a * np.exp(b * theta) * np.cos(theta)
        y = a * np.exp(b * theta) * np.sin(theta)

        # Modify the x and y values according to m and k
        x = x * m + k
        y = y * m + k

        # Plot the parametric curve
        plt.plot(x, y, label=f'm={m}, k={k}')

# Add labels and title
plt.xlabel('x(θ)')
plt.ylabel('y(θ)')
plt.title('Parametric Plot: x(θ) and y(θ)')

# Show legend
plt.legend()

# Show the plot
plt.show()
