n = int(input())
m = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

i, j = [int(a) for a in input().split()]

for rows in matrix:
    rows[j], rows[i] = rows[i], rows[j]

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()

## beautiful

# n, m = int(input()), int(input())
# matrix = [input().split() for _ in range(n)]
# col1, col2 = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
#
# for row in matrix:
#     print(*row)