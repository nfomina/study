str1 = input()
str2 = input()

if len(set(str1+str2)) == 10:
    print('YES')
else:
    print('NO')