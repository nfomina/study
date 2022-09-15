import csv
from operator import itemgetter

n = int(input())

with open('deniro.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    rows = [[row[0], int(row[1]), int(row[2])] for row in reader if row]
    res = sorted(rows, key=itemgetter(n-1))
    for item in res:
        print(','.join(str(x) for x in item))