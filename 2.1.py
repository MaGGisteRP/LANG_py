def create_sierpinski(level, triangle):
    if level == 0:
        return triangle
    else:
        length = len(triangle)
        top = create_sierpinski(level - 1, triangle)
        middle = create_sierpinski(level - 1, [row + ' ' * length + row for row in triangle])
        bottom = create_sierpinski(level - 1, triangle)
        return top + middle + bottom

# Initial triangle
base_triangle = ['  *  ', ' * * ', '*****']

# Generate Sierpinski triangle
sierpinski_triangle = create_sierpinski(5, base_triangle)

# Print Sierpinski triangle
for row in sierpinski_triangle:
    print(row)