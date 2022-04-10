n = int(input())

db = {}
for _ in range(n):
    customer, product, count = input().split()
    if db.get(customer):
        flag = 0
        for i, item in enumerate(db[customer]):
            if item['product'] == product:
                db[customer][i]['count'] += int(count)
                flag = 1
        if flag == 0:
            db[customer].extend([{'product': product, 'count': int(count)}])
    else:
        db[customer] = [{'product': product, 'count': int(count)}]

for key in sorted(db.keys()):
    print(f'{key}:')
    sorted_product = (sorted(db[key], key=lambda d: d['product']))
    for item in sorted_product:
        print(item['product'], item['count'])

