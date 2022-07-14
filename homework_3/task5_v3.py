#!/usr/bin/python3

# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

## без рекурсии, добавление отрицательных по другой формуле

import my_func


def get_fib_dict(n):

    tmp_dict = {}

    for i in range(n + 1):
        match i:
            case 0: tmp_dict[i] = 0
            case 1: tmp_dict[i] = 1
            case _: tmp_dict[i] = tmp_dict[i - 2] + tmp_dict[i - 1]
    
    return tmp_dict


def add_neg_fib(in_dict: dict):
    for i in range(1, len(in_dict)):
        in_dict[-i] = ((-1) ** (i + 1)) * in_dict[i]


def get_fib_list(in_dict: dict) -> list:
    fib_list = []
    for i in sorted(in_dict.keys()):
        fib_list.append(in_dict[i])
    return fib_list


n = my_func.input_int()

n = abs(n)

fib_dict = get_fib_dict(n)

add_neg_fib(fib_dict)

fib_list = get_fib_list(fib_dict)

print(fib_list)