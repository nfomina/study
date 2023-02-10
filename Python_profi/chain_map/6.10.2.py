from collections import ChainMap


def deep_update(chainmap, key, value):
    if chainmap.get(key) is None:
        chainmap.maps[0][key] = value
    else:
        for item in chainmap.maps:
            if item.get(key):
                item.update({key: value})


chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)

# short

# def deep_update(chainmap, key, value):
#     if key in chainmap:
#         [dct.update({key: value}) for dct in chainmap.maps if key in dct]
#     else:
#         chainmap[key] = value
