n, m = [int(a) for a in input().split()]

numbers = [i for i in range(1, n*m+1)]

for i in range(0, len(numbers), m):
    print(*numbers[i:i+m])


# short
#
# n, m = [int(i) for i in input().split()]
#
# for i in range(1, (n * m) + 1):
#     print(str(i).ljust(2), end=' ')
#     if i % m == 0:
#         print()