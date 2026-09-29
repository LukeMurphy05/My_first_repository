import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def driven_pendulum(t, y, A, b, omega0, omega_d):
    x, v = y

    dxdt = v
    dvdt = -b*v - (omega0**2)*x - A*np.sin(omega_d*t)

    return np.array([dxdt, dvdt])


# Parameters
A = 1
omega0 = 1

t0 = 0
tf = 100

x0 = 0
v0 = 0
y0 = np.array([x0, v0])

# Time points
n = 1000
t_eval = np.linspace(0.8*tf, tf, n)

# Driving frequencies
driving_frequencies = np.linspace(0, 2*omega0, 100)

# Five damping coefficients
damping_coefficients = [0.05, 0.1, 0.2, 0.5, 0.8]


# Outer loop: different damping coefficients
for b in damping_coefficients:

    amplitudes = []

    # Inner loop: different driving frequencies
    for omega_d in driving_frequencies:

        lfun = lambda t, y: driven_pendulum(
            t, y, A, b, omega0, omega_d
        )

        result = integrate.solve_ivp(
            fun=lfun,
            t_span=(t0, tf),
            y0=y0,
            method="RK45",
            t_eval=t_eval
        )

        x = result.y[0]

        # Calculate amplitude
        amplitude = (np.max(x) - np.min(x)) / 2
        amplitudes.append(amplitude)

    # Plot this damping coefficient
    plt.plot(
        driving_frequencies,
        amplitudes,
        label=f"b = {b}"
    )


plt.xlabel("Driving frequency, $\omega_d$")
plt.ylabel("Amplitude")
plt.title("Amplitude of Resonance for Different Damping")
plt.legend()
plt.grid()
plt.tight_layout()

plt.savefig("Oscillator-freq-multi.pdf", bbox_inches="tight")

plt.show()