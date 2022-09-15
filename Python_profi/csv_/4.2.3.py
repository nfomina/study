import csv

with open('sales.csv', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=';')
    next(rows)
    for line in rows:
        if int(line[2]) < int(line[1]):
            print(line[0])