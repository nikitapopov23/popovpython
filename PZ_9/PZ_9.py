# Вариант 22. Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.

vse = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
chasti = vse.split()

oranges = [int(chasti[1]), int(chasti[2]), int(chasti[3]), int(chasti[4]), int(chasti[5])]
apples = [int(chasti[7]), int(chasti[8]), int(chasti[9]), int(chasti[10]), int(chasti[11])]

max_oranges = max(oranges)
max_apples = max(apples)

print("Максимальные продажи:")
print("Апельсины:", max_oranges, "кг")
print("Яблоки:", max_apples, "кг")

