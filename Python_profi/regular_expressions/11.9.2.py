import re


print(', '.join([i.strip() for i in re.split(r'\s?[|&]\s?|\s?and\s?|\s?or\s?', input())]))

# easy
# print(*re.split(r'\s*(?:[|&]|and|or)\s*', input()), sep=', ')
