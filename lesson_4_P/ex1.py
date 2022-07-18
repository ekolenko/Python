#!/usr/bin/python3


from curses.ascii import isdigit


def is_int(str: str) -> bool:
    try:
        int(str)
        return True
    except ValueError:
        return False


def input_list_int_numbers(str_in: str) -> list:
    list_dirty = str_in.split(' ')
    list_clean = []
    for elem in list_dirty:
        if is_int(elem):
            list_clean.append(int(elem))
    return list_clean

f = open('str_file', 'r')
str_in = f.readline()
f.close()

numb_list = input_list_int_numbers(str_in)

print(numb_list)
print(max(numb_list))
print(min(numb_list))

print(isdigit('2354'))