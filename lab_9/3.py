import numpy as np

# Генерирование массива случайных чисел нормального распределения 10x4
arr = np.random.normal(size=(10, 4))

# Поиск минимального значения
min_val = np.min(arr)

# Поиск максимального значения
max_val = np.max(arr)

# Поиск среднего значения
mean_val = np.mean(arr)

# Поиск стандартного отклонения
std_dev = np.std(arr)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = arr[:5]

print("Массив случайных чисел:\n", arr)
print("Минимальное значение:", min_val)
print("Максимальное значение:", max_val)
print("Среднее значение:", mean_val)
print("Стандартное отклонение:", std_dev)
print("Первые 5 строк:\n", first_five_rows)