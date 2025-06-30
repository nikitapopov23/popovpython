# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.

import tkinter as tk
from tkinter import messagebox

def find_hundreds_digit():
    try:
        
        number = int(entry.get())
        
        
        if number <= 999:
            messagebox.showerror("Ошибка", "Введите число больше 999.")
            return
        
        
        hundreds_digit = (number // 100) % 10
        
        
        result_label.config(text=f"Цифра сотен: {hundreds_digit}")
    
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное целое число.")


root = tk.Tk()
root.title("Поиск цифры сотен")


label = tk.Label(root, text="Введите число больше 999:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Найти цифру сотен", command=find_hundreds_digit)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()
