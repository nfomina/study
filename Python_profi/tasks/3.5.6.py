from datetime import datetime

birthdays = {}

for _ in range(int(input())):
    name, family, date = input().split()
    date = datetime.strptime(date, '%d.%m.%Y')
    if birthdays.get(date):
        birthdays[date] += 1
    else:
        birthdays[date] = 1


max_value = max(birthdays.values())

max_dates = []
for item, value in birthdays.items():
    if value == max_value:
        max_dates.append(item)

for item in sorted(max_dates):
    print(item.strftime('%d.%m.%Y'))
# max(stats, key=stats.get)

# 5
# Иван Петров 01.05.1995
# Петр Сергеев 29.04.1995
# Сергей Романов 01.01.1996
# Роман Григорьев 01.01.1996
# Григорий Иванов 01.05.1995