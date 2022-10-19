import json

with open('data.json') as f:
    data = json.loads(f.read())

res = []

mapping = {str: lambda a: a + '!',
           int: lambda a: a + 1,
           bool: lambda a: not a,
           list: lambda a: a * 2,
           }
for item in data:
    if item is not None:
        if type(item) == dict:
            item['newkey'] = None
        else:
            item = mapping.get(type(item))(item)
        res.append(item)

with open('updated_data.json', 'w') as f:
    f.write(json.dumps(res))


# short

# import json
#
# opers = {'str': lambda x: x + '!',
#          'int': lambda x: x + 1,
#          'float': lambda x: x + 1,
#          'bool': lambda x: not x,
#          'list': lambda x: x * 2,
#          'dict': lambda x: x | {'newkey': None}}
#
# with open('data.json', encoding='utf8') as fi, open('updated_data.json', 'w', encoding='utf8') as fo:
# 	json.dump([opers[type(i).__name__](i) for i in json.load(fi) if type(i).__name__ in opers], fo, indent=3)