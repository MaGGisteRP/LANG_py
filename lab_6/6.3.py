class Child:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
# cоздаем дочерний класс для хранения отдельных дочерних данных
def parse_data(from_file):
    children = []
    with open(from_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(' ')
            children.append(Child(data[0], data[1], int(data[2])))
    return(children)
# читаем строки, создаем дочерний объект и сохраняем в массиве
def extract_youngest_oldest(children, youngest_file, oldest_file):
    children.sort(key=lambda x: x.age)
# сортируем список по возрасту

    with open(youngest_file, 'w') as f:
        f.write(children[0].surname + " " + children[0].name
                + " " +  str(children[0].age))
# сортировка по возрасту и сохранение младшего
    with open(oldest_file, 'w') as f:
        f.write(children[-1].surname + " " + children[-1].name
                + " " +  str(children[-1].age))
# сортировка по возрасту и сохранение мнимого чела)
def main():
    children = parse_data('input3.txt')
    extract_youngest_oldest(children, 'youngest.txt', 'oldest.txt')
# звоню функции, а она берет трубку
if __name__ == "__main__":
    main()