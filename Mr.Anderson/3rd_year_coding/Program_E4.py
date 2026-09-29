import matplotlib.pyplot as plt
import numpy as np

dt = 0.05
x = 0
y = 1
t = 0
t_max = 10*np.pi

x_arr = np.array([])
y_arr = np.array([])
t_arr = np.array([])

def dx_func(x, y, t):
    return y

def dy_func(x, y, t):
    return -x 

while t < t_max:
    x_old = x 
    y_old = y

    xinit = x_old+dt*y_old
    yinit = y_old-dt*x_old

    x = x_old + 0.5*dt*(y_old+ yinit)
    y = y_old - 0.5*dt*(x_old + xinit)

    t = t +dt 

    x_arr = np.append(x_arr ,x)
    y_arr = np.append(y_arr, y)
    t_arr = np.append(t_arr, t)

x_exact = np.sin(t_arr)
y_exact = np.cos(t_arr)

difference = np.abs(x_arr - x_exact)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(t_arr, x_arr, label="Modified Euler")
ax1.plot(t_arr, x_exact, 'r--', label="Exact")

ax1.set_title("Modified Euler vs Exact")
ax1.set_xlabel("Time, t")
ax1.set_ylabel("x(t)")
ax1.legend()
ax1.grid(True)

ax2.plot(t_arr, difference)

ax2.set_title("Numerical Error")
ax2.set_xlabel("Time, t")
ax2.set_ylabel("|Euler - Exact|")
ax2.grid(True)

plt.tight_layout(w_pad=3)
plt.show()


