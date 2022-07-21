
def spell(*args):
    res = {}
    for arg in args:
        if arg[0].lower() not in res:
            res[arg[0].lower()] = len(arg)
        elif len(arg) > res[arg[0].lower()]:
            res[arg[0].lower()] = len(arg)
    return res


words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))

print(spell())

words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
print(spell(*words))

words = ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
print(spell(*words))

words = ['a']
print(spell(*words))

words = ['a', 'ab', 'abc', 'abcd', 'ба', 'аб', 'абвгдеЁёёЁЁжбБбБввВ', 'ёёё', 'Ёаaа']
print(spell(*words))

# shortly
# def spell(*args):
#     result = {}
#     for word in args:
#         if result.get(word[0].lower(), 0) < len(word):
#             result[word[0].lower()] = len(word)
#     return result