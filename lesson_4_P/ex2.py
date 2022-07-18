#!/usr/bin/python3

f = open('file','r+')

f.write('\nq')

coef = f.readlines()

print(coef)

f.write('\n')
# f.write(str(a + b +c))

f.close()