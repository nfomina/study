import csv

def csv_columns(filename):
    with open(filename, encoding='utf-8') as csv_file:
        res = {}
        reader = csv.reader(csv_file)
        headers = next(reader, None)
        column = {}
        for h in headers:
            column[h] = []
        for row in reader:
            for h, v in zip(headers, row):
                column[h].append(v)
        return column


print(csv_columns('deniro.csv'))

# simple way

# def csv_columns(filename):
#
#     with open(filename, encoding="utf-8") as file_in:
#         rows = list(csv.reader(file_in))
#         return {key: value for key, *value in zip(*rows)}