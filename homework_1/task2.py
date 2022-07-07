
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, not (x and y and z)  == (not x or not y or not z))
            