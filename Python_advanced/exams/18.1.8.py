
flag = 0
with open(input()) as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith('def ') and i > 0:
            if lines[i-1].startswith('#') is False:
                print(line.split('(')[0][4:])
                flag = 1
        elif line.startswith('def ') and i == 0:
            print(line.split('(')[0][4:])
            flag = 1
if flag == 0:
    print('Best Programming Team')