from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


for item, val in groupby(sorted(persons, key=lambda a: a[2]), lambda a: a[2]):
    print(f'{item}:', ', '.join([item.name for item in sorted(val, key=lambda a: a[0])]))
# 158: Ariana, Eva
# 172: Mark
# ...
