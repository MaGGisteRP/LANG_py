def sort_and_write_numbers():
    # открываю файл
    with open('input2.txt', 'r') as file:
        # читаю строки, преобразую в int и сохраняю в списке
        numbers = [int(line.strip()) for line in file]

    # Сотртирую список
    numbers.sort()

    # открываю выходной файл
    with open('output.txt', 'w') as file:
        # Записываю числа в выходной
        for number in numbers:
            file.write(f'{number}\n')

# Позвонил функции
sort_and_write_numbers()
