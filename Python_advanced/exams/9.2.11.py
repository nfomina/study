m = int(input())

all_set = set()
for _ in range(m):
    n = int(input())
    new_set = set()
    for i in range(n):
        new_set.add(input())
    if all_set:
        all_set = new_set & all_set
    else:
        all_set = new_set

for item in sorted(all_set):
    print(item)

