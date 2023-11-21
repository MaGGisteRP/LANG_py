import numpy as np

# Загружаем датасет iris
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Берем столбец species
species = iris[:, 4]

# Находим уникальные значения и их количество
unique_species, counts = np.unique(species, return_counts=True)

# Выводим результаты
for us, count in zip(unique_species, counts):
    print(f"{us.decode('utf-8')}: {count}")