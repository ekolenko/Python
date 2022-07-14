#!/usr/bin/python3

# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.


import my_func

list_number = my_func.input_list_int_numbers()
print(list_number)

sum = 0

for i in range(1,len(list_number),2):
    sum += list_number[i]

print(sum)
