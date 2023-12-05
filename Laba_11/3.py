import csv
import matplotlib.pyplot as plt

# Создаем пустой список для хранения данных
data = []

# Открываем файл и считываем данные
with open('passengers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        data.append(int(row[1]))

# График пассажиропотока за все время
plt.plot(data)
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.title('Пассажиропоток за все время')
plt.show()

# Распределение пассажиров по месяцам в 1951-1955 гг. (гистограмма)
years = []
months = []
passengers = []

# Отбираем данные за указанный период
for row in reader:
    if '1951' <= row[0][:4] <= '1955':
        years.append(row[0][:4])
        months.append(row[0][5:])
        passengers.append(int(row[1]))

# Строим гистограмму
plt.bar(months, passengers)
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.title('Распределение пассажиров по месяцам в 1951-1955 гг.')
plt.show()