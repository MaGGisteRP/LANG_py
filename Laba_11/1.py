import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# Параметры сигнала
frequency = 1  # Частота сигнала (1 Гц)
sampling_rate = 1000  # Частота дискретизации (1000 Гц)
signal_length = 1  # Длительность сигнала (1 секунда)
t = np.linspace(0, signal_length, int(signal_length * sampling_rate), endpoint=False)  # Вектор времени

# Генерация прямоугольного сигнала
a = 0.25  # Начало прямоугольного сигнала (в долях от длительности сигнала)
b = 0.75  # Конец прямоугольного сигнала (в долях от длительности сигнала)
x = np.array([1 if a <= i < b else 0 for i in t])

# Отрисовка сигнала
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Rectangular Signal')
plt.grid(True)
plt.show()