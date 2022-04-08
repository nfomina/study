n = int(input())

all_set = set()
for _ in range(n-1):
    new_set = set(input())
    if all_set:
        all_set = new_set & all_set
    else:
        all_set = new_set

print(*sorted(all_set & set(input())))