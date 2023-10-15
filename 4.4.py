def count_string_occurrences(input_list):
    # Создаем пустой словарь для подсчета повторений строк
    counts = {}

    # Подсчитываем повторения каждой строки
    for string in input_list:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1

    # Выводим количество повторений каждой строки
    for key, value in counts.items():
        print(value, end=' ')

input_data1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
input_data2 = ['aaa', 'bbb', 'ccc']
input_data3 = ['abc', 'abc', 'abc']

print("1)", end=' ')
count_string_occurrences(input_data1)
print()

print("2)", end=' ')
count_string_occurrences(input_data2)
print()

print("3)", end=' ')
count_string_occurrences(input_data3)