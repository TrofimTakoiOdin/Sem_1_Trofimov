import re
import itertools


# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл, содержащий сумму многочленов

file1, file2, fileSum = 'Polynomial.txt', 'Polynomial2.txt', 'polynomSum.txt'

# Получение данных из файла

def readFile(file):
    with open(str(file), 'r') as data:
        polinom = data.read()
    return polinom


def convertPolinom(polynom):
    polynom = polynom.replace('= 0', '')
    polynom = re.sub("[*|^| ]", " ", polynom).split('+')
    polynom = [char.split(' ') for char in polynom]
    polynom = [[x for x in lst if x] for lst in polynom]
    for i in polynom:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    polynom = [tuple(int(x) for x in j if x != 'x') for j in polynom]
    return polynom


def foldPols(polinom_1, polinom_2):
    x = [0] * (max(polinom_1[0][1], polinom_2[0][1] + 1))
    for i in polinom_1 + polinom_2:
        x[i[1]] += i[0]
    result = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    result.sort(key=lambda y: y[1], reverse=True)
    return result


def getSumPol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    newPolinom = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in newPolinom:
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
            del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    newPolinom = list(itertools.chain(*newPolinom))
    newPolinom[-1] = ' = 0'
    return "".join(map(str, newPolinom))


def writeToFile(file, pol):
    with open(file, 'w') as data:
        data.write(pol)


pol1, pol2 = readFile(file1), readFile(file2)
pol_1, pol_2 = convertPolinom(pol1), convertPolinom(pol2)

resultSum = getSumPol(foldPols(pol_1, pol_2))
writeToFile(fileSum, resultSum)

print(pol1, pol2, resultSum, sep="\n")
