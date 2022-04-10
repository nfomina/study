mapping = {'execute': 'X',
           'read': 'R',
           'write': 'W'}

n = int(input())

files = {}
for _ in range(n):
    line = input().split()
    files[line[0]] = line[1:]

m = int(input())

for _ in range(m):
    operator, file = input().split()
    if mapping.get(operator) in files[file]:
        print("OK")
    else:
        print("Access denied")
