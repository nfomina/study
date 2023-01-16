from collections import Counter

counter = Counter(len(c) for c in input().split())
for item in sorted(counter.items(), key=lambda x: x[1]):
    print(f'Слов длины {item[0]}: {item[1]}')
