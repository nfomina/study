n, m = [int(a) for a in input().split()]
matrix = [[0]*m for _ in range(n)]

if n == 1:
    matrix = [int(i) for i in range(1, m + 1)]
    print(*matrix)
elif m == 1:
    matrix = [int(i) for i in range(1, n + 1)]
    for item in matrix:
        print(item)
else:
    numbers = (a for a in range (1, m*n+1))
    if m == n:
        matrix[m // 2][n // 2] = m * n

    i, j = 0, 0
    while matrix[i][j] == 0 and (m > 0 or n > 0):
        for right in range(i, m+i-1):
            matrix[i][right] = next(numbers)
        j = right + 1
        m = m - 1
        for down in range(i, n+i-1):
            matrix[down][j] = next(numbers)
        i = down + 1
        n = n - 1
        for left in range(j, j - m, -1):
            matrix[i][left] = next(numbers)
        j = left - 1
        m = m - 1
        for up in range(i, i - n, -1):
            matrix[up][j] = next(numbers)
        i = up
        n = n - 1
        j += 1

    for line in matrix:
        print(*line)


# amazing
# n, m = map(int, input().split())
# a = [[0] * m for _ in range(n)]
# dr, dc, r, c = 0, 1, 0, 0
#
# for cnt in range(1, n * m + 1):
#     a[r][c] = cnt
#
#     if a[(r + dr) % n][(c + dc) % m]:
#         dr, dc = dc, -dr
#
#     r += dr
#     c += dc
#
# for row in a:
#     print(*(f'{e:<3}' for e in row), sep='')

