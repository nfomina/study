from itertools import groupby

words = input().split()

for item, val in groupby(sorted(words, key=lambda a: len(a)), key=lambda a: len(a)):
    print(f'{item} ->', ', '.join(sorted(val)))
