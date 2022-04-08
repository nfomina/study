n = int(input())

pupils = []
for _ in range(n):
    family, mark = input().split()
    pupils.append((family, int(mark)))

for item in pupils:
    print(*item)

print()

for item in pupils:
    if item[1] == 4 or item[1] == 5:
        print(*item)