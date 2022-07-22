#!/usr/bin/python3

# Создайте программу для игры в "Крестики-нолики".

import os
from random import randint
import re
from time import sleep
import sys

board = {}
g_index = None
g_mod = None
roud_count = None
win_combination = None
lambda_list = []


def lambda_init():
    global lambda_list
    
    lambda_list.append(lambda x: x[0][0] == 1)
    lambda_list.append(lambda x: x[0][1] == 1)
    lambda_list.append(lambda x: x[0][0] == 2)
    lambda_list.append(lambda x: x[0][1] == 2)  
    lambda_list.append(lambda x: x[0][0] == 3)
    lambda_list.append(lambda x: x[0][1] == 3)          
    lambda_list.append(lambda x: x[0][0] == x[0][1])            
    lambda_list.append(lambda x: abs(x[0][0] - x [0][1]) == 2 or x[0][0] == x[0][1] == 2)


def game_init():

    os.system('clear')

    global board
    global g_index
    global g_mod
    global roud_count
    
    for i in range(1,4):
        for y in range(1,4):
            board[i,y] = ' '

    roud_count = 0

    if len(sys.argv) == 1:
        g_mod = 1
        print('Выбран режим по умолчанию: человек против человека.')
    elif len(sys.argv) == 2:
        match sys.argv[1]:
            case '-1': 
                g_mod = 1
                print('Выбран режим: человек против человека.')
            case '-2':
                g_mod = 2
                print('Выбран режим: человек против компьютера.')
            case '-3':
                g_mod = 3
                print('Выбран режим: человек против искуственного интелекта.')
            case __:
                print('Неверный ввод параметра. Выбор режима [-(1:3)]')
                return False
    else:
        print('Неверное количество параметров. Выбор режима [-(1:3)]')
        return False
    
    g_index = randint(1,2)

    lambda_init()

    print(f'\nИгрок {g_index % 2 + 1} начинает первым.\n')
   
    for i in range(3,0,-1):
        print(f'Игра начнётся через: {i}')
        sleep(1)
    
    return True


def game_score():
    os.system('clear')
    print('----------- ')
    for i in range(1,4):        
        print(' ' + ' | '.join([board[i,y] for y in range(1,4)]))
        print('----------- ')


def game_win_score():
    os.system('clear')
    print('----------- ')
    for i in range(1,4):        
        print(' ' + ' | '.join([ ('\033[32m'+board[i,y]+'\033[0m' if (i,y) in win_combination else board[i,y]) for y in range(1,4)]))
        print('----------- ')


def input_coordinates():
    str_n = input()
    if re.match(r'^[1-3]{2}$', str_n) == None:
        print('Неверный ввод. Введите координаты без пробела')
        return False
    else:
        return str_n


def check_coordinates(coord: str):
    
    if not coord:
        return False

    if board[int(coord[0]),int(coord[1])] == ' ':
        return coord

    else:
        print('Ячейка поля занята!')
        return False


def find_coord():
    for str_xo in ('o','x'):
        for f in lambda_list:
            coord_line = check_bot_combination(f,str_xo)

            if type(coord_line) == tuple:                
                for coord in coord_line:
                    if board[coord] == ' ':
                        return coord  

    list_coord = [ key for key in board.keys() if board[key] == ' ']
    coord = list_coord[randint(0,len(list_coord) - 1)]
    return  coord


def game_round():
    global board
    coord = False
    while not coord:
        print(f'\nХод Игрока {g_index} --> ', end=' ')
        coord = input_coordinates()
        coord = check_coordinates(coord)
    board[int(coord[0]),int(coord[1])] = 'x' if g_index == 1 else 'o'    


def game_bot_round():
    global board
    print(f'\nХод Игрока {g_index} (Компьютер) --> ', end=' ')
    if g_mod == 2:
        list_coord = [ key for key in board.keys() if board[key] == ' ']
        coord = list_coord[randint(0,len(list_coord) - 1)]
        
    else:
        if board[(2,2)] == ' ':
            coord = (2,2)
        else:
            coord = find_coord()            
    sleep(1)
    print(str(coord[0]) + str(coord[1]), end=' ', flush=True)
    sleep(1)
    board[coord] = 'o'


def game_over(is_draw):
    os.system('clear') 
    if is_draw:
        game_score() 
        print(f'\nНичья! Победила дружба!\n')
    else:
        game_win_score()
        print(f'\nПобедил Игрок {g_index}! Поздравляем!\n')


def game():
    global g_index
    global roud_count
    while not win_condition():
        g_index = g_index % 2 + 1
        if roud_count > 8:
            game_over(True)
            return
        player_2 = game_round
        game_score()
        if g_mod > 1:
            player_2 = game_bot_round
        if g_index == 1:
            game_round()
        else:
            player_2()
        roud_count += 1        
    game_over(False)


def check_win_combination(f) -> bool:
    global win_combination
    check_dict = dict(filter(f,board.items()))
    if tuple(check_dict.values()).count('x' if g_index == 1 else 'o') == 3:
        win_combination = tuple(check_dict.keys())
        return True
    return False


def check_bot_combination(f,str_xo):
    check_dict = dict(filter(f,board.items()))
    if tuple(check_dict.values()).count(str_xo) == 2 and tuple(check_dict.values()).count(' ') == 1:
        return tuple(check_dict.keys())
    return False


def win_condition() -> bool:
    for f in lambda_list:
            if check_win_combination(f):
                return True
    return False
    

if game_init():
    game()






