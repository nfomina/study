import sys
boys = ['Анри', 'Дима']

data = [int(i) for i in sys.stdin]
if data[-1] % 2 == 0:
    print(boys[abs((len(data) % 2)-1)])
else:
    print(boys[len(data) % 2])

# short and beauty
# import sys
# s = tuple(int(i.strip()) for i in sys.stdin.readlines())
# print(('Дима', 'Анри')[(len(s) - 1) % 2 == s[-1] % 2])