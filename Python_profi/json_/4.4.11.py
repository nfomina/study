import json

with open("food_services.json", encoding='UTF-8') as f:
    foods = json.loads(f.read())
    rayon = {}
    net = {}
    for item in foods:
        if item['District'] in rayon:
            rayon[item['District']] += 1
        else:
            rayon[item['District']] = 1
        if item['OperatingCompany'] in net:
            net[item['OperatingCompany']] += 1
        else:
            net[item['OperatingCompany']] = 1

res_rayon = sorted(rayon.items(), key=lambda x: x[1], reverse=True)[0]
res_net = sorted(net.items(), key=lambda x: x[1], reverse=True)[1]
print(f'{res_rayon[0]}: {res_rayon[1]}')
print(f'{res_net[0]}: {res_net[1]}')


# short
# import json
#
# with open("food_services.json", "r", encoding="utf-8") as f:
#     cafes = list(json.load(f))
#     dst = [i["District"] for i in cafes]
#     cmp = [i["OperatingCompany"] for i in cafes if i["OperatingCompany"]]
#     mfd, mfc = max(set(dst), key=dst.count), max(set(cmp), key=cmp.count)
#     print(f"{mfd}: {dst.count(mfd)}\n{mfc}: {cmp.count(mfc)}")
