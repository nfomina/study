from datetime import datetime

dates = [datetime.strptime(item, '%d.%m.%Y') for item in input().split()]

count_days = []

for i, item in enumerate(dates):
    if i > 0:
        count_days.append(abs(item - dates[i-1]).days)

print(count_days)


