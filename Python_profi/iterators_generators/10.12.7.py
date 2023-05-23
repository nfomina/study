from itertools import product


def numbers_gen(alphabet, r):
    res = []
    for item in product(alphabet, repeat=r):
        res.append(''.join(item))
    return res


alphabet = [*map(str, range(10)), 'A', 'B', 'C', 'D', 'E', 'F'][0:int(input())]

r = int(input())
print(' '.join(numbers_gen(alphabet, r)))

#  without bicycle
# import itertools as it
# from string import ascii_uppercase, digits
#
# n, m = int(input()), int(input())
# symbols = (digits + ascii_uppercase)[:n]
#
# print(*map("".join, it.product(symbols, repeat=m)))
