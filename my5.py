"""
10. Дано ціле число N (>0). Знайти значення виразу 1.1 - 1.2 + 1.3 - ... (N доданків, знаки чергуються).
Умовний оператор не використовувати.
"""


def calculation(number):
    """ Функция нахождения суммы слогаемых """
    res = 0
    i = 1
    while i <= number:
        res += pow(-1, i + 1) * (1.0 + (float(i / 10)))
        i += 1
    return round(res, 3)


def main():
    print(" Добро пожаловать в программу нахождения суммы слогаемых (1.1 - 1.2 + 1.3 - ...)!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти сумму слогаемых
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    n = int(input("Введите целое положительное число слогаемых "))
                    if n > 0:
                        break
                    else:
                        print("Число должно быть больше нуля!")
                except ValueError:
                    print("Несоответствие типов!")
            print("Результат исчисления ", calculation(n))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
