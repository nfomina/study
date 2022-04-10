def merge(values):      # values - это список словарей
    result = {}
    for item in values:
        for new_key in item.keys():
            if new_key in result:
                result[new_key].append(item[new_key])
            else:
                result[new_key] = [item[new_key]]
    for key, value in result.items():
        result[key] = set(value)
    return result

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)
