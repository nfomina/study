def read_csv():
    result = []
    with open('data.csv') as file:
        names = file.readline()[:-1].split(',')
        res_dict = dict.fromkeys(names)
        line = file.readline()
        while line != '':
            line = line[:-1]
            items = line.split(',')
            new_dict = {}
            for i, key in enumerate(res_dict):
                new_dict[key] = items[i]
            result.append(new_dict.copy())
            line = file.readline()
    return result
