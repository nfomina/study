def unique(iterable):
    new_dict = {}
    for item in iterable:
        if new_dict.get(item) is None:
            new_dict[item] = ''
            yield item


numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))

iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))

# smart
# def unique(iterable):
#     res = ({i:1 for i in iterable})
#     yield from res
