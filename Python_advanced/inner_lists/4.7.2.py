n, m = [int(x) for x in input().split()]

A = [[int(x) for x in input().split()] for _ in range(n)]
input()

m, k = [int(x) for x in input().split()]
B = [[int(x) for x in input().split()] for _ in range(m)]

C = [[0]*k for a in range(n)]

for i in range(n):
    for j in range(k):
        C[i][j] = sum([A[i][l]*B[l][j] for l in range(m)])


for line in C:
    print(*line)