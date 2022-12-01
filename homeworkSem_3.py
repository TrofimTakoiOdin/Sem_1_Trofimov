import os
import random
import time
import sys


def main():
    while True:
        print("Добро пожаловать в меню!")
        time.sleep(2)
        print("Выберите задачу 1 -5")
        time.sleep(1)
        userIn = inInt("Введите номер задачи: ")

        if userIn == 1:
            os.system("cls")
            time.sleep(0.5)
            print("Задача 1:")
            print()
            print("Задайте список из нескольких чисел.")
            print("Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции")

            result = listPairSum()
            time.sleep(0.5)
            print(f"Сумма элементов на нечетных позициях: {result}")
            time.sleep(2)
            userExit()

        elif userIn == 2:
            os.system("cls")
            time.sleep(0.5)
            print("Задача 2: ")
            print()
            print("Напишите программу, которая найдёт произведение пар чисел списка. ")
            print("Парой считаем первый и последний элемент, второй и предпоследний и т.д.")

            k = [random.randint(1, 100) for i in range(10)]
            print("Исходный список: ", k)
            result = pairOfListSum(k)
            print("Список произведений пар чисел списка: ", result)
            time.sleep(2)
            userExit()

        elif userIn == 3:
            os.system("cls")
            time.sleep(0.5)
            print("Задача 3:")
            print()
            print("Задайте список из вещественных чисел. Напишите программу, которая найдёт")
            print("разницу между максимальным и минимальным значением дробной части элементов")
            print()
            time.sleep(2)
            k = [round(random.uniform(1, 10), 2) for i in range(10)]
            minMaxFractionsDiff(k)
            time.sleep(2)
            userExit()

        elif userIn == 4:
            os.system("cls")
            time.sleep(0.5)
            print("Задача 4: ")
            print()
            print("Напишите программу, которая будет преобразовывать десятичное число в двоичное")
            print("(встроенными методами пользоваться нельзя)")

            someNum = random.randint(1, 100)
            print(f"Некоторое десятичное число {someNum} в двоичной системе: {convertDecimalToBinary(someNum)}")
            time.sleep(2)
            userExit()

        elif userIn == 5:
            os.system("cls")
            time.sleep(0.5)
            print("Задача 5: ")
            print()
            print("Задайте число. ")
            print("Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

            someNum = random.randint(3, 10)
            fibRes = fibonacci(someNum)
            print(f"Для некоторого числа {someNum} последовательность Фибоначчи: {fibRes}")
            time.sleep(2)
            userExit()


def userExit():
    print("Вернуться в меню? Y/N ")
    userIn = input(">> ")
    if userIn in list("YyНн"):
        return True
    else:
        sys.exit()


def inInt(text):
    while True:
        try:
            num = int(input(text))
            return num
        except ValueError:
            print("Введите число!")

def listPairSum():
    k, total = [random.randint(1,  10) for i in range(10)], 0
    print("Исходный список: ", k)
    for i in range(1, len(k), 2):
        total += k[i]
    return total


def pairOfListSum(lst):
    temp, temp2, prod, res = 0, 0, 0, []
    while lst:
        if len(lst) != 1:
            temp, temp2 = lst.pop(0), lst.pop(-1)
            prod = temp * temp2
            res.append(prod)
        else:
            prod = lst.pop(0) ** 2
            res.append(prod)
    return res


def minMaxFractionsDiff(lst):
    # Ищем числа в списке по принципу наименьшей и наибольшей дробной части, исп. lambda

    minFract, maxFract = min(lst, key=lambda x: float(x) - int(x)), max(lst, key=lambda x: float(x) - int(x))

    # Дробные значения для наглядности выведем в отдельную переменную

    a, b = round(float(maxFract) - int(maxFract), 2), round(float(minFract) - int(minFract), 2)
    res = round(a - b, 2)
    print("Исходный список: ", lst)
    print(f"Искомое значение: {a} - {b } = {res}")


def convertDecimalToBinary(num):
    res = []
    while num != 1:
        res.append(str(num % 2))
        num = num // 2
    res.append("1")
    res = "".join(res[::-1])
    return res


def fibonacci(num):
    fib1, fib2 = 0, 1
    lst = [0]
    for i in range(1, num + 1):
        if i < 2:
            lst.append(1)
            lst.insert(0, 1)
        else:
            fib1, fib2 = fib2, fib1 + fib2
            lst.append(fib2)
            lst.insert(0, fib2 * (-1)**(i+1))
    return lst


if __name__ == "__main__":
    main()



