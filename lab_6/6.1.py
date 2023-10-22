def read_and_write():
    # Открываю и считаю
    with open("input.txt", "r") as infile:
        numbers = infile.readline().split()
        # преобразовываю в целые
        numbers = [int(n) for n in numbers]

    product = 1
    for number in numbers:
        product *= number

    # Запеисываю в файл
    with open("output.txt", "w") as outfile:
        outfile.write(str(product))

# Алло?
read_and_write()
