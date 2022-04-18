with open('data.txt') as file:
    for line in file.readlines()[::-1]:
        print(line.rstrip())