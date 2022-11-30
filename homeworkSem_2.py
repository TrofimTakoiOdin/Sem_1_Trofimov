import sys
from math import factorial
import numpy as np
import random
import time

def main():
    while True:
        print("Добро пожаловать в меню!")
        print("Выберите задачу 1 -5")
        userIn = inInt("Введите номер задачи: ")
        if userIn == 1:
            print("Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр")
            problemOne()
            time.sleep(2.5)
            userExit()

        elif userIn == 2:
            print("Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N")
            problemTwo()
            time.sleep(2.5)
            userExit()

        elif userIn == 3:
            print("	Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.")
            problemThree()
            time.sleep(2.5)
            userExit()

        elif userIn == 4:
            print("Задайте числами список из N элементов, заполненных из промежутка [-N, N].")
            print("Найдите произведение элементов на указанных позициях. Позиции хранятся в ")
            print("файле file.txt в одной строке одно число.")
            problemFour()
            time.sleep(2.5)
            userExit()

        elif userIn == 5:
            print("Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие")
            print("методы из библиотеки random - можно).")
            problemFive()
            time.sleep(2.5)
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

def inFloat(text):
    while True:
        try:
            num = float(input(text))
            return num
        except ValueError:
            print("Введите число!")


def sumNums(num):
    k = [i for i in str(num) if i != "."]
    return sum(map(int, k))


def problemFive():
    k, m = [i for i in range(random.randint(5, 10))], []
    print("Изначальный список:", *k)
    while k:
        m.append(k.pop(random.randint(0, len(k) - 1)))
    print("Перемешанный список:", *m)


def problemFour():
    n = inInt("Введите число: ")
    k = [i for i in range(-n, n + 1, 1)]
    d = np.loadtxt("File.txt", delimiter="\t", dtype=str)
    d = str(d)
    x, y = int(d[0]), int(d[1])
    produce = k[x] * k[y]
    print("Числа массива:", *k)
    print(f"Произведение чисел на позициях {x} и {y} = {produce}")


def problemThree():
    n = inInt("Введите число: ")
    k = [((1 + 1 / n) ** n) for i in range(1, n + 1)]
    print(sum(k))


def problemTwo():
    n = inInt("Введите число: ")
    k = [factorial(i) for i in range(1, n + 1)]
    print(f"Набор произведений чисел от 1 до {n}:", *k)


def problemOne():
    num = inFloat("Введите вещественное число:")
    k = sumNums(num)
    print(f"Сумма чисел вещественного числа: {k}")


if __name__ == "__main__":
    main()



