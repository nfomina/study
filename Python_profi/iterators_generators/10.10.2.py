from itertools import pairwise


def is_rising(iterable):
    for item in pairwise(iterable):
        if item[0] >= item[1]:
            return False
    return True


print(is_rising([1, 2, 3, 4, 5]))
iterator = iter([1, 1, 1, 2, 3, 4])
print(is_rising(iterator))
iterator = iter(list(range(100, 200)))
print(is_rising(iterator))


# short
# def is_rising(iterable):
#     return all(a < b for a, b in pairwise(iterable))
