from itertools import product

n = int(input())
m = 2
k = 1
sum_ = 0

for m in range(2, n):
    for i in product([k*(k+1) for k in range(1, n//2)], repeat=m):
        if sum(i) == n:
            sum_ = sum(i)
            print(m)
            break
    if sum_ == n:
        break