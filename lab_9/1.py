def read_matrix_from_file(file_path):
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            matrix.append([int(element) for element in line.strip().split(',')])  
    return matrix

def get_sum_min_max(matrix):
    total = 0
    min_element = 10**100
    max_element = -10**100
    for row in matrix:
        for element in row:
            total += element
            min_element = min(min_element, element)
            max_element = max(max_element, element)
    return total, min_element, max_element

matrix = read_matrix_from_file("output_matrix.txt")

total, min_element, max_element = get_sum_min_max(matrix)

print('\nMatrix:')
for row in matrix:
    print(*row)

print(f'\nSum elements of matrix: {total}')
print(f'Min element: {min_element}')
print(f'Max element: {max_element}')