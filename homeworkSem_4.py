from random import randint
import itertools


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

def primes(num):
    num1, i, primes  = num, 2, []
    while i <= num:
        if num % i == 0:
            primes.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {num1} находятся в списке: {primes}")


def inInt(text):
    while True:
        try:
            num = int(input(text))
            return num
        except ValueError:
            print("Введите число!")


print("Задача 1: ")

num = inInt("Задайте натуральное число: ")
primes(num)


# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def somthingLikeSet():
    nums, setNums = list(map(int, input("Введите числа через пробел:\n").split())), []
    print(f"Исходный список: {nums}")
    for i in range(len(nums)):
        if nums[i] not in setNums:
            setNums.append(nums[i])
    print(f"Список из неповторяющихся элементов: {setNums}")
    print(f"Результат работы встроенной функции set(): {list(set(nums))}")

print()
print("Задача 2: ")

somthingLikeSet()
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²


print()
print("Задача 3: ")

k = randint(2, 7)

def getRatios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios


def getPolynomial(k, ratios):
    pattern = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, pattern, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:

        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    polynomial = "".join(map(str, polynomial))
    polynomial = polynomial.replace("1*x", "x")
    return polynomial


ratios = getRatios(k)
polynom1 = getPolynomial(k, ratios)
print(polynom1)

with open('Polynomial.txt', 'w') as data:
    data.write(polynom1)


# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = getRatios(k)
polynom2 = getPolynomial(k, ratios)
print(polynom2)

with open('Polynomial2.txt', 'w') as data:
    data.write(polynom2)