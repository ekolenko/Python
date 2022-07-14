#!/usr/bin/python3

# def is_number(str: str) -> bool:
#     try:
#         float(str)
#         return True
#     except ValueError:
#         return False


# def input_number() -> str:
#     str_number = input('--> ')
#     while not (is_number(str_number)):
#         print('bad input')
#         str_number = input('--> ')
#     return str_number

list_str = ['23423' , '234', '23432', '746']

a = input('--> ')

for str_temp in list_str:
    if str_temp.find(a) > -1:
        print('Yes')
        break
else:
    print('No')

