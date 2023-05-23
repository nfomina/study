def with_previous(iterable):
    previous = None
    for item in iterable:
        yield item, previous
        previous = item


numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))

iterator = iter('stepik')

print(*with_previous(iterator))

# one line generator
# def with_previous(iterable):
#     prev = None
#     return ((i, prev, prev := i)[:-1] for i in iterable)
