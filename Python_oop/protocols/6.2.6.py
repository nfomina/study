class AttrDict:
    def __init__(self, data={}):
        self.items = dict(data) or {}

    def __getitem__(self, item):
        return self.items[item]

    def __getattr__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __iter__(self):
        yield from self.items

    def __len__(self):
        return len(self.items)


attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})

print(attrdict['name'])
print(attrdict.father)
print(len(attrdict))

attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)

attrdict = AttrDict()

attrdict['school_name'] = 'BEEGEEK'
print(attrdict['school_name'])
print(attrdict.school_name)

# TEST_4:
d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')

# TEST_5:
d = dict.fromkeys(range(100), None)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)
