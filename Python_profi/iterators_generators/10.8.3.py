from itertools import cycle
import string


def alnum_sequence():
    res = zip(cycle(range(1, 27)), cycle(string.ascii_uppercase))
    for item in res:
        yield item[0]
        yield item[1]


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))

# a little bit beauty
# def alnum_sequence():
#     for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
#         yield from item
