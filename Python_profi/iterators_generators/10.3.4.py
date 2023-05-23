from random import choice


def random_numbers(left, right):
    return iter(lambda: choice(list(range(left, right+1))), 'a')



iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))

iterator = random_numbers(1, 10)

print(next(iterator))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

# the best
# import random
#
# def random_numbers(start: int, end: int) -> int:
#     return iter(lambda: random.randint(start, end), None)
