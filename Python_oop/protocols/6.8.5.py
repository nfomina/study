from random import randint


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache

    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.cache and self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        num = randint(self.start, self.end)
        if self.cache:
            obj.__dict__[self._attr] = num
        return num

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])

class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])

class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)

class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)
