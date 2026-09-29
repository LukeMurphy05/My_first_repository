import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# --------------------------------------------------
# Derivative function for the driven oscillator
# --------------------------------------------------

def driven_pendulum(t, y, A, b, omega0, omega_d):

    x, v = y

    dxdt = v
    dvdt = -b*v - (omega0**2)*x - A*np.sin(omega_d*t)

    dydt = np.array([dxdt, dvdt])

    return dydt


# --------------------------------------------------
# Parameters
# --------------------------------------------------

A = 1.5
b = 0.2
omega0 = 0.5

t0 = 0
tf = 100
h = 0.01

x0 = 0
v0 = 0

y0 = np.array([x0, v0])

t = np.linspace(t0, tf, int((tf-t0)/h) + 1)


# --------------------------------------------------
# Plot solutions for different driving frequencies
# --------------------------------------------------

omega_d_values = [0.5, 1.0, 1.5]

fig, ax = plt.subplots(1, 2, figsize=(13, 5))

for omega_d in omega_d_values:

    # Lambda function
    lfun = lambda t, y: driven_pendulum(
        t, y, A, b, omega0, omega_d
    )

    # Solve the ODE
    result = integrate.solve_ivp(
        fun=lfun,
        t_span=(t0, tf),
        y0=y0,
        method="RK45",
        t_eval=t
    )

    x = result.y[0]
    v = result.y[1]

    # Plot displacement against time
    ax[0].plot(
        t,
        x,
        label=r"$\omega_d=$" + str(omega_d)
    )

    # Plot phase space
    ax[1].plot(
        x,
        v,
        label=r"$\omega_d=$" + str(omega_d)
    )


# --------------------------------------------------
# First plot
# --------------------------------------------------

ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Displacement, x")
ax[0].set_title(
    "Driven Damped Oscillator\n"
    + f"A={A}, b={b}, omega0={omega0}"
)
ax[0].legend()
ax[0].grid()


# --------------------------------------------------
# Second plot
# --------------------------------------------------

ax[1].set_xlabel("x")
ax[1].set_ylabel("v")
ax[1].set_title("Phase Space")
ax[1].legend()
ax[1].grid()


plt.tight_layout()
plt.show()


# --------------------------------------------------
# Resonance investigation
# --------------------------------------------------

omega_d_array = np.linspace(0.2, 2.0, 100)

# Different damping values
b_values = [0.1, 0.2, 0.4]

plt.figure(figsize=(8, 5))

for b_current in b_values:

    amplitudes = []

    for omega_d in omega_d_array:

        # Lambda function
        lfun = lambda t, y: driven_pendulum(
            t, y, A, b_current, omega0, omega_d
        )

        # Solve the ODE
        result = integrate.solve_ivp(
            fun=lfun,
            t_span=(t0, tf),
            y0=y0,
            method="RK45",
            t_eval=t
        )

        x = result.y[0]

        # Only use the final part of the simulation
        # so the initial transient has mostly disappeared
        start = int(0.8 * len(x))

        x_steady = x[start:]

        # Estimate amplitude
        amplitude = (np.max(x_steady) - np.min(x_steady)) / 2

        amplitudes.append(amplitude)

    # Plot amplitude against driving frequency
    plt.plot(
        omega_d_array,
        amplitudes,
        label=f"b={b_current}"
    )


# --------------------------------------------------
# Resonance plot formatting
# --------------------------------------------------

plt.axvline(
    omega0,
    linestyle="--",
    label=r"$\omega_0$"
)

plt.xlabel(r"Driving frequency, $\omega_d$")
plt.ylabel("Steady-state amplitude")
plt.title(
    f"Resonance of Driven Oscillator\n"
    f"A={A}, omega0={omega0}"
)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()