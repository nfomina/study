n = int(input())
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    matrix[i][n - i - 1] = 1
    for j in range(n - i, n):
        matrix[i][j] = 2

for row in matrix:
    print(*row)


# smart
#
# n = int(input())
# for i in range(n):
#     row = [0 if i < n - 1 - j else 1 if i == n - 1 - j else 2 for j in range(n)]
#     print(*row)