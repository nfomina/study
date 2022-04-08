n = int(input())

new_set = set()
for _ in range(n):
    items = set(input().lower())
    for item in items:
        new_set.add(item)
print(len(new_set))