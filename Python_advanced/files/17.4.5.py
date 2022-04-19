colors = []
goats_dict = {}

with open('goats.txt') as file:
    line = file.readline()
    line = file.readline()
    while line != 'GOATS\n':
        colors.append(line[:-1])
        line = file.readline()
    line = file.readline()
    while line != '':
        goats_dict[line[:-1]] = goats_dict.get(line[:-1], 0) + 1
        line = file.readline()

count_goats = sum(goats_dict.values())

res = []
for key, value in goats_dict.items():
    if value >= count_goats*0.07:
        res.append(key)

with open('answer.txt', 'w') as file_out:
    print(*sorted(res), sep = '\n', file=file_out)

# really cool
# with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
#     cont = f1.read().split('\n')
#     colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
#     print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)