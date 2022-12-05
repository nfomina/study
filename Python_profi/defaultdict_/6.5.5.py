from collections import defaultdict


def flip_dict(dict_of_lists):
    result = defaultdict(list)
    for key, item in dict_of_lists.items():
        for element in item:
            result[element].append(key)
    return result

print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')
