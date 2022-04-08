n, m = [int(a) for a in input().split()]
matrix1, matrix2 = [], []

for _ in range(n):
    elem = [int(i) for i in input().split()]
    matrix1.append(elem)

space = input()

for _ in range(n):
    elem = [int(i) for i in input().split()]
    matrix2.append(elem)

sum_matrix = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

for line in sum_matrix:
    print(*line)

# short
#
# n, m = [int(x) for x in input().split()]
#
# A = [[int(x) for x in input().split()] for _ in range(n)]
# input()
# B = [[int(x) for x in input().split()] for _ in range(n)]
#
# C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
#
# for x in C:
#     print(*x)


