from collections import Counter

print(Counter([item.lower() for item in input().split()]).most_common(1)[0][0])

# perfect
# print(Counter(input().lower().split()).most_common()[0][0])