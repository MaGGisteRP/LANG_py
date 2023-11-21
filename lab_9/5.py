import numpy as np
from scipy.stats import multivariate_normal
import time
def logpdf_multivariate(X, m, C):
    N, D = X.shape
    diff = X - m
    inv_cov = np.linalg.inv(C)
    det_cov = np.linalg.det(C)
    log_prefactor = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_cov)
    exponents = -0.5 * np.sum(np.dot(diff, inv_cov) * diff, axis=1)
    log_probs = log_prefactor + exponents
    return log_probs

# Заданные параметры
N = 1000  # Количество точек
D = 3  # Размерность
m = np.array([1, 2, 3])  # Мат. ожидание
C = np.array([[2, 0, 0], [0, 1, 0], [0, 0, 0.5]])  # Матрица ковариаций

# Генерация случайных точек
X = np.random.randn(N, D)

# Вычисление логарифма плотности с использованием нашей функции
log_probs_custom = logpdf_multivariate(X, m, C)

# Сравнение со значениями, полученными с помощью scipy.stats.multivariate_normal
log_probs_scipy = multivariate_normal(m, C).logpdf(X)

# Сравнение скорости работы
start = time.time()
log_probs_custom = logpdf_multivariate(X, m, C)
end = time.time()
print("Custom function time: ", end - start)

start = time.time()
log_probs_scipy = multivariate_normal(m, C).logpdf(X)
end = time.time()
print("Scipy function time: ", end - start)


# Сравнение точности вычислений
comparison = np.allclose(log_probs_custom, log_probs_scipy)
print("The arrays are " + ("the same" if comparison else
         "not the same") + " within a tolerance.")
