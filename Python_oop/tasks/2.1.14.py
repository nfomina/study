def pluck(data, path, default=None):
    path = path.split('.')
    while True:
        if len(path) >= 2:
            data = data.get(path[0])
            if dict:
                path = path[1:]
            else:
                return default
        else:
            try:
                return data[path[0]]
            except KeyError:
                return default


d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'b'))

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'a.b'))

d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))

# best practise

# def pluck(data, path, default=None):
#     for key in path.split('.'):
#         if isinstance(data, dict) and key in data:
#             data = data[key]
#         else:
#             return default
#     return data
