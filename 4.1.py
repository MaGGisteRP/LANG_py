def find_greater_elements(input_list):
    result = []
    for i in range(1, len(input_list)):
        if input_list[i] > input_list[i - 1]:
            result.append(input_list[i])
    return result

input_list = [2, 4, 1, 7, 5, 9, 3]
result_list = find_greater_elements(input_list)
print(result_list)