a = int(input())
b = int(input())


print(*filter(None, map(lambda x: x if '0' not in str(x) and all(map(lambda i: x % i == 0 ,[int(i) for i in str(x)])) else None, range(a, b + 1))))
