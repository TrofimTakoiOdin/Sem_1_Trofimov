from math import gcd
from functools import reduce


def gcd_iterable():
    num, lst = 0, []
    while True:
        try:
            num = int(input("Введите число или нажмите Enter для завершения ввода: "))
            lst.append(num)
        except ValueError:

            break

    print(f"Наибольший общий делитель: {reduce(gcd, lst)}")


def eagle_and_tailes():

    lst = input("Введите последовательность типа 'ООРООР': ")
    # Загадочный символ "О" в строке может иметь несколько вариантов:
    if chr(79) in lst:
        lst = lst.split(chr(79))
    elif chr(48) in lst:
        lst = lst.split(chr(48))
    else:
        lst = lst.split(chr(1054))

    if [len(i) for i in lst]:
        print(f"Наибольшее количество выпавших подряд Решек: {(max([len(i) for i in lst]))}")
    else:
        print("0")

# Первая задача:
gcd_iterable()

# Вторая задача:
eagle_and_tailes()
