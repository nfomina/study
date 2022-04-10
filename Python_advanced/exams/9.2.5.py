first = set(int(i) for i in input().split())
second = set(int(i) for i in input().split())

if first & second:
    print(*sorted(first&second, reverse=True))
else:
    print('BAD DAY')