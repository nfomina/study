import copy


class Peekable:
    def __init__(self, iterable):
        self.copy_iterable = copy.deepcopy(iter(iterable))
        self.iterable = iter(iterable)
        self.val_origin = ''
        self.val_copy = ''

    def __iter__(self):
        return self

    def __next__(self):
        if self.val_copy == self.val_origin:
            self.val_copy = next(self.copy_iterable)
        self.val_origin = next(self.iterable)
        return self.val_origin

    def peek(self, default='abs'):
        if self.val_copy == self.val_origin:
            self.val_copy = next(self.copy_iterable, default)
        if self.val_copy == 'abs':
            raise StopIteration
        return self.val_copy or default



# TEST_1:
iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)

# TEST_2:
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

# TEST_3:
iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))

# TEST_4:
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор 1')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор 2')

# TEST_5:
from itertools import islice

iterator = Peekable([n ** 2 for n in [1, 2, 3, 4, 5]])

print(iterator.peek())
print(list(islice(iterator, 2)))

print(iterator.peek())
print(iterator.peek())

print(list(islice(iterator, 2)))
print(list(islice(iterator, 2)))

# TEST_6:
iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))

# TEST_7:
from itertools import islice

iterator = Peekable([1, 2, 3])

print(iterator.peek())
print(list(islice(iterator, 2)))
print(iterator.peek())
print(list(iterator))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')
