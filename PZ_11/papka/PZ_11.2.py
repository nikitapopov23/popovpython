# Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми
# кодами.
def count_uppercase_letters(text):
    return sum(1 for char in text if char.isupper())


def replace_with_ascii_codes(line):
    return ' '.join(str(ord(char)) for char in line)


input_filename = 'C:\\Users\\vasil\Desktop\\popovpython\\PZ_11\\papka\\text18-22.txt'
output_filename = 'poem_output.txt'

with open(input_filename, 'r', encoding='utf-16') as f:
    lines = f.readlines()


print("Содержимое файла:")
for line in lines:
    print(line.strip())


uppercase_count = sum(count_uppercase_letters(line) for line in lines)
print(f"\nКоличество букв в верхнем регистре: {uppercase_count}")


with open(output_filename, 'w', encoding='utf-16') as f:
    for i, line in enumerate(lines):
        if i == 2:  
        
            modified_line = replace_with_ascii_codes(line.strip())
            f.write(modified_line + '\n')
        else:
            f.write(line)

print(f"\nНовый файл '{output_filename}' создан с заменой символов в третьей строке.")
