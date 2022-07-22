#!/usr/bin/python3

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import os
from random import randint
import re
from time import sleep
import sys


k_count = None
g_index = None
g_mod = None

def game_init():
    os.system('clear')
    global k_count
    global g_index
    global g_mod
    k_count = 2021
    g_index = 2
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
   
    for i in range(3,0,-1):
        print(f'Игра начнётся через: {i}')
        sleep(1)
    return True


def game_score():
    os.system('clear')

    suf = ''
    last_digit =  k_count % 10
    last_2digit = k_count % 100
    if last_digit == 1: 
        suf = 'а'
    elif last_digit < 5: 
        suf = 'ы'
    if 10 < last_2digit < 15:
        suf = ''
    
    print(f'На столе {k_count} конфет{suf}')


def input_number():
    str_n = input()
    if re.match(r'^[1-9]$|^[1][0-9]$|^[2][0-8]$', str_n) == None:
        print('Неверный ввод. Введите число от 1 до 28.')
        return False
    else:
        return int(str_n)


def game_round():
    global k_count
    step = False
    while not step:
        print(f'\nХод Игрока {g_index} --> ', end=' ')
        step = input_number()
    k_count -= step
    

def game_bot_round():
    global k_count
    print(f'\nХод Игрока {g_index} (Компьютер) --> ', end=' ')
    if g_mod == 2:
        step = randint(1,28)
    else:
        step = k_count % 29
        if step == 0: 
            step = randint(1,28)
    sleep(1)
    print(step, end=' ', flush=True)
    sleep(2)
    k_count -= step


def game_over():
    os.system('clear')
    print(f'Конфет больше нет!\nПобедил Игрок {g_index}! Поздравляем!')


def game():
    global g_index
    while k_count > 0:
        g_index = g_index % 2 + 1
        player_2 = game_round
        game_score()
        if g_mod > 1:
            player_2 = game_bot_round
        if g_index == 1:
            game_round()
        else:
            player_2()
    game_over()


if game_init():
    game()





