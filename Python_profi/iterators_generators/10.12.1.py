from itertools import permutations


for item in sorted(set(permutations(input()))):
    print(''.join(item))
