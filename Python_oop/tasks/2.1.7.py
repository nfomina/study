def quantify(iterable, predicate):
    if predicate:
        return sum([predicate(element) for element in iterable])
    else:
        return sum([bool(element) for element in iterable])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x > 1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x % 2 == 0))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x < 0))

iterable = iter(['', 1, 0, (), [[]], [], {1: 2}])

print(quantify(iterable, None))