from itertools import count


def palindromes():
    for digits in count(1):
        first = 10 ** ((digits - 1) // 2)
        yield from [int(s + s[-(digits % 2) - 1::-1]) for s in map(str, range(first, 10 * first))]


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)

# beauty is simple
# from itertools import count
#
# def palindromes():
#     yield from (i for i in count(1) if str(i) == str(i)[::-1])
