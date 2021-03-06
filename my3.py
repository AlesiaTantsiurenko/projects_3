"""
14. Дано ціле число N (>0). Знайти добуток N! = 1*2*...*N (N-факторіал). Щоб уникнути цілочисельного
переповнення, обчислювати цей добуток за допомогою дійсної змінної і вивести його як дійсне число.
"""


def fact(num: int) -> float:
    """ Рекурсивная функция исчисления факториала """
    if num == 1 or num == 0:
        return 1
    else:
        return float(num * fact(num-1))


def main():
    print(" Добро пожаловать в программу нахождения факториала от числа!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти факториал
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    n = int(input("Введите целое позитивное число "))
                    if n > 0:
                        break
                    else:
                        print("Число должно быть больше нуля!")
                except ValueError:
                    print("Несоответствие типов!")
            print("Факториал числа ", n, " равен ", fact(n))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
