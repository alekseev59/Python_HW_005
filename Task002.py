# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

from random import randint


def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# Игра с ботом
# import random
# from random import randint, choice

# print(
#    '"Игра с конфетами"\n'
# )

# messages = ['Ваш ход брать конфеты']
# max_number_move = 0


# def introduce_players():
#    player1 = input('Первый игрок, напишите ваше имя\n')
#    player2 = 'SmartBOT'
#    print(f'Очень приятно, сегодня Вы играете с ботом - {player2}')
#    return [player1, player2]


# def sweets_game(players):
#    global max_number_move
#    total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
#    max_number_move = int(
#        input('Введите количество конфет, которое можно забрать за один ход:\n'))
#    first = int(input(
#        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#    if first != 1:
#        first = 0
#    return [total_sweets, max_number_move, int(first)]


# max_move = max_number_move


# def game_player_vs_smart_bot(sweets, players, messages):
#    global max_number_move
#    count = sweets[2]

#    while sweets[0] > 0:
#       if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
#           move = sweets[0] - 1
#          print(f'Я забираю {move}')

#      elif not count % 2:
#          move = random.randint(1, sweets[1])
#           print(f'Я забираю {move}')
#       else:
#           print(f'{players[0]}, {choice(messages)}')
#           move = int(input())
#         if move > sweets[0] or move > sweets[1]:
#                print(
#                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
#                chance = 2
#                while chance > 0:
#                    if sweets[0] >= move <= sweets[1]:
#                       break
#                   print(f'Попробуйте ещё раз, у Вас {chance} попытки')
#                   move = int(input())
#                   chance -= 1
#               else:
#                   return print(f'Попыток не осталось. Game over!')
#       sweets[0] = sweets[0] - move
#       if sweets[0] > 0:
#           print(f'Осталось {sweets[0]} конфет')
#       else:
#           print('Все конфеты разобраны.')
#       count += 1
#    return players[not count % 2]


# players = introduce_players()
# sweets = sweets_game(players)

# winer = game_player_vs_smart_bot(sweets, players, messages)
# if not winer:
#    print('У нас нет победителя.')
# else:
#    print(
#        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
