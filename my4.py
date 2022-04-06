"""
19. Дано ціле число N (>0). Послідовність чисел Фібоначчі Fk визначається наступним чином: F1=1, F2=1,
Fk=Fk-2+Fk-1, K=3,4....Перевірити, чи є число N числом Фібоначчі. Якщо є, то вивести true, якщо ні -
вивести false.
"""


def fib(num: int)-> bool:
    """ Функция опредиления, является ли число числои Фибоначчи """
    f1, f2 = 1, 1
    for i in range(num):
        f1, f2 = f2, f1 + f2
        if num == f2:
            return True
    return False


def main():
    print(" Добро пожаловать в программу опредиления числа Фибоначчи!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Опредилить, является ли число числом Фибоначчи
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    n = int(input("Введите целое число "))
                    if n > 0:
                        break
                    else:
                        print("Число должно быть больше нуля!")
                except ValueError:
                    print("Несоответствие типов!")
            print("Является ли число ", n, " числом Фибоначчи - ", fib(n))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
