n = int(input())

atlas = {}
for _ in range(n):
    country, *cities = input().split()
    atlas[country] = cities

m = int(input())
for _ in range(m):
    city = input()
    for country, cities in atlas.items():
        if city in cities:
            print(country)