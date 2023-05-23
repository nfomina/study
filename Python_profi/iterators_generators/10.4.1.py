class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))

bee = Repeater('bee')

print(next(bee))
