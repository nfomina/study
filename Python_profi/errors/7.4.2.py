import re


def get_id(names, name):
    if not type(name) is str:
        raise TypeError('Имя не является строкой')
    else:
        if bool(re.fullmatch('[A-Z]{1}[a-z]{1,}', name)):
            names.append(name)
    if name not in names:
        raise ValueError('Имя не является корректным')
    else:
        return len(names)


names = ['Timur', 'Anri', 'Dima', 'Roma', 'Gvido', 'Rosy', 'Soslan', 'Natasha', 'Arthur']
name = 'Arthur'

print(get_id(names, name))
