
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)




for i in range(n):
    for j in range(n):
        if abs(x-j) == abs(y-i):
            board[i][j] = '*'
board[y][x] = 'Q'
for i in range(n):
    if board[i][x] != 'Q':
        board[i][x] = '*'
    if board[y][i] != 'Q':
        board[y][i] = '*'

for row in board:
    print(*row)