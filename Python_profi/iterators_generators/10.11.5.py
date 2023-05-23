from itertools import groupby


def group_anagrams(words):
    return [tuple(values) for key, values in groupby(sorted(sorted(words, key=len), key=lambda a: sorted(a)),
                                                     key=lambda a: sorted(a))]


groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
print(*groups)

groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
print(*groups)

groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
print(*groups)

# from itertools import groupby
#
# def group_anagrams(words):
#     return (tuple(i) for _, i in groupby(sorted(words, key=sorted), key=sorted))
