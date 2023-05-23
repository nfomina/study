from itertools import pairwise


def max_pair(iterable):
    max = 0
    for item in pairwise(iterable):
        if sum(item) > max:
            max = sum(item)
    return max


print(max_pair([1, 8, 2, 4, 3]))
iterator = iter([1, 2, 3, 4, 5])
print(max_pair(iterator))
iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
print(max_pair(iterator))

# def max_pair(iterable):
#     return max(map(sum, pairwise(iterable)))
