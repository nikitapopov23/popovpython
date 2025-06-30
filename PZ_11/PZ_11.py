# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Количество четных элементов:
# Среднее арифметическое:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма положительных элементов:

import random

# Функция для создания файла с последовательностью целых чисел
def create_file(filename, numbers):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")


positive_numbers = [random.randint(1, 100) for _ in range(10)]  

create_file('positive_numbers.txt', positive_numbers)
create_file('negative_numbers.txt', negative_numbers)


with open('positive_numbers.txt', 'r') as f:
    positives = [int(line.strip()) for line in f.readlines()]

even_numbers = [num for num in positives if num % 2 == 0]
count_even = len(even_numbers)
average_even = sum(even_numbers) / count_even if count_even > 0 else 0


with open('negative_numbers.txt', 'r') as f:
    negatives = [int(line.strip()) for line in f.readlines()]

odd_numbers = [num for num in negatives if num % 2 != 0]
count_odd = len(odd_numbers)
sum_positive = sum(num for num in positives if num > 0)


with open('results.txt', 'w') as f:
    f.write("Содержимое первого файла:\n")
    f.write("Четные элементы: " + ', '.join(map(str, even_numbers)) + '\n')
    f.write("Количество четных элементов: " + str(count_even) + '\n')
    f.write("Среднее арифметическое: " + str(average_even) + '\n\n')

    f.write("Содержимое второго файла:\n")
    f.write("Нечетные элементы: " + ', '.join(map(str, odd_numbers)) + '\n')
    f.write("Количество нечетных элементов: " + str(count_odd) + '\n')
    f.write("Сумма положительных элементов: " + str(sum_positive) + '\n')

print("Файлы созданы и обработаны.")