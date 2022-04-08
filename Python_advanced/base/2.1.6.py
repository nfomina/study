a = int(input())
if len(str(a)) == 5:
    print(int(str(a)[::-1]))
else:
    print(int((str(a)[0] + str(a)[:-6:-1])))