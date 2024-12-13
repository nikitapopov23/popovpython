#Даны два числа. Вывести большее из них.

try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
except ValueError:
    print("Неправильно ввели")

if a > b:
    print(a)
else:
    print(b)

if a == b:
    print("Числа равны")