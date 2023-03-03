def dict_travel(nested_dicts, path=''):
    for k, v in sorted(nested_dicts.items()):
        if isinstance(v, dict):
            dict_travel(v, f'{path}{k}.')
        else:
            print(f'{path}{k}: {v}')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
dict_travel(data)
# a: 1
# b.a: 10
# b.b: 20
# b.c: 30

data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
dict_travel(data)
# a: 100
# b.a: 10
# b.b: 20
# b.c: 30
# d: 1

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
dict_travel(data)
# b.a: 10
# b.b.d: 40
# b.b.e: 50
# b.c: 30
