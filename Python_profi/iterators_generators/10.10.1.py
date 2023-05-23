from itertools import chain


def sum_of_digits(iterable):
    res = 0
    all_item = chain(iterable)
    for item in all_item:
        for i in str(item):
            res += int(i)
    return res


print(sum_of_digits([13, 20, 41, 2, 2, 5]))
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(sum_of_digits([123456789]))

# smart
# from itertools import chain
#
# def sum_of_digits(iterable):
#     tmp = map(str, iterable)
#     return sum(map(int, chain.from_iterable(tmp)))
