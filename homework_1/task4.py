a = int(input('--> '))

match a:
    case 1:
        print('x > 0 and y > 0')
    case 2:
        print('x > 0 and y < 0')
    case 3:
        print('x < 0 and y < 0')
    case 4:
        print('x < 0 and y > 0')
    case _:
        print('bad value')