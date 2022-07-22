n = int(input())
languages = input().split(', ')

for _ in range(n-1):
    languages = set(languages) & set(input().split(', '))
if languages:
    print(', '.join(sorted(languages)))
else:
    print('Сериал снять не удастся')