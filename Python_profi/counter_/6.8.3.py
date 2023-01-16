from collections import Counter

counter = Counter(c.lower() for c in input().split()).most_common()
max_value = max(x[1] for x in counter)
result = filter(lambda para: para[1] == max_value, counter)
print(sorted(c[0] for c in result)[-1])


# short enough
# c = Counter(input().lower().split())
# print(max(c, key=lambda x: (c[x], x)))