import csv

passengers = {'male': [], 'female': []}

with open('titanic.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for line in reader:
        if line[0] == '1' and float(line[3]) < 18:
            if line[2] == 'male':
                passengers['male'].append(line[1])
            else:
                passengers['female'].append(line[1])

for item in passengers['male']:
    print(item)
for item in passengers['female']:
    print(item)

# wtf
#
# import csv
#
# with open('titanic.csv', encoding='utf-8') as f:
#     passengers = [d for  s, *d, a in csv.reader(f, delimiter=';') if s == '1' and float(a) < 18]
#
# [print(name) for name, _ in sorted(passengers, key=lambda x: x[1], reverse=True)]