# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

import tkinter as tk
from tkinter import ttk

def submit_form():
    
    print("Форма отправлена!")


root = tk.Tk()
root.title("Форма регистрации пользователя")
root.geometry("400x400")


tk.Label(root, text="Ваше имя:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Возраст:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=10)


tk.Label(root, text="Ваш пол:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
gender_var = tk.StringVar(value="Мужской")
ttk.Radiobutton(root, text="Мужской", variable=gender_var, value="Мужской").grid(row=3, column=1, sticky="w")
ttk.Radiobutton(root, text="Женский", variable=gender_var, value="Женский").grid(row=4, column=1, sticky="w")


tk.Label(root, text="Ваши увлечения:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
hobbies_frame = ttk.Frame(root)
hobbies_frame.grid(row=5, column=1, sticky="w")

hobby_music = tk.BooleanVar()
hobby_art = tk.BooleanVar()
hobby_drawing = tk.BooleanVar()

ttk.Checkbutton(hobbies_frame, text="Музыка", variable=hobby_music).pack(anchor="w")
ttk.Checkbutton(hobbies_frame, text="Искусство", variable=hobby_art).pack(anchor="w")
ttk.Checkbutton(hobbies_frame, text="Рисование", variable=hobby_drawing).pack(anchor="w")


tk.Label(root, text="Ваша страна:").grid(row=6, column=0, padx=10, pady=10, sticky="w")
country_entry = tk.Entry(root)
country_entry.grid(row=6, column=1, padx=10, pady=10)

tk.Label(root, text="Ваш город:").grid(row=7, column=0, padx=10, pady=10, sticky="w")
city_entry = tk.Entry(root)
city_entry.grid(row=7, column=1, padx=10, pady=10)


tk.Label(root, text="Кратко о себе:").grid(row=8, column=0, padx=10, pady=10, sticky="w")
description_text = tk.Text(root, height=5, width=30)
description_text.grid(row=8, column=1, padx=10, pady=10)


submit_button = tk.Button(root, text="Данные подтвердить", command=submit_form)
submit_button.grid(row=9, column=1, padx=10, pady=10, sticky="e")

cancel_button = tk.Button(root, text="Отменить ввод", command=root.quit)
cancel_button.grid(row=9, column=0, padx=10, pady=10, sticky="w")


root.mainloop()