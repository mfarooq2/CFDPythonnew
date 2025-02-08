import numpy
from matplotlib import pyplot

def linear_convection(u, c, dt, dx, nx):
    """
    Performs a single time step update for the linear convection equation.

    Args:
        u: array of values
        c: constant for linear convection
        dt: time step
        dx: spatial step
        nx: number of grid points
    """
    un = numpy.ones(nx)
    for i in range(1, nx):
        un = u.copy()
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
    return u

def linear_convection(u, c, dt, dx, nx, nt):
    """
    Performs multiple time step update for the linear convection equation.

    Args:
        u: array of values
        c: constant for linear convection
        dt: time step
        dx: spatial step
        nx: number of grid points
        nt: number of time steps
    """
    un = numpy.ones(nx)
    for n in range(nt):
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
    return u

def nonlinear_convection(u, dt, dx, nx, nt):
    """
    Performs multiple time step update for the non linear convection equation

    Args:
        u: array of values
        dt: time step
        dx: spatial step
        nx: number of grid points
        nt: number of time steps
    """
    
    for n in range(nt):
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - u[i] * dt / dx * (un[i] - un[i-1])
    return u
