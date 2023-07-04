n = int(input())
matrix = [[1 for i in range(n)] for j in range(n)]


for i in range(n):
    for j in range(n):
        matrix[i][j] = min(i+1, j+1, n-i, n-j)

for line in matrix:
    print(*line)
