#!/usr/bin/python3

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.


from random import randint
import my_func


def get_coef(n: int) -> list:
    list_coef = []
    for i in range(n + 1):
        list_coef.append(randint(0,100))
    return list_coef


def get_str_m(list_in: list) -> str:
    str_m =''
    for i in range(n, -1, -1):
        if list_in[i] != 0:
            match i:
                case 1: 
                    str_m += ' + ' + str(list_in[i]) + 'x'
                case 0:
                    str_m += ' + ' + str(list_in[i])
                case __:
                    str_m += ' + ' + str(list_in[i]) + 'x' + my_func.int_to_pow(i)

    if len(str_m) > 0:
        str_m += ' = 0'
    return str_m[3:]

def write_to_file(str_in: str):
    file_name ='task4.txt'
    with open(file_name,'w') as f:
        f.write(str_in)


n = my_func.input_int()
list_coef = get_coef(n)
str_m = get_str_m(list_coef)
print(str_m)
write_to_file(str_m)