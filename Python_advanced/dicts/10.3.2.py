dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
dict1.update(dict2)
result = dict1

print(result)

# short
# result = dict1.copy()
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value