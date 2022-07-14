#!/usr/bin/python3

# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.


import my_func

n = my_func.input_int()
bin_number = []

while n > 0:
    bin_number.append(n % 2)
    n //= 2

for i in range(-1,-len(bin_number) - 1,-1):
    print(bin_number[i], end='')  

print()