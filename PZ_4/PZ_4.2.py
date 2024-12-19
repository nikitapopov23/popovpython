#Дано число A (>1). Вывести наибольшее из целых чисел K, для которых сумма 1 +
#1/2 + ... + 1/K будет меньше A, и саму эту сумму.

try:
    A = float(input("Введите число A (> 1): "))

    if A <= 1:
        print("A должно быть больше 1")
    else:
        K = 1
        sum_value = 0

        while sum_value + 1 / K < A:
            sum_value += 1 / K
            K += 1

        K -= 1

        print(f"Наибольшее K: {K}")
        print(f"Сумма для K={K}: {sum_value}")

except ValueError:
    print("Неправильно ввели")
