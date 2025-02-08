import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def plot_data(x, u):
    """
    Plots the data.
    """
    plt.plot(x, u)

def animate_data(x,u):
  """
  Animates the data.
  """
  fig = plt.figure()
  ax = fig.add_subplot(111)
  line, = ax.plot(x, u, color='blue')
  plt.close(fig)

  # Create the animation object
  ani = animation.FuncAnimation(fig, animate_data, interval=100, blit=True, repeat=True)
  plt.show()
