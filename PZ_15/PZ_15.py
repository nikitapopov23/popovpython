# Приложение УЧЕТ ВНУТРИОФИСНЫХ РАСХОДОВ для некоторой
# организации. БД должна содержать таблицу Канцелярия со следующей структурой
# записи: ФИО работника, отдел, вид расхода, сумма
import sqlite3


conn = sqlite3.connect('office_expenses.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Канцелярия (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT NOT NULL,
    department TEXT NOT NULL,
    expense_type TEXT NOT NULL,
    amount REAL NOT NULL
)
''')
conn.commit()

def add_expense(fio, department, expense_type, amount):
    """Добавляет запись о расходах в таблицу."""
    try:
        cursor.execute('''
        INSERT INTO Канцелярия (fio, department, expense_type, amount)
        VALUES (?, ?, ?, ?)
        ''', (fio, department, expense_type, amount))
        conn.commit()
        print("Запись успешно добавлена!")
    except Exception as e:
        print(f"Ошибка при добавлении записи: {e}")

def search_expense_by_fio(fio):
    """Ищет записи по ФИО работника."""
    try:
        cursor.execute('SELECT * FROM Канцелярия WHERE fio = ?', (fio,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка при поиске записи: {e}")
        return []

def search_expense_by_department(department):
    """Ищет записи по отделу."""
    try:
        cursor.execute('SELECT * FROM Канцелярия WHERE department = ?', (department,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка при поиске записи: {e}")
        return []

def delete_expense_by_id(expense_id):
    """Удаляет запись по ID."""
    try:
        cursor.execute('DELETE FROM Канцелярия WHERE id = ?', (expense_id,))
        conn.commit()
        print("Запись успешно удалена!")
    except Exception as e:
        print(f"Ошибка при удалении записи: {e}")

def update_expense(expense_id, fio, department, expense_type, amount):
    """Редактирует запись о расходах по ID."""
    try:
        cursor.execute('''
        UPDATE Канцелярия
        SET fio = ?, department = ?, expense_type = ?, amount = ?
        WHERE id = ?
        ''', (fio, department, expense_type, amount, expense_id))
        conn.commit()
        print("Запись успешно обновлена!")
    except Exception as e:
        print(f"Ошибка при обновлении записи: {e}")

def view_all_expenses():
    """Выводит все записи о расходах."""
    try:
        cursor.execute('SELECT * FROM Канцелярия')
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
    except Exception as e:
        print(f"Ошибка при просмотре записей: {e}")

def main():
    """Основная функция для взаимодействия с пользователем."""
    while True:
        print("\n1. Добавить запись о расходах")
        print("2. Просмотреть все записи")
        print("3. Найти записи по ФИО")
        print("4. Найти записи по отделу")
        print("5. Удалить запись по ID")
        print("6. Редактировать запись по ID")
        print("7. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            fio = input("Введите ФИО работника: ")
            department = input("Введите отдел: ")
            expense_type = input("Введите вид расхода: ")
            amount = float(input("Введите сумму: "))
            add_expense(fio, department, expense_type, amount)
        
        elif choice == '2':
            print("\nВсе записи о расходах:")
            view_all_expenses()
        
        elif choice == '3':
            fio = input("Введите ФИО работника: ")
            results = search_expense_by_fio(fio)
            if results:
                for record in results:
                    print(record)
            else:
                print("Записи не найдены.")
        
        elif choice == '4':
            department = input("Введите отдел: ")

            results = search_expense_by_department(department)
            if results:
                for record in results:
                    print(record)
            else:
                print("Записи не найдены.")
        
        elif choice == '5':
            expense_id = int(input("Введите ID записи для удаления: "))
            delete_expense_by_id(expense_id)
        
        elif choice == '6':
            expense_id = int(input("Введите ID записи для редактирования: "))
            fio = input("Введите новое ФИО работника: ")
            department = input("Введите новый отдел: ")
            expense_type = input("Введите новый вид расхода: ")
            amount = float(input("Введите новую сумму: "))
            update_expense(expense_id, fio, department, expense_type, amount)
        
        elif choice == '7':
            print("Выход из программы.")
            break
        
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()


conn.close()

