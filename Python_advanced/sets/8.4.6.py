string = input()

if len(string) == len(set(string)):
    print('YES')
else:
    print('NO')