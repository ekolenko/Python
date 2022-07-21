#!/usr/bin/python3

def read_from_file(f_name: str) -> str:
    with open(f_name,'r') as f:
        return f.readline()

a = read_from_file('ex3').split()

b = ' '.join(filter( lambda x: 'абв' not in x, a))

print(b)