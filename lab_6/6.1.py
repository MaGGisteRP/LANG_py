def read_and_write():
    # Откройте и считайте числа из входного файла
    with open("input.txt", "r") as infile:
        numbers = infile.readline().split()
        # Преобразовать числа в целые
        numbers = [int(n) for n in numbers]

    product = 1
    for number in numbers:
        product *= number

    # Запишите продукт в выходной файл
    with open("output.txt", "w") as outfile:
        outfile.write(str(product))

# Вызов функции
read_and_write()
