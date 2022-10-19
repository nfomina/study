import json

with open('countries.json') as f:
    countries = json.loads(f.read())

religions = {}
for country in countries:
    if religions.get(country['religion']):
        religions[country['religion']].append(country['country'])
    else:
        religions[country['religion']] = [country['country']]


with open('religion.json', 'w') as f:
    f.write(json.dumps(religions))


# just easy
# import json
#
# with open("countries.json") as file_in, open("religion.json", "w") as file_out:
#
#     d = {}
#     datas = json.load(file_in)
#     for data in datas:
#         d[data['religion']] = d.get(data['religion'], []) + [data['country']]
#
#     json.dump(d, file_out)
