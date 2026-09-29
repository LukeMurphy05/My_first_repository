import numpy as np
import matplotlib.pyplot as plt
from R4_function import damped_pendulum

# Parameters
omega0 = 1
h = 0.01
tmax = 20

# Three damping values
b_values = [0.1, 2, 4]
labels = ["Underdamped", "Critically damped", "Overdamped"]

# Time array
t_arr = np.arange(0, tmax + h, h)

# Create figure
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Run simulation for each value of b
for b, label in zip(b_values, labels):

    # Initial conditions
    x = 0
    v = 1

    # Arrays
    x_arr = np.empty_like(t_arr)
    v_arr = np.empty_like(t_arr)

    x_arr[0] = x
    v_arr[0] = v

    # Euler method
    for i in range(1, len(t_arr)):

        y = np.array([x, v])

        dydt = damped_pendulum(t_arr[i - 1], y, b, omega0)

        x = x + h * dydt[0]
        v = v + h * dydt[1]

        x_arr[i] = x
        v_arr[i] = v

    # First plot: displacement against time
    ax[0].plot(t_arr, x_arr, label=label)

    # Second plot: phase space
    ax[1].plot(x_arr, v_arr, label=label)


# First plot
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Displacement, x")
ax[0].set_title("Damped Oscillator")
ax[0].legend()
ax[0].grid()

# Second plot
ax[1].set_xlabel("x")
ax[1].set_ylabel("v")
ax[1].set_title("Phase Space")
ax[1].legend()
ax[1].grid()

plt.tight_layout()
plt.show()