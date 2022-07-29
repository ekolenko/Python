#!/usr/bin/python3

import sys
from app.controller import ctrl

g_mod = None # выбор графического интерфейса

d_mod = None # выбор 

def init():
    
    # Выбор графического интерфейса
    # 1 - CLI
    # 2 - GUI
    global g_mod

    # Выбор типа хранилища
    # 1 - SQLite
    # 2 - CSV
    global d_mod

    for i in range(1, len(sys.argv)):
        match sys.argv[i]:
            case '-gui': 
                g_mod = 2
            case '-cli':
                g_mod = 1
            case '-sql':
                d_mod = 1
            case '-csv':
                d_mod = 2
            case '-msql':
                d_mod = 3
            case __:
                print('Неверный ввод параметров')
                return False

    if g_mod == None:
        g_mod = 2
        print('Выбран режим по умолчанию: CLI')

    if d_mod == None:
        d_mod = 1
        print('Выбран режим по умолчанию: SQLite')
    
    return True

if init():
    ctrl.init(g_mod, d_mod)