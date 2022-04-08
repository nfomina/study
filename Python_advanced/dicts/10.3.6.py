s = input().translate(str.maketrans('', '', '.,!?:;-')).split()
result = {}
for item in s:
    result[item.lower()] = result.get(item.lower(), 0) + 1

min_val = min(result.values())
res = [k for k, v in result.items() if v==min_val]

print(min(res))

# easy way
# d = {}
# for w in input().split():
#     w = w.strip('.,!?:;-').lower()
#     d[w] = d.get(w, 0) + 1
# print(min(d.items(), key=lambda x: (x[1], x[0]))[0])