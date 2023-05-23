from itertools import count


def first_largest(iterable, number):
    counter = count()
    for item in iterable:
        if item > number:
            return next(counter)
        else:
            next(counter)
    return -1


numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))

iterator = iter([18, 21, 14, 72, 73, 18, 20])

print(first_largest(iterator, 10))

# cheat
# from itertools import compress, count
#
# first_largest = lambda it, n: next(compress(count(), (i>n for i in it)), -1)
