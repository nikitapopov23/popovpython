# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


averages = []


for i in range(len(matrix)):
  
    if (i + 1) % 2 != 0:
        
        row_average = sum(matrix[i]) / len(matrix[i])
        averages.append(row_average)


for index, avg in enumerate(averages):
    print(f"Среднее арифметическое для строки {2 * index + 1}: {avg}")
