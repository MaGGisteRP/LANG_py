import numpy as np

def run_length_encoding(x):
    x_unique = np.unique(x)  # Получаем значения из входного вектора
    counts = np.diff(np.where(np.concatenate(([x[0]], x[:-1] != x[1:], [True])))[0])[::2]  # Считаем длины серий
    return x_unique, counts

x = np.array([2, 2, 2, 3, 3, 3, 5])
result = run_length_encoding(x)
print(result)