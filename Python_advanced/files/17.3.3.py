with open('lines.txt') as file:
    lines = file.readlines()
    lines = sorted(lines, key = lambda x: len(x), reverse = True)
max_len = len(lines[0])
for line in lines:
    if len(line) == max_len:
        print(line.rstrip())
    else:
        break