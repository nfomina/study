with open('numbers.txt') as file:
    line = file.readline()
    while line != '':
        print(sum([int(i) for i in line.split()]))
        line = file.readline()