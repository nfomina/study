word = input()
n = int(input())

dict_count = {}
for _ in range(n):
    letter, count = input().split(': ')
    dict_count[int(count)] = letter

symbols = {}
for item in word:
    symbols[item] = symbols.get(item, 0) + 1

for item in word:
    print(dict_count.get(symbols.get(item)), end='')

