import numpy as np
import matplotlib.pyplot as plt

N_initial = 10
tau = 2
dt = 1
t = np.arange(0, 10 + dt, dt)

N_exact = N_initial * np.exp(-t / tau)

N_euler = np.empty_like(t)
N_euler[0] = N_initial
for i in range(1, len(t)):
    N_euler[i] = N_euler[i-1] - (dt / tau) * N_euler[i-1]

def new_func(t, N_exact, N_euler, i):
    print(f"{t[i]:.2f}  {N_exact[i]:.6f}  {N_euler[i]:.6f}")

for i in range(len(t)):
    new_func(t, N_exact, N_euler, i)

plt.plot(t, N_exact, label="Exact")
plt.plot(t, N_euler, '--', label="Euler")
plt.xlabel("Time")
plt.ylabel("N(count)")
plt.title("N vs t (1 step)")
plt.legend()
plt.show()

print("max error:", np.max(np.abs(N_exact - N_euler)))