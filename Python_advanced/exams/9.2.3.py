n = int(input())

cities = set()
for _ in range(n):
    cities.add(input())

new_city = input()
if new_city in cities:
    print('REPEAT')
else:
    print('OK')
