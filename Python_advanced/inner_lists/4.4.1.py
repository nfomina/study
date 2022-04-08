n = int(input())
m = int(input())

matrix = []
for i in range(n):
    line = [input() for word in range(m)]
    matrix.append(line)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]), end=' ')
    print()