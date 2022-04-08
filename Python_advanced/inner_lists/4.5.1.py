n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    matrix.append([0] * m)

for i in range(n):
    for j in range(m):
        matrix[i][j] = i*j

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()