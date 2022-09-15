import csv

with open('salary_data.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    companies = {}
    next(reader)
    for line in reader:
        name, salary = line[0], line[1]
        if companies.get(name):
            companies[name].append(int(salary))
        else:
            companies[name] = [int(salary)]

mean_companies = {}
for key in companies:
    mean_companies[sum(companies[key])/len(companies[key])] = key
for key in sorted(mean_companies):
    print(mean_companies[key])


# smart
# import csv
# d = {}
# with open('salary_data.csv', encoding='utf-8') as file:
#     rows = list(csv.reader(file, delimiter=';'))
#     for key, value in rows[1:]:
#         d[key] = d.get(key, []) + [int(value)]
#
#     d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
#     print(*d_sort, sep='\n')