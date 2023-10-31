import json
import csv

def json_to_csv(json_file):
    with open(json_file, 'r', encoding='utf-8') as json_file: #блок открывает JSON-файл для чтения. Файл читается с кодировкой UTF-8, чтобы обеспечить правильное чтение кириллических символов.
        data = json.load(json_file) #загружает содержимое JSON-файла и сохраняет его в переменной data.

    name = str(list(data.keys())[0])
    filename = name + '.csv'
    data = list(data.values())[0]

    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file) # содаём переменную связанную с файлом
        csv_writer.writerow(data[0].keys()) # запись заголовков
        for i in data:
            csv_writer.writerow(i.values())

json_file = input("Введите имя JSON файла: ")
json_to_csv(json_file)