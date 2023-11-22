class AnyClass:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)
        self.args = args
        self.kwargs = kwargs
        res = []
        for x, y in self.kwargs.items():
            if type(y) != str:
                res.append(''.join(map(str, [x, '=', y])))
            else:
                res.append(''.join(map(str, [x, "='", y, "'"])))
        self.res = res

    def __str__(self):
        return f"AnyClass: {', '.join(self.res)}"

    def __repr__(self):
        return f"AnyClass({', '.join(self.res)})"


any = AnyClass()

print(str(any))
print(repr(any))

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))

# AnyClass: attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None
# AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

# TEST_6:
attrs = {
    'name': 'Guido van Rossum',
    'birth_date': '31.01.1956',
    'age': 67,
    'career': 'python guru'
}
obj = AnyClass(**attrs)
print(obj.name)
print(obj.birth_date)
print(obj.age)
print(obj.career)

# best practices
# class AnyClass:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __str__(self):
#         return f'AnyClass: {", ".join(self._attrs())}'
#
#     def __repr__(self):
#         return f'AnyClass({", ".join(self._attrs())})'
#
#     def _attrs(self):
#         return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]
