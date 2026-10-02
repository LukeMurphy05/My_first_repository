# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    
    #simple harmonic stuff
    x, v = np.meshgrid(coords, coords)
    omega = 1
    dx = x
    dy = -omega**2*v
    z = dx+dy

    #complex harmonic stuff
    b = 1
    dx_damped = x
    dy_damped = -b*v - omega**2*x
    z_damped = dx_damped+dy_damped


    #plotting
    fig,ax = plt.subplots(1,2,figsize=(12,5))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D Vector field: $f(x,y)=(-1-x^2+y, 1+x-y^2)$')
    
    ax[0].quiver(x, v, dx, dy)  # plot field as quiver
    ax[0].contourf(x,v,z,25,cmap='coolwarm_r')
    ax[0].streamplot(x, v, dx, dy)  # plot streamlines of field.
    ax[0].set_title(f'simple harmonic plot, w(omega) = {omega}')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')

    ax[1].quiver(x,v,dx_damped,dy_damped)
    ax[1].streamplot(x,v,dx_damped,dy_damped)
    ax[1].contourf(x,v,z_damped,25,cmap='coolwarm_r')
    ax[1].set_title(f'damped harmonic plot, b = {b}')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('y')
    
    plt.tight_layout()
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main() 