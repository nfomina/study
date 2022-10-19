import json

with open('data1.json') as f:
    data1 = json.loads(f.read())

with open('data2.json') as f:
    data2 = json.loads(f.read())

merged_dict = {**data1, **data2}

with open('data_merge.json', 'w') as f:
    f.write(json.dumps(merged_dict))


# one line
# import json
#
# with open('data1.json', encoding='Utf-8') as file1, \
#      open('data2.json', encoding='utf-8') as file2, \
#      open('data_merge.json', 'w') as outer:
#     data1, data2=json.load(file1), json.load(file2)
#     json.dump(data1|data2, outer)
