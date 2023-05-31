from re import search
import sys


for line in sys.stdin:
    match = search('(?P<country>\d+)[\s-](?P<city>\d+)[\s-](?P<number>\d+)', line)
    items = match.groupdict()
    print(f'Код страны: {items.get("country")}, Код города: {items.get("city")}, Номер: {items.get("number")}')
