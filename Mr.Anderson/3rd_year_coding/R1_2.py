import numpy as np
import matplotlib.pyplot as plt

N_initial = 10
tau = 2

dt_values = [0.01, 0.005, 0.001]

for dt in dt_values:

    t = np.arange(0, 10 + dt, dt)

    N_exact = N_initial * np.exp(-t / tau)

    N_euler = np.empty_like(t)
    N_euler[0] = N_initial

    for i in range(1, len(t)):
        N_euler[i] = N_euler[i-1] - (dt / tau) * N_euler[i-1]

    # Calculate absolute difference
    difference = np.abs(N_exact - N_euler)

    # Print maximum error
    print("dt =", dt)
    print("max error:", np.max(difference))

    # Plot exact and Euler solutions
    plt.figure()
    plt.plot(t, N_exact, label="Exact")
    plt.plot(t, N_euler, '--', label="Euler")

    plt.xlabel("Time")
    plt.ylabel("N(count)")
    plt.title(f"N vs t, dt = {dt}")
    plt.legend()
    plt.grid()
    plt.show()

    # Plot difference
    plt.figure()
    plt.plot(t, difference)

    plt.xlabel("Time")
    plt.ylabel("Absolute difference")
    plt.title(f"Error vs time, dt = {dt}")
    plt.grid()
    plt.show()