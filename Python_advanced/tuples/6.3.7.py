n = int(input())

f1, f2, f3 = 1, 1, 1
res = []
for i in range(n):
    res.append(f1)
    f1, f2, f3 = f2, f3, f1 + f2 + f3

print(*res)