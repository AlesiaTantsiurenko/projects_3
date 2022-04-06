"""
9. Дано натуральне число. Знайдіть число десятків у його десяткового запису.
"""


def tens(num: int) -> int:
    """ Функция для нахождения десятков в числе """
    ten = (num // 10) % 10
    return ten


def main():
    print(" Добро пожаловать в программу нахождения десятков в числе!")
    choice = None
    while choice != "0":
        print(
            """
           0 - Выйти
           1 - Найти разряд десятков в числе
          """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    n = int(input("Введите натуральное число "))
                    if n > 0:
                        break
                    else:
                        print("Число должно быть больше нуля!")
                except ValueError:
                    print("Несоответствие типов!")
            print("Количество деястков в числе ", n, "равно ", tens(n))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
