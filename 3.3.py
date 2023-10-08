import sys

a, b, c, d = int(input()), 0, 0, 0
d = a%10

c = (a//10)%10

b = a//100

d_dict = dict([(1, 'один'), (2, 'два'), (3, 'три'), (4, 'четыре'), (5, 'пять'), (6, 'шесть'), (7, 'семь'),
                (8, 'восемь'), (9, 'девять'), (0, '')])
c_dict = dict([(2, 'двадцать'), (3, 'тридцать'), (4, 'сорок'), (5, 'пятьдесят'), (6, 'шестьдесят'),
                (7, 'семьдесят'), (8, 'восемьдесят'), (9, 'девяносто'), (0, '')])
b_dict = dict([(1, 'сто'), (2, 'двести'), (3, 'триста'), (4, 'четыреста'), (5, 'пятьсот'), (6, 'шестьсот'),
                (7, 'семьсот'), (8, 'восемьсот'), (9, 'девятьсот'), (0, '')])

if a == 0:
    print('ноль')
    sys.exit()
elif a == 10:
    print('десять')
    sys.exit()
elif a == 11:
    print('одиннадцать')
    sys.exit()
elif a == 12:
    print('двенадцать')
    sys.exit()
elif a == 13:
    print('тринадцать')
    sys.exit()
elif a == 14:
    print('четырнадцать')
    sys.exit()
elif a == 15:
    print('пятнадцать')
    sys.exit()
elif a == 16:
    print('шестнадцать')
    sys.exit()
elif a == 17:
    print('семнадцать')
    sys.exit()
elif a == 18:
    print('восемьнадцать')
    sys.exit()
elif a == 19:
    print('девятнадцать')
    sys.exit()

if b != 0 and c != 0 and d != 0:
    print(b_dict[b] + ' ' + c_dict[c] + ' ' + d_dict[d])
elif b == 0 and c != 0 and d != 0:
    print(c_dict[c] + ' ' + d_dict[d])
else:
    print(d_dict[d])