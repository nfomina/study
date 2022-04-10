def build_query_string(params):
    query = ''
    keys = sorted(params.keys())
    for key in keys:
        if query:
            query += f'&{key}={params[key]}'
        else:
            query += f'{key}={params[key]}'
    return query

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))