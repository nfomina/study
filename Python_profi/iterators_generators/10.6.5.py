def interleave(*items):
    for symbol in (item[i] for i in range(len(items[0])) for item in items):
        yield symbol


print(*interleave('bee', '123'))

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))

# from author
# def interleave(*args):
#     for iterable in zip(*args):
#         yield from iterable
