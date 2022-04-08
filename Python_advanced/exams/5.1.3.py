n = int(input())

matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(len(matrix)):
    for j in range(i , len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for line in matrix:
    print(*line)