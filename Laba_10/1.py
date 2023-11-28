import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 100)  # x-axis values

fig, ax = plt.subplots()

for i in range(1, 8):
    y = legendre(i)(x)  # generate Legendre polynomial for each degree
    ax.plot(x, y, label=f'n = {i}')  # plot the polynomial with a label

ax.set_xlabel('x')
ax.set_ylabel('Pn(x)')
ax.set_title('Legendre Polynomials')
ax.legend()

plt.show()