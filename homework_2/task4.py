# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции задаются с клавиатуры через пробел.


from random import randint


def is_int(str: str) -> bool:
    try:
        int(str)
        return True
    except ValueError:
        return False


def input_int() -> int:
    str_number = input('N --> ')
    while not (is_int(str_number)):
        print('bad input')
        str_number = input('N --> ')
    return int(str_number)


def fill_list(n: int) -> list:
    list_n = []
    for i in range(n):
        list_n.append(randint(-n, n))
    return list_n


def fill_index(max_value: int) -> list:
    str_in = input('Indexes --> ')
    str_index_dirty = str_in.split(' ')
    str_index_clean = []
    for index in str_index_dirty:
        if  is_int(index) and int(index) < max_value:
                str_index_clean.append(int(index))
    return str_index_clean


def mult_list(list_n: list, index_list: list) -> int:
    mult = 1
    for index in index_list:
        mult *= list_n[index]
    return mult


n = input_int()
list_n = fill_list(n)

print(list_n)

index_list = fill_index(n)

if len(index_list) > 0:
    print(mult_list(list_n, index_list))
else:
    print('index list empty')

