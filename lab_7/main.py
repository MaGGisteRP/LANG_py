import json
import csv
import os
import sys

def json_to_csv(json_filename):
    # Определить имя CSV-файла из имени JSON-файла
    csv_filename = os.path.splitext(json_filename)[0] + ".csv"

    # Открыть JSON-файл и загрузить его содержимое
    with open(json_filename, "r") as json_file:
        data = json.load(json_file)

    # Открыть CSV-файл для записи
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Записать заголовок CSV-файла (ключи из первой записи JSON)
        writer.writerow(data[0].keys())

        # Записать каждую запись JSON в CSV-файл
        for entry in data:
            writer.writerow(entry.values())

    print(f"Файл {csv_filename} успешно создан.")

# Получить имя JSON-файла из аргументов командной строки
json_filename = sys.argv[1]

# Запустить преобразование JSON в CSV
json_to_csv(json_filename)

