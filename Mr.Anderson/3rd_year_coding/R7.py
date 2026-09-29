import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# --------------------------------------------------
# Driven oscillator derivative function
# --------------------------------------------------

def driven_pendulum(t, y, b, omega0, omega_d):

    x, v = y

    dxdt = v
    dvdt = -b*v - (omega0**2)*x - A*np.sin(omega_d*t)

    dydt = np.array([dxdt, dvdt])

    return dydt


# --------------------------------------------------
# Parameters
# --------------------------------------------------

A = 1
b = 0.2
omega0 = 1

t0 = 0
tf = 100

x0 = 0
v0 = 0

y0 = np.array([x0, v0])


# --------------------------------------------------
# Time array
# --------------------------------------------------

# Only use the final 20% of the simulation
n = 1000

t = np.linspace(0.8*tf, tf, n)


# --------------------------------------------------
# Driving frequencies
# --------------------------------------------------

driving_freq = np.linspace(0, 2*omega0, 100)


# --------------------------------------------------
# Store amplitudes
# --------------------------------------------------

amplitudes = []


# --------------------------------------------------
# Loop through driving frequencies
# --------------------------------------------------

for omega_d in driving_freq:

    # Lambda function
    lfun = lambda t, y: driven_pendulum(
        t, y, b, omega0, omega_d
    )

    # Solve the differential equation
    result = integrate.solve_ivp(
        fun=lfun,
        t_span=(t0, tf),
        y0=y0,
        method="RK45",
        t_eval=t
    )

    # Extract x and v
    t_result = result.t
    x = result.y[0]
    v = result.y[1]

    # Measure amplitude from final 20%
    amplitude = (np.max(x) - np.min(x)) / 2

    amplitudes.append(amplitude)


# --------------------------------------------------
# Plot resonance curve
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    driving_freq,
    amplitudes,
    label=f"A={A}, b={b}, omega0={omega0}"
)

plt.xlabel(r"Driving frequency, $\omega_d$")
plt.ylabel("Amplitude")
plt.title("Resonance Curve")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()  