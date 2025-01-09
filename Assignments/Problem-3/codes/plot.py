import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared library
lib = ctypes.CDLL('./bilinear.so')

# Define the prototype of the functions
lib.differentialEquation.restype = ctypes.c_double
lib.differentialEquation.argtypes = [ctypes.c_double]

lib.bilinearTransform.restype = None
lib.bilinearTransform.argtypes = [ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double), ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))]

# Define the CFUNCTYPE for the differential equation
C_FUNC_TYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
c_differential_equation = C_FUNC_TYPE(lib.differentialEquation)

# Initial conditions
x0 = 0  # Initial x value
y0 = 1  # Initial y value (y at x=0)
h = 0.05  # Step size
n = 50  # Number of steps

# Allocate memory for the results array
results = (ctypes.POINTER(ctypes.c_double) * (n + 1))()
for i in range(n + 1):
    results[i] = (ctypes.c_double * 2)()

# Call the bilinearTransform function from the shared library
lib.bilinearTransform(c_differential_equation, x0, y0, h, n, results)

# Extract results to numpy arrays for plotting
x_values = np.linspace(x0, x0 + n * h, n + 1)
y_values = np.zeros(n + 1)

for i in range(n + 1):
    y_values[i] = results[i][1]

# Let's say we want to plot another set of data (e.g., the exact solution y = x^2 + 2x + 1)
exact_y_values = x_values**2 + 2*x_values + 1  # This is the exact solution for y' = 2x + 2

# Plot both the numerical and exact solutions on the same plot
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Siml')
plt.plot(x_values, exact_y_values, linestyle='--', color='r', label='Theoritical')

# Add titles and labels
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()  # Show the legend to differentiate the two curves

# Display the plot
plt.savefig('../figs/fig.png')

