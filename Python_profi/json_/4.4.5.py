import json

uniq_keys = set()

with open('people.json') as f:
    people = json.loads(f.read())

for item in people:
    for key in item.keys():
        if key not in uniq_keys:
            uniq_keys.add(key)

for item in people:
    for key in uniq_keys:
        if item.get(key) is None:
            item[key] = None

with open('updated_people.json', 'w') as f:
    f.write(json.dumps(people))
