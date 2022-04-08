n, m = [int(a) for a in input().split()]

numbers = [i for i in range(1, n*m+1)]

for i in range(0, len(numbers)//m):
    for j in range(i, len(numbers), n):
        print(numbers[j], end =' ')
    print()