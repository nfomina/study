mapping = {'a': 0,
           'b': 1,
           'c': 2,
           'd': 3,
           'e': 4,
           'f': 5,
           'g': 6,
           'h': 7}

n = 8
matrix = [['.']*n for _ in range(n)]

horse = input()
horse_c = [n - int(horse[1]), mapping.get(horse[0])]

matrix[horse_c[0]][horse_c[1]] = 'N'

if n-horse_c[0]<7:
    if n-horse_c[1]<8:
        matrix[horse_c[0]-2][horse_c[1]-1] = '*'
    if n-horse_c[1]>1:
        matrix[horse_c[0]-2][horse_c[1]+1] = '*'

if horse_c[0]+2<8:
    if n-horse_c[1]<8:
        matrix[horse_c[0]+2][horse_c[1]-1] = '*'
    if n-horse_c[1]>1:
        matrix[horse_c[0]+2][horse_c[1]+1] = '*'

if n-horse_c[1]<7:
    if n-horse_c[0]<8:
        matrix[horse_c[0]-1][horse_c[1]-2] = '*'
    if horse_c[0]+2<=8:
        matrix[horse_c[0]+1][horse_c[1]-2] = '*'

if horse_c[1]+2<8:
    if n-horse_c[0]<8:
        matrix[horse_c[0]-1][horse_c[1]+2] = '*'
    if horse_c[0]+2<=8:
        matrix[horse_c[0]+1][horse_c[1]+2] = '*'

for row in matrix:
    print(*row)


# beautiful:
#
# x, y = input()
# n = 8
# board = [['.'] * n for _ in range(n)]
# x = ord(x) - 97
# y = n - int(y)
# board[y][x] = 'N'
#
# for i in range(n):
#     for j in range(n):
#         if abs(y - i) * abs(x - j) == 2:
#             board[i][j] = '*'
#
# for row in board:
#     print(*row)