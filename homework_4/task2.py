#!/usr/bin/python3

# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N

import my_func
import math


def check_simple(a: int) -> bool:
    i = 2
    while i <= math.sqrt(a):
        if a % i == 0:
            return False
        i += 1
    return True


def find_simple(n: int) -> list:
    list_simple = []
    i = 2
    while i <= n / 2:
        if n % i == 0 and check_simple(i):
            list_simple.append(i)
        i += 1
    return list_simple




n = my_func.input_int()
print(find_simple(n))