n, m = [int(a) for a in input().split()]

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for _ in range(steps):
            lst.append(lst.pop(0))
    else:
        for _ in range(steps):
            lst.insert(0, lst.pop())
    return lst

numbers = [a for a in range(1, m + 1)]
print(*numbers)

for i in range(n-1):
    numbers = shift(numbers, -1)
    print(*numbers)


# simple
#
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()