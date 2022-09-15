import csv

def condense_csv(filename, id_name):
    res = {}
    with open(filename, encoding='UTF-8') as f:
        rows = csv.reader(f)
        headers = []
        for item in rows:
            if res.get(item[0], []):
                res[item[0]].append((item[1], item[2]))
            else:
                res[item[0]] = [(item[1], item[2])]
            if item[1] not in headers:
                headers.append(item[1])
    with open('condensed.csv', 'w', encoding='UTF-8', newline='') as f:
        header = [id_name]
        header.extend(list(headers))
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for item in res:
            row = {}
            row[header[0]] = item
            for head in header[1:]:
                for i in res[item]:
                    if i[0] == head:
                        row[head] = i[1]
            writer.writerow(row)


