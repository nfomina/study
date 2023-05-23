def around(iterable):
    prev_1 = None
    prev_2 = None
    if iterable:
        for item in iterable:
            if prev_1 or prev_1 == 0 or prev_2 or prev_2 == 0:
                res = prev_1, prev_2, item
                prev_1 = prev_2
                prev_2 = item
                yield res
            else:
                prev_1 = prev_2
                prev_2 = item
    if prev_1 or prev_2:
        yield prev_1, prev_2, None


# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

# TEST_2:
iterator = iter('hey')

print(*around(iterator))

# TEST_3:
iterator = around(iter('beegeek'))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_4:
data = map(abs, range(-100, 100))

print(*around(data))

# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*around(data))

# TEST_6:
data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))

# TEST_7:
data = map(str.upper, 'yt')

print(*around(data))

# TEST_8:
data = map(str.upper, 'ytu')

print(*around(data))

# TEST_9:
data = ['bee', 'geek', 'stepik', 'python']

print(*around(data))

# TEST_10:
print(list(around([])))

# beauty
# def around(iterable):
#     it = iter(iterable)
#     a = None
#     try:
#         b = next(it)
#         for i in it:
#             yield (a, b, i)
#             a, b = b, i
#         yield (a, b, None)
#     except StopIteration:
#         pass
