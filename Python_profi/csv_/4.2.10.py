import csv

nicknames = {}

with open('name_log.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for line in reader:
        if nicknames.get(line[1]):
            if line[2] > nicknames[line[1]][1]:
                nicknames[line[1]] = [line[0], line[2]]
        else:
            nicknames[line[1]] = [line[0],line[2]]

with open('new_name_log.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['username', 'email', 'dtime'])
    writer.writeheader()
    for item in (sorted(nicknames)):
        writer.writerow({'username': nicknames[item][0], 'email': item, 'dtime': nicknames[item][1]})

# short
# import csv
# from datetime import datetime
#
# with open('name_log.csv', encoding='UTF-8') as f:
# 	header, *rows = csv.reader(f)
#
# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
#
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))