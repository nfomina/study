n, X, Y, A, B = [int(i) for i in input().split()]

first_list = [i for i in range(1, n+1)]
first_list[X-1:Y] = first_list[X-1:Y][::-1]
first_list[A-1:B] = first_list[A-1:B][::-1]

print(*first_list)
