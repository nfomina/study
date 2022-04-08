n, m = [int(a) for a in input().split()]

matrix = []

for _ in range(n):
    if _%2 == 0:
        line = ['.', '*']*(m//2)
        if m%2 != 0:
            line.append('.')
    else:
        line = ['*', '.'] * (m // 2)
        if m % 2 != 0:
            line.append('*')
    matrix.append(line)

for rows in matrix:
    print(*rows)


# smart
#
# n, m = [int(i) for i in input().split()]
# board = [['.'] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(1 - i % 2, m, 2):
#         board[i][j] = '*'
#
# for row in board:
#     print(*row)