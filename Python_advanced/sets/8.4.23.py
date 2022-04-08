set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())
set3 = set(int(x) for x in input().split())

set_all = set(i for i in range(11))
print(*sorted(set_all - set1 - set2 - set3))