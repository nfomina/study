def pairwise(iterable):
    prev = None
    if iterable:
        for item in iterable:
            if prev or prev == 0:
                res = prev, item
                prev = item
                yield res
            else:
                prev = item
    if prev:
        yield prev, None



numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

# TEST_2:
iterator = iter('stepik')

print(*pairwise(iterator))

# TEST_3:
data = map(abs, range(-100, 100))

print(*pairwise(data))

# TEST_4:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*pairwise(data))

# TEST_5:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*pairwise(data))

# TEST_6:
iterator = pairwise('A')

print(next(iterator))

# TEST_7:
data = ['bee', 'geek', 'stepik', 'python']

print(*pairwise(data))

# TEST_8:
print(list(pairwise([])))
