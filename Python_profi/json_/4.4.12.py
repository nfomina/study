import json

with open("food_services.json", encoding='UTF-8') as f:
    foods = json.loads(f.read())
    res = {}
    for food in foods:
        if (food['TypeObject'] in res and food['SeatsCount'] > res[food['TypeObject']]['SeatsCount']) or \
                food['TypeObject'] not in res:
            res[food['TypeObject']] = {'Name': food['Name'], 'SeatsCount': food['SeatsCount']}

for item in sorted(res):
    print(f'{item}: {res[item]["Name"]}, {res[item]["SeatsCount"]}')


# hard to understand
# import json
# with open('food_services.json',encoding='utf-8') as f:
#     d={}
#     [d.setdefault(i['TypeObject'],[]).append([i['Name'],i['SeatsCount']]) for i in json.load(f)]
#     [print(f'{i[0]}: {i[1]}, {i[2]}') for i in  sorted([[i]+max(d[i],key=lambda x: int(x[1])) for i in d])]