a, b = input('Введите число 1: '), input('Введите число 2: ')   #Ввод чисел

while type(a) != int:                                           #обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильный ввод числа')
        a = input('Введите число 1: ')

while type(b) != int:                                           #Обработка исключений
    try:
        b = int(b)
    except ValueError:
        print('Неправильный ввод числа')
        b = input('Введите число 2: ')

if a % 2 == 1 and b % 2 == 1:
    print('Это нечётные числа')
else:
    print('Это чётные числа')
print('Программа успешно завершена!')
