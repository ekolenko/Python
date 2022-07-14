# My function


def is_int(str: str) -> bool:
    try:
        int(str)
        return True
    except ValueError:
        return False


def input_int() -> int:
    str_number = input('--> ')
    while not (is_int(str_number)):
        print('bad input')
        str_number = input('--> ')
    return int(str_number)


def is_number(str: str) -> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False


def input_list_int_numbers() -> list:
    list_dirty = input('--> ').split(' ')
    list_clean = []
    for elem in list_dirty:
        if is_int(elem):
            list_clean.append(int(elem))
    return list_clean


def input_list_float_numbers() -> list:
    list_dirty = input('--> ').split(' ')
    list_clean = []
    for elem in list_dirty:
        if is_number(elem):
            list_clean.append(float(elem))
    return list_clean


