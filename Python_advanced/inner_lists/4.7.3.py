n = int(input())
A = [[int(x) for x in input().split()] for _ in range(n)]
m = int(input())

def multiply_matrix(A, B, n):
    C = [[0] * n for a in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = sum([A[i][l] * B[l][j] for l in range(n)])
    return C

res = A.copy()
for _ in range(m-1):
    res = multiply_matrix(res, A, n)

for line in res:
    print(*line)

# simple
#
# n = int(input())
# m1 = [[int(j) for j in input().split()] for i in range(n)]
# m = int(input())
# res = m1
#
# for l in range(m-1):
#     res = [[sum([res[i][p] * m1[p][j] for p in range(n)]) for j in range(n)] for i in range(n)]
#
# for r in res:
#     print(*r)