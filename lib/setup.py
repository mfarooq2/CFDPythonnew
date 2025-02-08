import numpy
from matplotlib import pyplot

def setup_grid(nx, dx):
    """
    Sets up the grid parameters

    Args:
        nx: number of grid points
        dx: spatial step
    """
    dx = 2 / (nx - 1)
    return dx


def setup_initial_conditions(nx, dx):
    """
    Sets up the initial conditions for the problem

    Args:
        nx: number of grid points
        dx: spatial step
    """
    u = numpy.ones(nx)
    u[int(.5 / dx):int(1 / dx + 1)] = 2
    return u

def setup_time_steps(nt, dt):
  """
  Sets up the time step parameters

  Args:
    nt: number of time steps
    dt: size of each time step
  """
  return nt, dt
