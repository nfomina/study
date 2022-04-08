n = int(input())

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1
        elif j == n-i-1:
            matrix[i][j] = 1

for row in matrix:
    print(*row)

# in one line
#
# n = int(input())
#
# res = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]
#
# for x in res:
#     print(*x)