from sympy.utilities.iterables import multiset_permutations

n, k = map(int, input().split())


def isValid(c, n):
    X = [0, -1, 0, 1]
    Y = [1, 0, -1, 0]
    isValid = True
    for i in range(n):
        for j in range(n):
            for k in range(n):
                newX = i + X[k]
                newY = j + Y[k]
                if (newX < n and newY < n and
                        newX >= 0 and newY >= 0 and
                        c[newX][newY] == c[i][j]):
                    isValid = false
    return isValid


numbers = []
if (n*n) % k != 0:
    print('No')
else:
    for i in range(1, k+1):
        numbers.extend(str(i)*(n//k))
print(numbers)

for i in multiset_permutations(numbers):
    print(i, end=' ')