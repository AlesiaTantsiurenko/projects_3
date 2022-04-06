"""
4. Дано ціле n>2. Вивести всі прості числа з діапазону [2, n].
"""


def isprime(num: int) -> list:
    """ Функция нахождения простых чисел из заданного диапазона """
    numbers = [2]
    for num_1 in range(3, num + 1, 2):
        divider = 0
        square = int(num ** 0.5) + 2
        for num_2 in numbers:
            if num_2 > square:
                break
            if num_1 % num_2 == 0:
                divider = 1
                break
        if divider == 0:
            numbers.append(num_1)
    return numbers


def main():
    print(" Добро пожаловать в программу нахождения списка простых чисел!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Сформировать список простых чисел
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    n = int(input("Введите количество простых чисел (целое число больше 2) "))
                    if n > 2:
                        break
                    else:
                        print("Число должно быть больше двух!")
                except ValueError:
                    print("Несоответствие типов!")
            print("Список простых чисел в диапазоне [ 2 ;", n, "] выглядит так: ", isprime(n))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
