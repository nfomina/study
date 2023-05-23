from itertools import tee, chain


def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))


print(*ncycles([1, 2, 3, 4], 3))
iterator = iter('bee')
print(*ncycles(iterator, 4))
iterator = iter([1])
print(*ncycles(iterator, 10))
