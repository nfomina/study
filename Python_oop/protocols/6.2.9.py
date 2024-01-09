class MutableString:
    def __init__(self, string=''):
        self.list_string = [i for i in str(string)]

    def __str__(self):
        return ''.join(self.list_string)

    def __repr__(self):
        return f"MutableString('{''.join(self.list_string)}')"

    def __iter__(self):
        yield from self.list_string

    def __len__(self):
        return len(self.list_string)

    def __getitem__(self, key):
        if type(key) is slice:
            return MutableString(''.join(self.list_string[key]))
        return ''.join(self.list_string[key])

    def __setitem__(self, key, value):
        self.list_string[key] = value
        new_str = ''.join(self.list_string)
        self.list_string = [i for i in new_str]

    def __delitem__(self, key):
        del self.list_string[key]

    def lower(self):
        self.list_string = [i.lower() for i in self.list_string]

    def upper(self):
        self.list_string = [i.upper() for i in self.list_string]

    def __add__(self, other):
        if isinstance(other, MutableString):
            return ''.join(self.list_string + other.list_string)


# mutablestring = MutableString('beegeek')
#
# print(*mutablestring)
# print(str(mutablestring))
# print(repr(mutablestring))
#
# mutablestring = MutableString('Beegeek')
#
# mutablestring.lower()
# print(mutablestring)
# mutablestring.upper()
# print(mutablestring)
#
# mutablestring1 = MutableString('bee')
# mutablestring2 = MutableString('geek')
#
# print(mutablestring1 + mutablestring2)
# print(mutablestring2 + mutablestring1)
#
# mutablestring = MutableString('beegeek')
#
# print(mutablestring)
# mutablestring[0] = 'B'
# mutablestring[-4] = 'G'
# print(mutablestring)
#
# # TEST_5:
# mutablestring = MutableString('beegeek')
#
# s1 = mutablestring[2:]
# s2 = mutablestring[:5]
# s3 = mutablestring[2:5:2]
#
# print(s1, type(s1))
# print(s2, type(s2))
# print(s3, type(s3))
#
# # TEST_6:
# mutablestring = MutableString('Ada Wong')
# id1 = id(mutablestring)
#
# mutablestring.upper()
# id2 = id(mutablestring)
#
# print(id1 == id2)
#
# # TEST_7:
# string = '''For a long time it was a mystery to me how something very expensive and technologically advanced could be
# so useless. And I soon realized that a computer is a stupid machine that has the ability to do incredibly smart things,
# while programmers are smart people who have a talent for doing incredibly stupid things. In short,
# they found each other.
# Bill Bryson'''
#
# mutablestring1 = MutableString(string)
# mutablestring2 = mutablestring1[20:45]
#
# print(mutablestring1 is mutablestring2)
#
# # TEST_8:
# string = '''Sometimes it's better to stay home on Monday than to spend the whole week debugging code written on Monday.
# Christopher Thompson'''
# mutablestring = MutableString(string)
#
# print(mutablestring[30], mutablestring[3], mutablestring[66], mutablestring[66], mutablestring[1], sep='')
#
# # TEST_9:
# string = '''Many of you are familiar with the virtues of being a programmer. There are only three of them,
# and of course this is: laziness, impatience and pride. Larry Wall'''
# mutablestring = MutableString(string)
#
# print(mutablestring[20])
# print(mutablestring[-30])
# print(mutablestring[:11])
# print(mutablestring[16:])
# print(mutablestring[4::10])
# print(mutablestring[::-10])
#
# # TEST_10:
# string1 = MutableString('Разбежавшись')
# string2 = MutableString('прыгну')
# string3 = MutableString('со скалы')
#
# array = [string1, string2, string3]
# print(array)
#
# # TEST_11:
# mutablestring = MutableString()
# print(repr(mutablestring))
#
# # TEST_12:
# mutablestring = MutableString('beegeek')
#
# del mutablestring[2:5]
# del mutablestring[1:5:2]
# print(mutablestring)

# TEST_13:
mutablestring = MutableString('beegeek')

mutablestring[-1] = 'ee'
print(mutablestring)

mutablestring[-2:] = 'geek'
print(mutablestring)

# TEST_14:
mutablestring = MutableString('beegeek')

del mutablestring[1:3]
print(mutablestring)