class AttrsIterator:
    def __init__(self, obj):
        self.data = obj.__dict__
        self.keys = iter(obj.__dict__)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        return key, self.data[key]


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)


# TEST_2:
class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
user.profession = 'singer'
user.height = 160

attrsiterator = AttrsIterator(user)

print(*attrsiterator, sep='\n')


# TEST_3:
class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))


# TEST_4:
class Kish:
    def __init__(self, song, year):
        self.song = song
        self.year = year


forester = Kish('лесник', 1997)
attrs_iterator = AttrsIterator(forester)

next(attrs_iterator)
next(attrs_iterator)

try:
    next(attrs_iterator)
except StopIteration:
    print('Атрибуты закончились')
