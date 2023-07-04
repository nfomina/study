def intersperse(iterable, delimiter):
    new_list = []
    for item in iterable:
        new_list.append(item)
        new_list.append(delimiter)
    if new_list:
        return iter(new_list[:-1])
    else:
        return []


print(*intersperse([1, 2, 3], 0))
inter = intersperse('beegeek', '!')
print(next(inter))
print(next(inter))
print(*inter)
print(*intersperse('A', '...'))

# good boy
# def intersperse(iterable, delimiter):
#     first = True
#     for item in iterable:
#         if not first:
#             yield delimiter
#         first = False
#         yield item
