def hash_as_key(objects):
    new_dict = {}
    for item in objects:
        key = hash(item)
        if new_dict.get(key):
            if isinstance(new_dict[key], list):
                new_dict[key].append(item)
            else:
                old_item = new_dict[key]
                new_dict[key] = [old_item, item]
        else:
            new_dict[key] = item
    return new_dict


data = [1, 2, 3, 4, 5, 5]
print(hash_as_key(data))

data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))

data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
print(hash_as_key(data))

# smart
# def hash_as_key(objects):
#     rv = {}
#     for i in objects:
#         rv.setdefault(hash(i), []).append(i)
#     return {i: j if len(j) > 1 else j[0] for i, j in rv.items()}
