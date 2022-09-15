import csv
import operator

with open('data.csv', encoding='utf-8') as csv_file:
    domens = {}
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    for line in reader:
        name_domen = line[2].split('@')[1]
        if domens.get(name_domen):
            domens[name_domen] += 1
        else:
            domens[name_domen] = 1

domens = sorted(domens.items(), key=operator.itemgetter(0))
res = sorted(domens, key=operator.itemgetter(1))
with open('domain_usage.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['domain', 'count'])
    writer.writeheader()
    for item in res:
        writer.writerow({'domain': item[0], 'count': item[1]})

# smart
# import csv
#
# domens = dict()
#
# with open('data.csv', encoding='utf-8') as f:
#     for *n,d in csv.reader(f):
#         key = d.split('@')[-1]
#         domens[key] = domens.get(key, 0) + 1
#
# del domens['email']
#
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['domain','count'])
#     for row in sorted(domens.items(), key=lambda x: (x[1], x[0])):
#         writer.writerow(row)