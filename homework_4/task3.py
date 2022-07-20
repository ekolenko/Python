#!/usr/bin/python3

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.



file_name = 'task3.txt'

with open(file_name,'r') as f:
    str_numbers = f.readline()

list_numbers = str_numbers.split()

dict_numbers = {}

for elem in list_numbers:
    if elem in dict_numbers:
        dict_numbers[elem] += 1
    else:
        dict_numbers[elem] = 1

for key, value in dict_numbers.items():
    if value == 1:
        print(key, end = ' ')

print()
