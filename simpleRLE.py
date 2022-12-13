# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах. Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:          12W1B12W3B24W1B14W


def encode(some_string):
    counter, result = 1, ""
    for i in range(len(some_string) - 1):
        if some_string[i] == some_string[i + 1]:
            counter += 1
        else:
            result = result + str(counter) + some_string[i]
            counter = 1
    if counter > 1 or (some_string[len(some_string) - 2] != some_string[-1]):
        result = result + str(counter) + some_string[-1]
    return result


def decode(some_string):
    number, res = "", ""

    for i in range(len(some_string)):
        if not some_string[i].isalpha():
            number += some_string[i]
        else:
            res = res + some_string[i] * int(number)
            number = ''
    return res


def main():
    string = input("Введите текст: ")
    print(f"Результат кодировки: {encode(string)}")
    print(f"Результат дешифровки: {decode(encode(string))}")


if __name__ == "__main__":
    main()