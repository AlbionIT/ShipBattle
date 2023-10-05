from classes import *
from functions import *
import random

# M - miss
# X - попал в корабль
# ▀ - кусок корабля
# 0 - пустое поле
player_desk = Desk()
computer_desk = Desk()

#Расстановка кораблей игрока:
while True:
    try:
        print("Расставьте корабли\nВведите коардинаты носа корабля через пробел")
        player_desk.field_output()
        input_row_col = list(map(int, input("Введите 3х палубный корабль").split()))
        player_ship3_1 = Ship(length=3, row_col=input_row_col)
        if not player_desk.add_ship(player_ship3_1):
            raise ValueError
        print("Ваше поле:")
        player_desk.field_output()

        for i in range(2):
            input_row_col = list(map(int, input("Введите 2х палубный корабль").split()))
            if not player_desk.can_add(input_row_col, 2):
                raise ValueError
            if i == 0:
                player_ship2_1 = Ship(length=2, row_col=input_row_col)
                if not player_desk.add_ship(player_ship2_1):
                    raise ValueError
                print("Ваше поле:")
                player_desk.field_output()
            else:
                computer_ship2_2 = Ship(length=2, row_col=input_row_col)
                if not player_desk.add_ship(computer_ship2_2):
                    raise ValueError
                print("Ваше поле:")
                player_desk.field_output()

        for i in range(4):
            input_row_col = list(map(int, input("Введите 1 палубный корабль").split()))
            if not player_desk.can_add(input_row_col, 1):
                raise ValueError
            if i == 0:
                computer_ship1_1 = Ship(length=1, row_col=input_row_col)
                if not player_desk.add_ship(computer_ship1_1):
                    raise ValueError
                print("Ваше поле:")
                player_desk.field_output()
            elif i == 1:
                player_ship1_2 = Ship(length=1, row_col=input_row_col)
                if not player_desk.add_ship(player_ship1_2):
                    raise ValueError
                print("Ваше поле:")
                player_desk.field_output()
            elif i == 2:
                player_ship1_3 = Ship(length=1, row_col=input_row_col)
                if not player_desk.add_ship(player_ship1_3):
                    raise ValueError
                print("Ваше поле:")
                player_desk.field_output()
            else:
                player_ship1_4 = Ship(length=1, row_col=input_row_col)
                if not player_desk.add_ship(player_ship1_4):
                    raise ValueError
        break
    except ValueError:
        print("Неверные координаты")
        player_desk.clear_desk()

#Расстановка кораблей компутера:
while True:
    try:
        input_row_col[0] = random.randint(1, 6)
        input_row_col[1] = random.randint(1, 6)
        computer_ship3_1 = Ship(length=3, row_col=input_row_col)
        if not computer_desk.add_ship(computer_ship3_1):
            raise ValueError

        for i in range(2):
            input_row_col[0] = random.randint(1, 6)
            input_row_col[1] = random.randint(1, 6)
            if not computer_desk.can_add(input_row_col, 2):
                raise ValueError
            if i == 0:
                computer_ship2_1 = Ship(length=2, row_col=input_row_col)
                if not computer_desk.add_ship(computer_ship2_1):
                    raise ValueError
            else:
                computer_ship2_2 = Ship(length=2, row_col=input_row_col)
                if not computer_desk.add_ship(computer_ship2_2):
                    raise ValueError

        for i in range(4):
            input_row_col[0] = random.randint(1, 6)
            input_row_col[1] = random.randint(1, 6)
            if not computer_desk.can_add(input_row_col, 1):
                raise ValueError
            if i == 0:
                computer_ship1_1 = Ship(length=1, row_col=input_row_col)
                if not computer_desk.add_ship(computer_ship1_1):
                    raise ValueError
            elif i == 1:
                computer_ship1_2 = Ship(length=1, row_col=input_row_col)
                if not computer_desk.add_ship(computer_ship1_2):
                    raise ValueError
            elif i == 2:
                computer_ship1_3 = Ship(length=1, row_col=input_row_col)
                if not computer_desk.add_ship(computer_ship1_3):
                    raise ValueError
            else:
                computer_ship1_4 = Ship(length=1, row_col=input_row_col)
                if not computer_desk.add_ship(computer_ship1_4):
                    raise ValueError
        break
    except ValueError:
        computer_desk.clear_desk()

#print("Поле компа:")
#computer_desk.field_output()

#геймплэй:
n_moves = 1  # счётчик хода, нечётный = игрок, чётный = компутер
print("Делаете выстрел в поле врага, вводя коардинаты точки черз пробел")
while True:
    try:
        if n_moves % 2 == 1:
            print("Ваше поле:")
            player_desk.field_output()
            print("Поле врага:")
            player_desk.field_output_enemy()
            player_shot = list(map(int, input("Сделаете выстрел:").split()))
            if any([player_shot[0] <= 0, player_shot[0] > 6, player_shot[1] <= 0, player_shot[1] > 6]):
                raise ValueError
            if is_miss(row=player_shot[0], col=player_shot[1], desk=computer_desk) == 'hit':
                player_desk.shot(row=player_shot[0], col=player_shot[1], desk=computer_desk)
                if player_desk.is_Win():
                    print("Вы ПОБЕДИТЕЛЬ!!!\nПоздровляю!")
                    break
            elif is_miss(row=player_shot[0], col=player_shot[1], desk=computer_desk) == 'miss':
                player_desk.shot(row=player_shot[0], col=player_shot[1], desk=computer_desk)
                n_moves += 1
            else:
                raise ValueError
        if n_moves % 2 == 0:
            computer_shot = [random.randint(1, 6), random.randint(1, 6)]
            if is_miss(row=computer_shot[0], col=computer_shot[1], desk=player_desk) == 'hit':
                computer_desk.shot(row=computer_shot[0], col=computer_shot[1], desk=player_desk)
                if computer_desk.is_Win():
                    print("Победил непобедимый искусственный интеллект, увы(((")
                    break
            elif is_miss(row=computer_shot[0], col=computer_shot[1], desk=player_desk) == 'miss':
                computer_desk.shot(row=computer_shot[0], col=computer_shot[1], desk=player_desk)
                n_moves += 1
            else:
                raise ValueError
    except ValueError:
        if n_moves % 2 == 1:
            print("Что-то не так, попробуйте снова!")

print("END!")
