from itertools import combinations_with_replacement


wallet = [100, 50, 20, 10, 5]

min_element = min(wallet)
count_r = 100//min_element

all_combinations = set()
for r in range(1, count_r + 1):
    for item in combinations_with_replacement(wallet, r):
        if sum(item) == 100:
            all_combinations.add(item)
print(len(all_combinations))

