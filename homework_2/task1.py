# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

def is_number(str: str) -> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False


def input_number() -> str:
    str_number = input('--> ')
    while not (is_number(str_number)):
        print('bad input')
        str_number = input('--> ')
    return str_number


def sum_digits(str_number: str) -> int:
    sum = 0
    for char_ in str_number:
        if char_ == '.':
            continue
        else:
            sum += ord(char_) - 48
    return sum


a = input_number()
print(sum_digits(a))



