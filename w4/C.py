DIRS = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

board = [[False for _ in range(5)] for _ in range(5)]


def position_valid(y, x):
    return 0 <= y < 5 and 0 <= x < 5


def check_position(y, x):
    for di in DIRS:
        dy, dx = di
        yy, xx = y + dy, x + dx
        if position_valid(yy, xx):
            if board[yy][xx]:
                return False
    return True


# .x.x.
# x...x
# ..k..
# x...x
# .x.x.

nk = 0

for i in range(5):
    s = input()
    for j in range(5):
        if s[j] == 'k':
            nk += 1
        board[i][j] = s[j] == 'k'

if nk != 9:
    print('invalid')
else:
    valid = True
    for i in range(5):
        for j in range(5):
            if board[i][j]:
                if not check_position(i, j):
                    valid = False
                    break
        if not valid:
            break
    print('valid' if valid else 'invalid')
