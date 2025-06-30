# В двумерном списке найти минимальный элемент в предпоследнем столбце.

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


if len(matrix) > 0 and len(matrix[0]) > 1:
    # Извлечение предпоследнего столбца
    penultimate_column = [row[-2] for row in matrix]
    
    
    min_value = min(penultimate_column)
    
    print("Минимальный элемент в предпоследнем столбце:", min_value)
else:
    print("Матрица должна содержать как минимум два столбца.")