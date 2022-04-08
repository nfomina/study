n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i]

for row in matrix:
    print(*row)


## beautiful

# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for row in matrix:
#     print(*row)