import json
import csv

with open("students.json", encoding='UTF-8') as file_in, open("data.csv", "w", encoding='UTF-8') as file_out:
    students = json.loads(file_in.read())
    data = []
    for student in students:
        if student['age'] >= 18 and student['progress'] >= 75:
            data.append([student['name'], student['phone']])
    w = csv.writer(file_out)
    w.writerow(['name', 'phone'])
    for item in sorted(data, key=lambda x: x[0]):
        w.writerow(item)


# smart
# import json, csv
#
# with open('students.json', encoding='UTF-8') as f:
#     data = sorted([d for d in json.load(f) if d['progress'] > 74 and d['age'] > 17],
#                   key=lambda x: x['name'])
#
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=['name', 'phone'], extrasaction='ignore')
#     writer.writeheader()
#     writer.writerows(data)