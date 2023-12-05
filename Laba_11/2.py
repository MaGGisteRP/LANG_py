import numpy as np
import matplotlib.pyplot as plt

# Устанавливаем сид для воспроизводимости результатов
np.random.seed(0)

# Генерируем 1000 случайных чисел из нормального распределения
mu = 0  # среднее значение
sigma = 1  # стандартное отклонение
sample_size = 1000  # размер выборки
data = np.random.normal(mu, sigma, sample_size)

# Отрисовка гистограммы
plt.hist(data, bins=30, density=True, alpha=0.7, color='steelblue', edgecolor='black')

# Добавление названий осей и заголовка графика
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма нормального распределения')

plt.show()