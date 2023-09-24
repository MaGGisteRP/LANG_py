def pyramid_pattern(n):
    for i in range(1, n + 1):

        for j in range(n - i, 0, -1):
            print(" ", end="")

        for k in range(1, i + 1):
            print(k, end="")

        for k in range(i - 1, 0, -1):
            print(k, end="")

        print()


n = int(input("Введите натуральное N: "))
pyramid_pattern(n)