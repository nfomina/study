from collections import Counter
import json
import csv


with open('prices.json') as f:
    prices = json.loads(f.read())

vegetables = Counter()
for i in range(1, 5):
    with open(f'quarter{i}.csv') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for line in reader:
            vegetables.update({line[0]: sum([int(i) for i in line[1:]])})
sum = 0
for veg, count in vegetables.items():
    sum += prices.get(veg) * count

print(sum)

