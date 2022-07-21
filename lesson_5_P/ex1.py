#!/usr/bin/python3

def read_from_file(f_name: str) -> str:
    with open(f_name,'r') as f:
        return f.readline()

a = list(map(int,read_from_file('ex1').split()))

for i in range(len(a)):
    if a[i + 1] != a[i] + 1:
        print(a[i]+1)
        break
