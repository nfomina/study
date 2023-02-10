from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()
    for item in chainmap.maps:
        if item.get(key):
            return item.get(key)


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))

#  so smart
# def get_value(chainmap, key, from_left=True):
#     if not from_left:
#         chainmap.maps.reverse()
#     return chainmap.get(key)
