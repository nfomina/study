import csv

with open('student_counts.csv', encoding='UTF-8') as f:
    file_data = csv.reader(f)
    headers = next(file_data)
    res = [dict(zip(headers, i)) for i in file_data]

with open('sorted_student_counts.csv', 'w', encoding='UTF-8', newline='') as f:
    w = csv.writer(f)
    header = [headers[0]] + sorted(headers[1:], key=lambda a: (int(a.split('-')[0]), a.split('-')[1]))
    w.writerow(header)
    for item in res:
        row = []
        year = item.pop('year')
        row.append(year)
        for i in sorted(item, key=lambda a: (int(a.split('-')[0]), a.split('-')[1])):
            row.append(item[i])
        w.writerow(row)

# smart
# import csv
#
# def key_func(grade):
#     number, letter = grade.split('-')
#     return int(number), letter
#
# with open('student_counts.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
#     rows = list(reader)
#
# with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(rows)
