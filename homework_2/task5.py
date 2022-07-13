# Реализуйте алгоритм перемешивания списка.

from random import randint

def is_int(str: str) -> bool:
    try:
        int(str)
        return True
    except ValueError:
        return False


def input_int() -> int:
    str_number = input('List size --> ')
    while not (is_int(str_number)):
        print('bad input')
        str_number = input('List size --> ')
    return int(str_number)

def random_list(n: int) -> list:
    out_list = []
    for i in range(n):
        out_list.append(randint(0,99))
    return out_list


def mix_list(in_list: list) -> list:
    out_list =[]
    size_list = len(in_list)
    max_index = size_list - 1
    for i in range(size_list):
        rand_index = randint(0, max_index - i)
        rand_element = in_list.pop(rand_index)
        out_list.append(rand_element)
    return out_list     


n = input_int()
rand_list = random_list(n)

print(rand_list)

mixed_list = mix_list(rand_list)

print(mixed_list)



