n = int(input())

matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

answer = 'YES'
for k in range(n):
    for l in range(n):
        if matrix[k][l]!=matrix[n-l-1][n-k-1]:
            answer = 'NO'
            break

print(answer)
