from collections import Counter


def scrabble(symbols, word):
    res = Counter(symbols.lower())
    res.subtract(word.lower())
    for item in res.values():
        if item < 0:
            return False
    return True


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
print(scrabble('begk', 'beegeek'))
print(scrabble('beegeek', 'beegeek'))

# best of the best
# from collections import Counter
#
# def scrabble(symbols, word):
#     return Counter(word.lower()) <= Counter(symbols.lower())