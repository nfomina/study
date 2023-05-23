def filterfalse(predicate, iterable):
    if not predicate:
        predicate = bool
    return filter(lambda x: predicate(x) is False, iterable)


objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))

numbers = (1, 2, 3, 4, 5)

print(*filterfalse(lambda x: x % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5]

print(*filterfalse(lambda x: x >= 3, numbers))
