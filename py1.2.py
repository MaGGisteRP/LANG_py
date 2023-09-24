# Вводим натуральное число n
n = int(input("Введите натуральное число n: "))

# Используем числа для создания лестницы
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Вводим натуральное число n
n = int(input("Введите натуральное число n: "))

# Используем строки для создания лестницы
for i in range(1, n + 1):
    staircase = ''.join(str(j) for j in range(1, i + 1))
    print(staircase)