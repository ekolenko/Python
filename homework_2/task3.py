# Задайте список из n чисел последовательности 
# (1 + 1/n)^n и выведите на экран их сумму.

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


def fill_list(n: int) -> list:
    list_n = []
    for i in range(1, n + 1):
        list_n.append((1 + 1 / i) ** i)
    return list_n

n = input_int()
sum_list_n = sum(fill_list(n))
print(sum_list_n)