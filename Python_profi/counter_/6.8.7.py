from collections import Counter
import csv

with open('name_log.csv') as file:
    names = csv.reader(file)
    next(names)
    res = Counter([item[1] for item in names])

for email in sorted(res):
    print(f'{email}: {res[email]}')
