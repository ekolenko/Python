#!/usr/bin/python3

import time

def randomize(a,b):

    t = time.time_ns()

    tail = t % 100000


    str_float = '0.' + str(tail)

    koef = float(str_float)
    
    print (koef)

    return int((a + (b - a) * koef))

print(randomize(500,1000))