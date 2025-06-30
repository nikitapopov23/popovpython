# .Даны текущие оценки студента по дисциплине «Основы программирования» за
# месяц. Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и
# определить итоговую оценку за месяц.

grades_input = input("Введите оценки студента через пробел: ")
grades = list(map(int, grades_input.split()))  


count_2 = grades.count(2)
count_3 = grades.count(3)
count_4 = grades.count(4)
count_5 = grades.count(5)


total_grades = sum(grades)
num_grades = len(grades)

if num_grades > 0:
    average_grade = total_grades / num_grades
else:
    average_grade = 0


if average_grade < 3:
    final_grade = 2
elif average_grade < 4:
    final_grade = 3
elif average_grade < 5:
    final_grade = 4
else:
    final_grade = 5


print(f"Количество '2': {count_2}")
print(f"Количество '3': {count_3}")
print(f"Количество '4': {count_4}")
print(f"Количество '5': {count_5}")
print(f"Итоговая оценка за месяц: {final_grade:.1f} (средний балл: {average_grade:.2f})")