# # Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string


input_string = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'


punctuation_chars = [char for char in input_string if char in string.punctuation]


result = ''.join(punctuation_chars)


print("Символы пунктуации:", result)