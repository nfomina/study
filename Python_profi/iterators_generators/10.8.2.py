from itertools import accumulate
import operator


def factorials(n):
    yield from accumulate(range(1, n+1), operator.mul)


numbers = factorials(6)

print(*numbers)

numbers = factorials(2)

print(next(numbers))
print(next(numbers))
