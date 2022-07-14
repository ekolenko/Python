#!/usr/bin/python3

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


import my_func

list_number = my_func.input_list_int_numbers()
print(list_number)

result_list = []

half_len = (len(list_number) + 1) // 2

for i in range(half_len):
    result_list.append(list_number[i] * list_number[-i-1])
    
print(result_list)
