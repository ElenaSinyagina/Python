# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один 
# ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint

def input_inf(name):
    x = int(input(f"{name}, введите количество конфет (от 1 до 28): "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректные данные: "))
    return x

def p_print(name, k, count, candies):
    print(f"Игрок {name} взял {k}, всего у игрока {count} конфет. На столе {candies} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ") #для бота: player2 = "Компьютер"
candies = int(input("Введите количество конфет на столе: "))
game_move = randint(0,2) 
if game_move:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count1 = 0 
count2 = 0

while candies > 28:
    if game_move:
        k = input_inf(player1)
        count1 += k
        candies -= k
        game_move = False
        p_print(player1, k, count1, candies)
    else:
        k = input_inf(player2) # для бота: k = randint(1, 29)
        count2 += k
        candies -= k
        game_move = True
        p_print(player2, k, count2, candies)

if game_move:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")


