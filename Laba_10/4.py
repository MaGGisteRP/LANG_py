import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the initial wave parameters
initial_frequency1 = 1.0
initial_amplitude1 = 1.0
initial_frequency2 = 2.0
initial_amplitude2 = 0.5

# Generate x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 1000)

# Generate the initial waves (sinusoidal waves)
wave1 = initial_amplitude1 * np.sin(initial_frequency1 * x)
wave2 = initial_amplitude2 * np.sin(initial_frequency2 * x)

# Create the plot figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))
plt.subplots_adjust(left=0.1, bottom=0.4)

# Plot the initial waves
wave1_line, = ax1.plot(x, wave1, 'r-', label='Wave 1')
wave2_line, = ax2.plot(x, wave2, 'b-', label='Wave 2')

# Add legends and titles to the subplots
ax1.legend()
ax2.legend()
ax1.set_title('Wave 1: Amplitude = {:.2f}, Frequency = {:.2f}'.format(initial_amplitude1, initial_frequency1))
ax2.set_title('Wave 2: Amplitude = {:.2f}, Frequency = {:.2f}'.format(initial_amplitude2, initial_frequency2))

# Plot the resulting wave (sum of wave1 and wave2)
resultant_line, = ax3.plot(x, wave1 + wave2, 'g-', label='Resultant Wave')
ax3.set_title('Resultant Wave')

# Create sliders for interactive adjustments
slider_frequency1 = Slider(ax=ax1, label='Frequency 1', valmin=0.1, valmax=5, valinit=initial_frequency1)
slider_amplitude1 = Slider(ax=ax1, label='Amplitude 1', valmin=0, valmax=2, valinit=initial_amplitude1)
slider_frequency2 = Slider(ax=ax2, label='Frequency 2', valmin=0.1, valmax=5, valinit=initial_frequency2)
slider_amplitude2 = Slider(ax=ax2, label='Amplitude 2', valmin=0, valmax=2, valinit=initial_amplitude2)


# Function to be called when sliders are changed
def update(val):
    frequency1 = slider_frequency1.val
    amplitude1 = slider_amplitude1.val
    frequency2 = slider_frequency2.val
    amplitude2 = slider_amplitude2.val

    # Update the waves
    wave1 = amplitude1 * np.sin(frequency1 * x)
    wave2 = amplitude2 * np.sin(frequency2 * x)

    # Update the plot
    wave1_line.set_ydata(wave1)
    wave2_line.set_ydata(wave2)
    resultant_line.set_ydata(wave1 + wave2)

    # Update subplot titles
    ax1.set_title('Wave 1: Amplitude = {:.2f}, Frequency = {:.2f}'.format(amplitude1, frequency1))
    ax2.set_title('Wave 2: Amplitude = {:.2f}, Frequency = {:.2f}'.format(amplitude2, frequency2))

    # Redraw the plot
    fig.canvas.draw()


# Connect the sliders to their update functions
slider_frequency1.on_changed(update)
slider_amplitude1.on_changed(update)
slider_frequency2.on_changed(update)
slider_amplitude2.on_changed(update)

# Display the plot
plt.show()