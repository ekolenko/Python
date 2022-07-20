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


def pow_to_int(str_pow: str) -> int:
    str_int_pow = ''
    dict_pow = {    
        '\u00B9' : '1',
        '\u00B2' : '2',
        '\u00B3' : '3',
        '\u2074' : '4',
        '\u2075' : '5',
        '\u2076' : '6',
        '\u2077' : '7',
        '\u2078' : '8',
        '\u2079' : '9',
        '\u2070' : '0' 
        }
    for char in str_pow:
        str_int_pow += dict_pow[char]
    
    return int(str_int_pow)


def int_to_pow(int_pow: int) -> str:
    str_pow = ''
    dict_pow = {    
        '1' : '\u00B9',
        '2' : '\u00B2',
        '3' : '\u00B3',
        '4' : '\u2074',
        '5' : '\u2075',
        '6' : '\u2076',
        '7' : '\u2077',
        '8' : '\u2078',
        '9' : '\u2079',
        '0' : '\u2070' 
        }
    for char in str(int_pow):
        str_pow += dict_pow[char]
    return str_pow