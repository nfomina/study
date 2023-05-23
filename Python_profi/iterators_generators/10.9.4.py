from itertools import islice


def take(iterable, n):
    return islice(iterable, 0, n)


print(*take(range(10), 5))

iterator = iter('beegeek')

print(*take(iterator, 22))

iterator = iter('beegeek')

print(*take(iterator, 1))

# it's genius
# from itertools import islice as take
