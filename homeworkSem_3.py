import random
from random import randint
import time
import sys


def main():
    pass


def unevenElemSum():
    k, total = [random.randint(1,  10) for i in range(10)], 0
    for i in range(1, len(k), 2):
        total += k[i]
    return total


def pairOfListSum(lst):
    temp, temp2, prod, res = 0,0, 0, []
    while lst:
        if len(lst) != 1:
            temp, temp2 = lst.pop(0), lst.pop(-1)
            prod = temp * temp2
            res.append(prod)
        else:
            prod = lst.pop(0) ** 2
            res.append(prod)
    return res



# k = [2, 3, 5, 6]
# print("Исходный список:", k)
# l = pairOfListSum(k)
# print("Результирующий список: ", l)


def minMaxFractionsDiff(lst):
    # Ищем числа в списке по принципу наименьшей и наибольшей дробной части, исп. lambda

    minFract, maxFract = min(lst, key=lambda x: float(x) - int(x)), max(lst, key=lambda x: float(x) - int(x))

    # Дробные значения для наглядности выведем в отдельную переменную

    a, b = round(float(maxFract) - int(maxFract), 2), round(float(minFract) - int(minFract), 2)
    res = a - b
    print("Исходный список: ", lst)
    print(f"Искомое значение: {a} - {b } = {res}")

# k = [round(random.uniform(1, 10), 2) for i in range(10)]
# print(k)
# c = min(k, key=lambda x: float(x) - int(x))
# d = max(k, key=lambda x: float(x) - int(x))
# print(c)
# print(d)
# res = round(float(d) - int(d), 2) - round(float(c) - int(c), 2)
# print(res)

# k = [round(random.uniform(1, 10), 2) for i in range(10)]
# minMaxFractionsDiff(k)


def convertDecimalToBinary(num):
    res = []
    while num != 1:
        res.append(str(num % 2))
        num = num // 2
    res.append("1")
    res = "".join(res[::-1])
    return res

# l = convertDecimalToBinary(11)
# print(l)


def fibonacci(num):
    fib1, fib2 = 0, 1
    lst = [0]
    for i in range(1, n + 1):
        if i < 2:
            lst.append(1)
            lst.insert(0, 1)
        else:
            fib1, fib2 = fib2, fib1 + fib2
            lst.append(fib2)
            lst.insert(0, fib2 * (-1)**(i+1))
    return lst




# n = 8
# print(fibonacci(8))



