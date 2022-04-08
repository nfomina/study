n = int(input())

matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

max_ = matrix[n-1][n-1]
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            if matrix[i][j] > max_:
                max_ = matrix[i][j]
print(max_)