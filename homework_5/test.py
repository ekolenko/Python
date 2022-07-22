board = {}
for i in range(1,4):
        for y in range(1,4):
            board[i,y] = str(i) + str(y)

board[1,1] = 'x'
board[1,2] = 'x'
board[1,3] = 'x'


def check_combination(f):
    global win_combination
    check_dict = dict(filter(f,board.items()))
    if tuple(check_dict.values()).count('x' if 1 == 1 else 'o') == 3:
        win_combination = tuple(check_dict.keys())
        print(check_dict)
        print(win_combination)
        input()
        return True
    return False


def win_condition() -> bool:
    for i in range(1,4):
        if check_combination(lambda x: x[0][0] == i):
            return True
        if check_combination(lambda x: x[0][1] == i):
            return True
    if check_combination(lambda x: x[0][0] == x[0][1]):
            return True
    if check_combination(lambda x: abs(x[0][0] - x [0][1])%2 == 0):
            return True
    return False

win_condition()