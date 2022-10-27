import json
from zipfile import ZipFile


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False

names = []
with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    for item in info:
        if item.filename.endswith('.json'):
            with zip_file.open(item.filename) as file:
                try:
                    data = file.read().decode('utf-8')
                except:
                    data = None
                if data and is_correct_json(data):
                    players = json.loads(data)
                    if players.get('team') == 'Arsenal':
                        names.append((players.get('first_name') + ' ' + players.get('last_name')))

for name in sorted(names):
    print(name)

# short enough
# from zipfile import ZipFile
# import json
#
# with ZipFile('data.zip') as zip_file:
#     lst = []
#     for i in zip_file.namelist():
#         with zip_file.open(i) as json_file:
#             try: lst.append(json.load(json_file))
#             except: ...
#     [print(i['first_name'], i['last_name'])
#      for i in sorted(filter(lambda x: x['team'] == 'Arsenal', lst),
#                      key=lambda x: (x['first_name'], x['last_name']))]
