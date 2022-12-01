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


k = [round(random.uniform(1, 10), 2) for i in range(10)]
print(k)
c = min(k, key=lambda x: float(x) - int(x))
d = max(k, key=lambda x: float(x) - int(x))
print(c)
print(d)
res = round(float(d) - int(d), 2) - round(float(c) - int(c), 2)
print(res)






