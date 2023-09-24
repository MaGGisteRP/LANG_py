num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

count = 0

if num1 == num2:
    count += 1
if num1 == num3:
    count += 1
if num2 == num3:
    count += 1

if count == 3:
    print("Результат: 3 - все числа совпадают")
elif count == 2:
    print("Результат: 2 - два числа совпадают")
else:
    print("Результат: 0 - все числа различны")
