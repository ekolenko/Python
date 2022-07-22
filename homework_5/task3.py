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
        print(' ' + ' | '.join([ ('\033[33m'+board[i,y]+'\033[0m' if (i,y) in win_combination else board[i,y]) for y in range(1,4)]))
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
    board_lst = get_board_lst()
    find_ind = 8
    for i in range(len(board_lst)):
        if re.match(r'^[o][ ][o]$|^[o][o][ ]$|^[ ][o][o]$',board_lst[i]) != None:
            find_ind = i
            find_pos = board_lst[i].index(' ')
            return return_coord(find_ind, find_pos)
    
    for i in range(len(board_lst)):
        if re.match(r'^[x][ ][x]$|^[x][x][ ]$|^[ ][x][x]$',board_lst[i]) != None:
            find_ind = i
            find_pos = board_lst[i].index(' ')
            return return_coord(find_ind, find_pos)
    
    return return_coord(8,None)
    

def return_coord(find_ind: int,find_pos: int) -> tuple:

    match find_ind:
        case 0:
            return (1, find_pos + 1)
        case 1:
            return (find_pos + 1, 1)
        case 2:
            return (2, find_pos + 1)
        case 3:
            return (find_pos + 1, 2)
        case 4:
            return (3, find_pos + 1)
        case 5:
            return (find_pos + 1, 3)
        case 6:
            return (find_pos + 1, find_pos + 1) 
        case 7:
            return (3 - find_pos , find_pos + 1)   
        case 8:
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
    sleep(2)
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


def check_combination(f):
    global win_combination
    check_dict = dict(filter(f,board.items()))
    if tuple(check_dict.values()).count('x' if g_index == 1 else 'o') == 3:
        win_combination = tuple(check_dict.keys())
        return True
    return False


def win_condition() -> bool:
    for i in range(1,4):
        if check_combination(lambda x: x[0][0] == i):
            return True
        if check_combination(lambda x: x[0][1] == i):
            return True
    if check_combination(lambda x: x[0][0] == x[0][1]):
            return True
    if check_combination(lambda x: abs(x[0][0] - x [0][1]) == 2 or x[0][0] == x[0][1] == 2):
            return True
    return False
    

if game_init():
    game()






