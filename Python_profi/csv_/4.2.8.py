import csv

wifi = dict()

with open('wifi.csv', encoding='utf-8') as f:
    rows = list(csv.reader(f, delimiter=';'))
    for adm_area, district, location, number_of_access_points in rows[1:]:
        wifi[district] = wifi.get(district, 0) + int(number_of_access_points)

for row in sorted(wifi.items(), key=lambda x: (-x[1], x[0])):
    print(f'{row[0]}: {row[1]}')
