n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

answer = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            answer = 'NO'
            break
print(answer)
