n = int(input())
m = int(input())
matrix = []

_max = None
for _ in range(n):
    elem = [int(i) for i in input().split()]
    if _max is None or max(elem)>_max:
        _max = max(elem)
        index = [_, elem.index(_max)]

print(*index)
