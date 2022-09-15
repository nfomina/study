import csv

with open('prices.csv', encoding='UTF-8') as f:
    file_data = csv.reader(f, delimiter=';')
    headers = next(file_data)
    res = [dict(zip(headers, i)) for i in file_data]

    best_food = []
    for item in res:
        shop = item.pop('Магазин')
        min_price = min(item.values(), key=lambda x: int(x))
        foods = [k for k,v in item.items() if v == min_price]
        best_food.append([min_price, foods, shop])
best = (sorted(best_food, key=lambda a: (int(a[0]), sorted(a[1]), a[2])))
print(f'{sorted(best[0][1])[0]}: {best[0][2]}')

# cheat
# import csv
#
# with open('prices.csv', encoding='UTF-8') as f:
#     h, *rows = csv.reader(f, delimiter=';')
#
# goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
# cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))
#
# print(f'{cheapest[1]}: {cheapest[0]}')
