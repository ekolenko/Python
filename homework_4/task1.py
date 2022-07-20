#!/usr/bin/python3

# Вычислить число Пи c заданной точностью d

import re


def get_pi(acc: int) -> float:
    a = 0
    for k in range(acc):
        a += ( 16 ** (-k)  ) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
    return a  


def input_accurancy() -> int:
    str_in = input('--> ')   
    reg_exp = re.match(r'^[0][.][0-1]+$',str_in)
    while reg_exp == None or len(str_in) > 12:
        print('bad input')
        str_in = input('--> ')
        reg_exp = re.match(r'^[0][.][0-1]+$',str_in)
    else:
        return len(str_in)


d = input_accurancy()
pi_string = str(get_pi(d - 2))
print(pi_string[:d])