import re

infected = []
for i in range(int(input())):
    string = input()
    result = re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', string)
    if result:
        infected.append(i+1)

if infected:
    print(*infected)