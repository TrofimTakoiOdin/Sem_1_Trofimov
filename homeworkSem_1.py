import sys


def main():
    print("Добро пожаловать в меню!")
    print("Выберите задачу 1 - 4")
    while True:
        userIn = inputNum("Введите номер задачи: ")
        if userIn == 1:
            print("Задача 1")
            print("Напишите программу, которая принимает на вход цифру, обозначающую день недели"
              ", и проверяет, является ли этот день выходным. "
              "Пример: - 6 -> да - 7 -> да - 1 -> нет")
            print()
            isHoliday()
            userExit()

        elif userIn == 2:
            print("Задача 2")
            print("Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,"
                "является ли этот день выходным.Пример: - 6 -> да - 7 -> да - 1 -> нет")
            print()
            coord = coordinates2D()
            checkCoordinates(coord)
            userExit()
        elif userIn == 3:
            print("Задача 3")
            print(""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат""")
            print()
            result = checkPredicate()
            print(result)
            userExit()
        elif userIn == 4:
            print("Задача 4")
            print(""" Напишите программу, которая принимает на вход координаты двух точек
             и находит расстояние между ними в 2D пространстве. 
            Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """)
            print()
            coordinates = pointsAandB()
            dist = calculateDistance2D(coordinates[0], coordinates[1])
            print(f"Расстояние между точками А и В равно: {round(dist, 2)}")
            userExit()


def userExit():
    print("Вернуться в меню? Y/N ")
    userIn = input(">> ")
    if userIn in list("YyНн"):
        return True
    else:
        sys.exit()


def inputNum(text):
    while True:
        try:
            num = int(input(text))
            return num
        except:
            print("Введите число!")


def inputNumbers(inputText):
    x = int(input("Сколько чисел будем вводить? Укажите число: "))
    while True:
        try:
            num = list(map(int, input(inputText).split()))
            if len(num) == x:
                return num
            else:
                print(f"Необходимо ввести {x} чисел(а)!")
        except ValueError:
            print("Необходимо ввести числа!")


# Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример: - 6 -> да - 7 -> да - 1 -> нет

def isHoliday():
    day = int(input("Введите цифру-номер дня недели: "))
    if 0 < day < 6:
        print("Нет, идем на работу!")
    elif day == 6 or day == 7:
        print("Да, выходной!")
    else:
        print("Вы ввели что-то не то!")


# Задача 2
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3

def coordinates2D():
    a = [0, 0]
    for i in range(2):
        flag = False
        while not flag:
            try:
                number = int(input(f"Введите {i + 1} координату: "))
                a[i], flag = number, True
                if a[i] == 0:
                    flag = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Пожалуйста, введите число!")
    return a


def checkCoordinates(x_y):
    if x_y[0] > 0 and x_y[1] > 0:
        quarter = 1
    elif x_y[0] < 0 and x_y[1] > 0:
        quarter = 2
    elif x_y[0] < 0 and x_y[1] < 0:
        quarter = 3
    else:
        quarter = 4
    print(f"Точка находится в {quarter} четверти плоскости")


# Задача 3
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Решил проверить именно численные значения. Для строк результат будет тем же."""

def checkPredicate():
    predicate = inputNumbers("Введите численные значения предиката: ")
    leftStatement = not (predicate[0] or predicate[1] or predicate[2])
    rightStatement = not predicate[0] and not predicate[1] and not predicate[2]
    result = leftStatement == rightStatement
    return (result)


# Задача 4
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21

def pointsAandB():
    print("Введите координаты точек А и В: ")
    coord = []
    for i in range(2):
        coord.append(coordinates2D())
    return coord


def calculateDistance2D(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return distance


if __name__ == "__main__":
    main()


