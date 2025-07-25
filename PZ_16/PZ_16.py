# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во".

class Товар:
    def __init__(self, название, цена, количество):
        self.название = название
        self.цена = цена
        self.количество = количество

    def информация_о_товаре(self):
        """Метод для вывода информации о товаре."""
        return f"Название: {self.название}, Цена: {self.цена}, Количество: {self.количество}"


if __name__ == "__main__":
    товар1 = Товар("Яблоко", 50, 10)
    товар2 = Товар("Банан", 30, 20)

    print(товар1.информация_о_товаре())
    print(товар2.информация_о_товаре())
