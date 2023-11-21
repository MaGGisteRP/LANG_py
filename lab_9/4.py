import numpy as np

def find_max_after_zero(x):
    max_element = None
    found_zero = False

    for element in x:
        if element == 0:
            found_zero = True
        elif found_zero:
            if max_element is None or element > max_element:
                max_element = element
            found_zero = False

    return max_element

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
result = find_max_after_zero(x)
print(result)