
with open(input()) as file:
    strings = file.readlines()
    if len(strings) < 10:
        res = strings
    else:
        res = strings[-10:]
for item in res:
    print(item.rstrip())