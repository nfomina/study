from itertools import count


def tabulate(func):
    counter = count(1)
    for item in counter:
        yield func(item)


func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))

func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))

# short
# from itertools import count
#
# def tabulate(func):
#     return map(func, count(1))
