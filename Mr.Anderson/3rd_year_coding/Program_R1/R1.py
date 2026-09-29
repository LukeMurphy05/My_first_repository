# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# define the nonlinear derivative function
def nonlinear1(t, y, a , b):
    return -a * y**3 + b +np.sin(t)


def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """
    parameter_sets = [(1,1),(0.5,1),(1,2)]
    # define the initial variables
    y0 = np.array([0])  # initial state at t = 0
    t0 = 0  # initial time
    tf = 20  # final time
    n = 101  # Number of points at which output will be evaluated (note 101 points are needed for 100 spaces)
    # Note: this does not mean the integrator will take only n steps SciPy
    # will control this to control the error in the solution

    # create a numpy array of n times linearly spaced between t0 and tf
    t = np.linspace(t0, tf, n)

    # Call the RK integrator and return the solution in the array "result"
    # Note that because the brackets aren't closed, the method integrate.solve_ivp()
    # behaves as though it was on just one line.
    for a,b in parameter_sets:
        result = integrate.solve_ivp(fun=nonlinear1,  # The function defining the derivative
                                 t_span=(t0, tf),  # Initial and final times
                                 y0=y0,  # Initial state
                                 method="RK45",  # Integration method
                                 t_eval=t,
                                 args=(a,b)
                                 ) 
        plt.plot(result.t, result.y[0], label=f"a={a}, b={b}") # Time points for result to be reported

    plt.title("Solutions of dy/dt = -ay^3 + b sin(t)")
    plt.xlabel("Time, t")
    plt.ylabel("Solution, y(t)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()