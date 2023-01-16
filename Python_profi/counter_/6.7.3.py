from collections import Counter

for item in sorted(Counter(input().split(',')).items()):
    print(f'{item[0]}: {item[1]}')
