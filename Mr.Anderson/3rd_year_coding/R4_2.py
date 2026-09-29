import matplotlib.pyplot as plt
import numpy as np

dt = 0.05
x0 = 0
y0 = 1
t0 = 0
t_max = 10*np.pi

n_steps = int((t_max - t0)/dt)

t_arr = np.zeros(n_steps)
x_euler = np.zeros(n_steps)
y_euler = np.zeros(n_steps)

x_modified = np.zeros(n_steps)
y_modified = np.zeros(n_steps)

# Initial conditions
x_euler[0] = x0
y_euler[0] = y0

x_modified[0] = x0
y_modified[0] = y0

# Standard Euler
for i in range(n_steps - 1):

    x = x_euler[i]
    y = y_euler[i]

    dx = y
    dy = -x

    x_euler[i+1] = x + dx*dt
    y_euler[i+1] = y + dy*dt


# Modified Euler
for i in range(n_steps - 1):

    x = x_modified[i]
    y = y_modified[i]

    # Euler prediction
    xinit = x + dt*y
    yinit = y - dt*x

    # Corrected values
    x_modified[i+1] = x + 0.5*dt*(y + yinit)
    y_modified[i+1] = y - 0.5*dt*(x + xinit)


# Time array
t_arr = np.arange(n_steps)*dt

# Exact solution
x_exact = np.sin(t_arr)

# Errors
error_euler = np.abs(x_euler - x_exact)
error_modified = np.abs(x_modified - x_exact)


# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Solutions
ax1.plot(t_arr, x_exact, 'r--', label="Exact")
ax1.plot(t_arr, x_euler, label="Standard Euler")
ax1.plot(t_arr, x_modified, label="Modified Euler")

ax1.set_title("Euler Methods vs Exact Solution")
ax1.set_xlabel("Time, t")
ax1.set_ylabel("x(t)")
ax1.legend()
ax1.grid(True)

# Errors
ax2.plot(t_arr, error_euler, label="Standard Euler")
ax2.plot(t_arr, error_modified, label="Modified Euler")

ax2.set_title("Numerical Error")
ax2.set_xlabel("Time, t")
ax2.set_ylabel("Absolute Error")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()