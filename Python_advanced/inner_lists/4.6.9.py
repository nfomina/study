# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m заполнив её "диагоналями" в соответствии с образцом.
#
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# 3 5
# Sample Output 1:
#
# 1  2  4  7  10
# 3  5  8  11 13
# 6  9  12 14 15

n, m = [int(a) for a in input().split()]

numbers = [i for i in range(1, n*m+1)]

matrix = [[0]*m for _ in range(n)]

nm = 0
for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                nm += 1
                matrix[i][j] = nm

for line in matrix:
    print(*line)

# smart
#
# n, m = map(int, input().split())
#
# matrix = [[0] * m for _ in range(n)]
# total = 1
# for l in range(n * m ):
#     for i in range(n):
#         for j in range(m):
#             if i + j == l:
#                 matrix[i][j] = total
#                 total += 1
# for i in range(n):
#     print(*matrix[i])