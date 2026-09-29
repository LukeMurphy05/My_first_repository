# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Parameters
# -----------------------------

h = 0.05
tmax = 10 * np.pi

x = 0
v = 1


# -----------------------------
# Create arrays
# -----------------------------

t_arr = np.arange(0, tmax + h, h)

x_arr = np.empty_like(t_arr)
v_arr = np.empty_like(t_arr)

x_exact = np.empty_like(t_arr)
v_exact = np.empty_like(t_arr)


# Initial conditions
x_arr[0] = x
v_arr[0] = v


# -----------------------------
# Euler method
# -----------------------------

for i in range(1, len(t_arr)):

    x_old = x
    v_old = v

    x = x_old + h * v_old
    v = v_old - h * x_old

    x_arr[i] = x
    v_arr[i] = v


# -----------------------------
# Exact solution
# -----------------------------

x_exact = np.sin(t_arr)
v_exact = np.cos(t_arr)


# -----------------------------
# Create two plots
# -----------------------------

fig, ax = plt.subplots(1, 2, figsize=(12, 5))


# -----------------------------
# Plot 1: Time dependence
# -----------------------------

ax[0].plot(t_arr, x_arr, label="Euler x")
ax[0].plot(t_arr, x_exact, label="Exact x")

ax[0].plot(t_arr, v_arr, label="Euler v")
ax[0].plot(t_arr, v_exact, label="Exact v")

ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("x / v")
ax[0].set_title("Time Dependence")
ax[0].legend()
ax[0].grid()


# -----------------------------
# Plot 2: Phase space
# -----------------------------

ax[1].plot(x_arr, v_arr, 'k', label="Euler")

ax[1].plot(x_exact, v_exact, label="Exact")

ax[1].axis('equal')

ax[1].set_xlabel(r"$x$")
ax[1].set_ylabel(r"$v$")
ax[1].set_title("Phase Space")
ax[1].legend()
ax[1].grid()


# -----------------------------
# Save and display
# -----------------------------

plt.tight_layout()

plt.savefig("R3_results.png", dpi=300)

plt.show()