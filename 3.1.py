def compress_string(line):
    compressed_string = ""
    the_current_character = line[0]
    counter = 1

    for symbol in line[1:]:
        if symbol == the_current_character:
            counter += 1
        else:
            if counter > 1:
                compressed_string += the_current_character + str(counter)
            else:
                compressed_string += the_current_character
            the_current_character = symbol
            counter = 1

    # Обработка последнего символа
    if counter > 1:
        compressed_string += the_current_character + str(counter)
    else:
        compressed_string += the_current_character

    return compressed_string

source_string = "YYYYggkeeeAAABV"
compressed_string = compress_string(source_string)
print(compressed_string)