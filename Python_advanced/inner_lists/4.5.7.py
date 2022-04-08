n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n//2):
    matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

matrix = list(map(list, zip(*matrix)))

for row in matrix:
    print(*row)

# beautiful
#
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# result = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         result[i][j] = matrix[n - j - 1][i]
#
# for row in result:
#     print(*row)