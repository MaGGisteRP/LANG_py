def num(nl):
    # список в набор
    ns = set(nl)
    # возвращает длину
    return len(ns)

print(num([1, 2, 3, 2, 1]))
print(num([1, 2, 3, 4, 5, 6, 7]))
print(num([1, 1, 1, 1, 1]))
print(num([1, 2, 3, 1, 1]))