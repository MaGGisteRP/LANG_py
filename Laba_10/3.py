import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

t = np.linspace(0, 2*np.pi, 100)  # Time parameter
a_ratio = np.linspace(0, 1, 100)  # Frequency ratio parameter
x = np.sin(2*np.pi*a_ratio*t + 0)  # x-component of Lissajous figure
y = np.sin(2*np.pi*t + 0)  # y-component of Lissajous figure

def update(frame):
    ax.clear()
    ax.plot(x[frame], y[frame], color='blue')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_title('Lissajous Figure')

anim = FuncAnimation(fig, update, frames=len(a_ratio), interval=100)

plt.show()