#!/usr/bin/python3

# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.


import my_func

def find_dif(list_in: list) -> float:
    new_list = []
    for elem in list_in:
        elem_str = str(elem)
        new_elem = float('0' + elem_str[elem_str.find('.'):])
        if new_elem != 0:
            new_list.append(new_elem)
    dif = max(new_list) - min(new_list)
    return dif


list_number = my_func.input_list_float_numbers()
print(list_number)

print(find_dif(list_number))