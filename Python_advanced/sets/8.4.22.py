set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())
set3 = set(int(x) for x in input().split())

print(*sorted(set3 - set1 - set2, reverse = True))