from itertools import combinations


wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

all_combinations = set()
for r in range(1, len(wallet)):
    for item in combinations(wallet, r):
        if sum(item) == 100:
            all_combinations.add(item)
print(len(all_combinations))
