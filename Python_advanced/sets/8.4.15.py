set1 = set([int(x) for x in input().split()])
set2 = set([int(x) for x in input().split()])
print(*sorted(set1 & set2))