#!/usr/bin/python3

# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.


def read_from_file(f_name: str) -> str:
    with open(f_name,'r') as f:
        return f.readline()

a = list(map(int,read_from_file('ex2').split()))


tmp = a[0]
lst = [a[0]]
for i in range(len(a)):
    if a[i] > tmp:
        lst.append(a[i])
        tmp = a[i]

print(lst)


