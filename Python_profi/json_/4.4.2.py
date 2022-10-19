import json
import sys


data = json.loads(sys.stdin.read())
for item in data.items():
    if type(item[1]) == list:
        print(f'{item[0]}: {", ".join([str(i) for i in item[1]])}')
    else:
        print(f'{item[0]}: {item[1]}')
