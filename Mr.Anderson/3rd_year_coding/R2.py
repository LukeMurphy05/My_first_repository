# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# This file isn't a complete template, but rather gives an outline of what you need the function to do.
# If you're feeling ambitious, you can keep these functions in a separate file and import them.
# Look up how to do so for yourself, or experiment based on what you see in library imports
import numpy as np
import matplotlib.pyplot as plt

def differential_rl(v, r, l, i):
    """
    Calculates the change in current over time from the formula
    L(dI/dt) = V - Ri
    :param v: Float for voltage
    :param r:
    :param l:
    :param i:
    :return:
    """
    difference = (v-r*i)/l
    return difference

    # complete the docstring
    # do some maths to calculate the difference
    # return the difference
    #pass # this is a placeholder. Replace it with a return value


def exact_solution_rl(v, r, l, t):
    """
    Calculates the change in current over time from the formula
    I = (V/R)(1-exp(-Rt/L))
    :param v: Float for voltage
    :param r:
    :param l:
    :param t:
    :return:
    """
    exact = (v/r)*(1-np.exp(-r*t/l))
    return exact

#parameters
v = 10
r = 50
l = 100

#initial conditions
i = 0
t = 0 

#time parameters
h = 0.1 
t_max = 10

#arrays
t_arr = np.arange(0, t_max +h, h)
i_arr = np.empty_like(t_arr)
i_exact = np.empty_like(t_arr)

i_arr[0]= i

for j in range(1,len(t_arr)):
    di_dt = differential_rl(v,r,l,i)
    i = i + h*di_dt
    i_arr[j]=i

for j in range(len(t_arr)):
    i_exact[j]=exact_solution_rl(r,v,l,t_arr[j])

plt.plot(t_arr, i_arr, label="Euler method")
plt.plot(t_arr, i_exact, label="Exact solution")

plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("RL Circuit: Current vs Time")
plt.legend()
plt.grid()

plt.show()
    # complete the docstring
    # do some maths to calculate the exact solution at a given time
    # return the difference
    #pass # this is a placeholder. Replace it with a return value