from collections import Counter

fruits = Counter([item.lower() for item in input().split()])
min_value = min(fruits.items(), key=lambda i: i[1])[1]
res = []
for item in sorted(fruits.items(), key=lambda i: i[1]):
    if item[1] == min_value:
        res.append(item[0])

print(', '.join(sorted(res)))


# counter=Counter(c.lower() for c in input().split()).most_common()
# min_value=min(x[1] for x in counter)
# result=filter(lambda para: para[1]== min_value,counter)
# print(*sorted(c[0] for c in result), sep=', ')
