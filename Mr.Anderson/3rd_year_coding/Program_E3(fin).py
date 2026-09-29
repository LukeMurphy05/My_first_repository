# %%
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

def dx_func(x,y,t):
    dx = y
    return dx

def dy_func(x,y,t):
    dy = -x
    return dy

while t < t_max:
   dx = dx_func(x,y,t)
   dy = dy_func(x,y,t)
   x = x + dx*dt
   y = y+dy*dt
   t = t+ dt
   x_arr=np.append(x_arr,x)
   y_arr= np.append(y_arr,y)
   t_arr = np.append(t_arr,t)

x_exact = np.sin(t_arr)

difference = np.abs(x_arr - x_exact)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Graph 1: Euler vs exact
ax1.plot(t_arr, x_arr, label="Euler")
ax1.plot(t_arr, x_exact, 'r--', label="Exact")

ax1.set_title("Euler vs Exact Solution")
ax1.set_xlabel("Time, t")
ax1.set_ylabel("x(t)")
ax1.legend(loc='upper right')
ax1.grid(True)

# Graph 2: Error
ax2.plot(t_arr, difference)

ax2.set_title("Numerical Error")
ax2.set_xlabel("Time, t")
ax2.set_ylabel("|Euler - Exact|")
ax2.grid(True)

plt.tight_layout(w_pad=3)
plt.show()