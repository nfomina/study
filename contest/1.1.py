n = int(input())

count = 0
a = 1
res = []
while count <= n:
    res.extend([a]*a)
    count += a
    a += 1

print(*res[0:n])