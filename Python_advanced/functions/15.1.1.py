
def matrix(n=1, m=None, value=0):
    if not m:
        m = n
    return [[value for _ in range(m)] for i in range(n)]

print(matrix())                   # матрица 1 × 1 из 0
print(matrix(3))                  # матрица 3 × 3 из 0
print(matrix(2, 5))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))            # матрица 3 × 4 из 9