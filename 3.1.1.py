def recover_string(compressed_string):
    source_string = ""
    index = 0

    while index < len(compressed_string):
        symbol = compressed_string[index]
        index += 1

        if index < len(compressed_string) and compressed_string[index].isdigit():
            repetitions = int(compressed_string[index])
            index += 1
        else:
            повторения = 1

        source_string += symbol * repetitions

    return source_string

# Пример использования:
compressed_string = "Y4g2ke3A3BV"
source_string = recover_string(compressed_string)
print(source_string)