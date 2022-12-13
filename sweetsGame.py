from random import randint
import time
import sys


try:
    import bext
except ImportError:
    print("Модуль bext нужно заранее установить")
    print("Как это сделать, читай на")
    print("https://pypi.org/project/Bext/")
    sys.exit()


def userExit():
    print("Вернуться в меню? Y/N ")
    userIn = input(">> ")
    if userIn in list("YyНн"):
        return True
    else:
        sys.exit()


def showGameInfo():
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    bext.fg("green")
    print("Логическая игра с конфетами (человек против человека или бота)")
    bext.fg("red")
    print("Обычная сложность - имя второго игрока 'bot', хард - 'smartBot'")
    bext.fg("green")
    print("Условие задачи: На столе лежит N конфет. Играют два игрока делая ход друг после друга.")
    print("Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.")
    print("Все конфеты оппонента достаются сделавшему последний ход.")
    bext.fg("red")
    print("Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?")
    bext.fg("black")
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()


def inputData(name):
    while True:
        try:
            bid = int(input(f"{name}, сколько конфет возьмете? (от 1 до 28): "))
            if 0 < bid < 29:
                return bid
            else:
                print("По правилам можно взять только от 1 до 28 конфет!")
        except ValueError:
            print("Нужно ввести число!")


def turnInfo(name, k, counter, value):
    print()
    bext.fg("random")
    print(f"Ход совершил {name}. Им взято {k}, сейчас у него {counter} конфет. На столе осталось {value} конфет.")
    bext.fg("black")
    print()


def playerNamesAndSweets():
    player1, player2 = input("Введите имя первого игрока: "), input("Введите имя второго игрока (bot или smartBot, если хотите сыграть с компьютером): ")
    value, turn = int(input("Введите количество конфет на столе: ")), randint(1, 2)
    info = (player1, player2, value, turn)
    return info


def botBrain(value):
    take = value % 29 if value % 29 != 0 else randint(1, 28)

    return take


def whoWins(turn, player1, player2):
    if turn == 1:
        bext.fg("green")
        print(f"Выиграл {player1}! Поздравляем!")
        bext.fg("black")
        userExit()
    else:
        bext.fg("red")
        print(f"Выиграл {player2}!")
        bext.fg("black")
        userExit()


def stupidBotTurn(value, player1, player2, turn):
    counter1, counter2 = 0, 0
    while value > 28:
        if turn == 1:
            k = inputData(player1)
            counter1 += k
            value -= k
            turn += 1
            turnInfo(player1, k, counter1, value)
        else:
            k = randint(1,28)
            counter2 += k
            value -= k
            turn -= 1
            turnInfo(player2, k, counter2, value)

    whoWins(turn, player1, player2)


def smartBotGame(value, player1, player2, turn):
    counter1, counter2 = 0, 0
    while value > 28:
        if turn == 1:
            time.sleep(1)
            k = inputData(player1)
            counter1 += k
            value -= k
            turn += 1
            turnInfo(player1, k, counter1, value)
        else:
            time.sleep(1)
            k = botBrain(value)
            counter2 += k
            value -= k
            turn -= 1
            turnInfo(player2, k, counter2, value)

    whoWins(turn, player1, player2)


def twoPlayers(value, player1, player2, turn):

    counter1, counter2 = 0, 0
    while value > 28:
        if turn == 1:
            k = inputData(player1)
            counter1 += k
            value -= k
            turn += 1
            turnInfo(player1, k, counter1, value)
        else:
            k = inputData(player2)
            counter2 += k
            value -= k
            turn -= 1
            turnInfo(player2, k, counter2, value)

    whoWins(turn, player1, player2)


def main():
    showGameInfo()
    while True:
        keyInfo = playerNamesAndSweets()
        player1, player2, value, turn = keyInfo[0], keyInfo[1], keyInfo[2], keyInfo[3]
        time.sleep(1)
        if turn == 1:
            print(f"Первым ходит {player1}")
        else:
            print(f"Первым ходит {player2}")
        time.sleep(1)

        if player2 == "bot":
            stupidBotTurn(value, player1, player2, turn)

        elif player2 == "smartBot":
            smartBotGame(value, player1, player2, turn)

        else:
            twoPlayers(value, player1, player2, turn)


if __name__ == "__main__":
    main()
