from collections import ChainMap


def get_all_values(chainmap, key):
    key_set = set()
    for item in chainmap.maps:
        if item.get(key):
            key_set.add(item[key])
    return key_set


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)
