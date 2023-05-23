from itertools import repeat


def roundrobin(*args):
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat('')
                value = ''
            values.append(value)
        for item in values:
            if item or item == 0 or item is None:
                yield item


# TEST_1:
print(*roundrobin('abc', 'd', 'ef'))

# TEST_2:
numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))

# TEST_3:
print(list(roundrobin()))

# TEST_4:
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = range(5)
letters = iter('beegeek')

print(*roundrobin(numbers1, numbers2, letters))

# TEST_5:
letters = iter('stepik')

print(*roundrobin(letters))

# TEST_6:
numbers = roundrobin(map(abs, range(-10, 10)))

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# TEST_7:
numbers1 = map(abs, range(-10, 10))
numbers2 = filter(None, range(-10, 10))
numbers3 = map(abs, range(-5, 5))
numbers4 = filter(None, range(-5, 5))
numbers5 = map(abs, range(-1, 1))
numbers6 = filter(None, range(-1, 1))

print(*roundrobin(numbers1, numbers2, numbers3, numbers4, numbers5, numbers6))

# TEST_8:
print(list(roundrobin([], [], [], [])))

# TEST_9:
numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))

# teacher's
# from itertools import cycle
#
# def take(iterable, n):
#     for elem, _ in zip(iterable, range(n)):
#         yield elem
#
# def roundrobin(*iterables):
#     non_empty = len(iterables)
#     iterables = cycle(map(iter, iterables))
#     while non_empty:
#         try:
#             for it in iterables:
#                 yield next(it)
#         except StopIteration:
#             non_empty -= 1
#             iterables = cycle(take(iterables, non_empty))
