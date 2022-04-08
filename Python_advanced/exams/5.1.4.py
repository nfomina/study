n = int(input())

matrix = [['.']*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j or j == n - i - 1:
            matrix[i][j] = '*'
for i in range(n):
    matrix[n//2][i] = '*'
    matrix[i][n//2] = '*'

for line in matrix:
    print(*line)