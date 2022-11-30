def matchingNums():
    a, b, c = int(input("Введите число a: ")), int(input("Введите число b: ")), int(input("Введите число c: "))
    if  a == b == c:
        print("3")
    elif a == b or b == c or a == c:
        print("2")
    else:
        print("0")


def unevenFromAtoB():
    a, b, k = int(input("Введите число a: ")), int(input("Введите число b: ")), []
    for i in range(a - int((a % 2) == 0), b - 1, -2):
        print(i)


def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False



