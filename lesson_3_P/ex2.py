#!/usr/bin/python3

list_str = ['23423' , '2374', '23432', '746']

a = input('--> ')

find_1 = False

for i in range(len(list_str)):
    if list_str[i].find(a) > -1:
        if find_1:
            print(i)
            break
        else:
            find_1 = True
        
else:
    print('No')