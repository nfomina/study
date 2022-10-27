import json
import csv

with open("playgrounds.csv", encoding='UTF-8') as file_in, open("addresses.json", "w", encoding='UTF-8') as file_out:
    file_data = csv.reader(file_in, delimiter=';')
    headers = next(file_data)
    playgrounds = [dict(zip(headers, i)) for i in file_data]

    res = {}
    for play in playgrounds:
        if play['AdmArea'] not in res:
            res[play['AdmArea']] = {}

        if play['District'] in res[play['AdmArea']]:
            res[play['AdmArea']][play['District']].append(play['Address'])
        else:
            res[play['AdmArea']][play['District']] = [play['Address']]
    json.dump(res, file_out)


# short
# import csv
# import json
#
# with open('playgrounds.csv', encoding='utf8') as fi, open('addresses.json', 'w') as fo:
#     _, *playgrounds = csv.reader(fi, delimiter=';')
#     d = {}
#     [d.setdefault(i[1], {}).setdefault(i[2], []).append(i[3]) for i in playgrounds]
#     json.dump(d, fo, indent=3, ensure_ascii=False)