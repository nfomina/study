def zip_longest(*lists, fill=None):
    len_max = len(max(lists, key=len))
    new_lists = []
    for item in lists:
        while len(item) < len_max:
            item.append(fill)
        new_lists.append(item)
    return [c for c in zip(*new_lists)]


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))

# smart
# def zip_longest(*args, fill=None):
#     max_len = max(map(len, args))
#     lst = [i + [fill] * (max_len - len(i)) for i in args]
#     return list(zip(*lst))
