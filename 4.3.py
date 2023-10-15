def count_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return len(common_elements)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_count = count_common_elements(list1, list2)
print("Количество общих элементов:", common_count)