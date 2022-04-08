n = int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

max = matrix[0][0]
for i in range(n):
    for j in range(n):
        if i > j and i < n-1-j:
            if matrix[i][j] > max:
                max = matrix[i][j]
        if i < j and i > n-1-j:
            if matrix[i][j] > max:
                max = matrix[i][j]
print(max)
