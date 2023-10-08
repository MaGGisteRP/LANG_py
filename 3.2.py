from collections import Counter

def count_characters(string):
    # Удаляем пробелы из строки
    string = string.replace(" ", "")
    
    # Используем Counter для подсчета символов
    character_counts = Counter(string)
    
    # Получаем 3 наиболее часто встречающихся символа
    most_common = character_counts.most_common(3)
    
    return most_common

# Получаем строку от пользователя
user_input = input("Введите строку: ")

# Получаем наиболее часто встречающиеся символы
most_common_characters = count_characters(user_input)

# Выводим результат
print("Наиболее часто встречающиеся символы:")
for character, count in most_common_characters:
    print(f"Символ: {character}, Количество: {count}")