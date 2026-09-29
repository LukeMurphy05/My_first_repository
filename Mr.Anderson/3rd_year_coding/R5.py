import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

from R4_function import damped_pendulum


# Parameters
b = 0.1
omega0 = 1

h = 0.01
t0 = 0
tf = 20

# Initial conditions
x0 = 0
v0 = 1

# Initial state
y0 = np.array([x0, v0])

# Time points
t = np.linspace(t0, tf , int((tf-t0)/h)+1)


# Lambda function
lfun = lambda t, y: damped_pendulum(t, y, b, omega0)


# Solve the ODE
result = integrate.solve_ivp(
    fun=lfun,
    t_span=(t0, tf),
    y0=y0,
    method="RK45",
    t_eval=t
)


# Extract x and v from the result
x = result.y[0]
v = result.y[1]


# Plotting
fig, ax = plt.subplots(1, 2, figsize=(12, 5))


# x and v versus time
ax[0].plot(t, x, label="x(t)")
ax[0].plot(t, v, label="v(t)")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("x, v")
ax[0].set_title("Damped Oscillator")
ax[0].legend()
ax[0].grid()


# Phase space plot
ax[1].plot(x, v)
ax[1].set_xlabel("x")
ax[1].set_ylabel("v")
ax[1].set_title("Phase Space")
ax[1].grid()


plt.tight_layout()
plt.show()