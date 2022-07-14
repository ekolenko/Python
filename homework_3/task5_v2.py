#!/usr/bin/python3

# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

## без рекурсии


def get_fib_dict(n):

    tmp_dict = {}

    for i in range(n + 1):
        match i:
            case 0: tmp_dict[i] = 0
            case 1: tmp_dict[i] = 1
            case 2: tmp_dict[i] = 1
            case _: tmp_dict[i] = tmp_dict[i - 2] + tmp_dict[i - 1]
    
    return tmp_dict


def add_neg_fib(in_dict: dict):
    for i in range(1, len(in_dict)):
        in_dict[-i] = in_dict[-i + 2] - in_dict[-i + 1]


def get_fib_list(in_dict: dict) -> list:
    fib_list = []
    for i in sorted(in_dict.keys()):
        fib_list.append(in_dict[i])
    return fib_list


n = int(input('--> '))

fib_dict = get_fib_dict(n)

add_neg_fib(fib_dict)

fib_list = get_fib_list(fib_dict)

print(fib_list)