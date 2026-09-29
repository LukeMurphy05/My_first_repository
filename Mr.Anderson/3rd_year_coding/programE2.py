import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tmax = 50
h = 0.01

x0 = [3, 1, 0, -0.7, -0.75]

n_steps = int((tmax - t0)/h) + 1
t = np.linspace(t0, tmax, n_steps)


def f(x, t):
    return t - x**2


for x_initial in x0:

    x = np.empty(n_steps)
    x[0] = x_initial

    for i in range(n_steps - 1):
        x[i+1] = x[i] + h*f(x[i], t[i])

    plt.plot(t, x, label=f'x0 = {x_initial}')

plt.title("Non-Linear Euler Example")
plt.xlabel("t")
plt.ylabel("x")
plt.xlim(0,50)
plt.ylim(-10,10)
plt.grid()
plt.legend()
plt.show()