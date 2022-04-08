# Латинским квадратом порядка n называется квадратная матрица размером n×n,
# каждая строка и каждый столбец которой содержат все числа от 1 до n.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

n = int(input())

matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

numbers = [i for i in range(1, n+1)]
answer = 'YES'
for line in matrix:
    if set(line)!=set(numbers):
        answer = 'NO'
        break
for i in range(len(matrix)):
    for j in range(i , len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for line in matrix:
    if set(line)!=set(numbers):
        answer = 'NO'
        break
print(answer)


# Without set
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# numbers = list(range(1, n + 1))
# result = 'YES'
#
# for i in range(n):
#     row_nums = sorted(matrix[i])
#     col_nums = sorted([matrix[j][i] for j in range(n)])
#     if row_nums != numbers or col_nums != numbers:
#         result = 'NO'
#         break
#
# print(result)