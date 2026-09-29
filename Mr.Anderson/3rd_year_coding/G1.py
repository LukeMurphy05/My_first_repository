# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """
    x_pos = 0.9
    y_pos =0.9
    key_size =2 

    plt.close()
    x_values = np.linspace(0,2*np.pi,101)
    y_values = np.linspace(0,2*np.pi,101)
    x, y = np.meshgrid(x_values, y_values)
    vx = np.cos(x)*y
    vy = np.sin(y)*x
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal',adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example of a quiver plot')
    q=plt.quiver(x[::5,::5], y[::5,::5], vx[::5,::5] ,vy[::5,::5], pivot='mid', label='$v_x$ = cos($x$), $v_y$ = sin($y$)')
    plt.quiverkey(q,x_pos,y_pos, key_size,r'$2\frac{m}{s}$', labelpos = 'E', coordinates='figure')
    plt.legend()
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()