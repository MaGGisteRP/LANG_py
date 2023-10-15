def swap_max_min(input_list):
    if not input_list:
        return input_list  # Если список пустой, ничего не меняем

    # Находим индексы наибольшего и наименьшего элементов
    max_index = input_list.index(max(input_list))
    min_index = input_list.index(min(input_list))

    # Меняем местами элементы по найденным индексам
    input_list[max_index], input_list[min_index] = input_list[min_index], input_list[max_index]

    return input_list

input_list = [4, 2, 9, 1, 7]
result_list = swap_max_min(input_list)
print(result_list)