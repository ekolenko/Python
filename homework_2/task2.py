# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N

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
    list_n.append(1)
    for i in range(1, n):
        list_n.append(list_n[i - 1] * (i + 1))
    return list_n

n = input_int()
print(fill_list(n))