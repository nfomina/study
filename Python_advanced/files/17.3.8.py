
with open('population.txt') as file:
    line = file.readline()
    while line != '':
        country, population = line.split('\t')
        if country.startswith('G') and int(population) >= 500000:
            print(country)
        line = file.readline()


# beauty
# with open('population.txt') as f:
#     for line in f:
#         n, p = line.split('\t')
#         if n.startswith('G') and int(p) > 500000:
#             print(n)