#!/usr/bin/python3

# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 2 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def get_fib_dict(n: int) -> dict:
    temp_dict ={}
    for i in range(n + 1):
        temp_dict[i] = fib(i)
    return temp_dict


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
