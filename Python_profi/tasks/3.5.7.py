from datetime import datetime, timedelta

today_date = datetime.strptime(input(), '%d.%m.%Y')
birthday_dates = [((today_date + timedelta(days=x)).day, (today_date + timedelta(days=x)).month)  for x in range(1, 8)]

persons = {}
for _ in range(int(input())):
    name, family, date = input().split()
    date = datetime.strptime(date, '%d.%m.%Y')
    birthday_date = (date.day, date.month)
    if birthday_date in birthday_dates:
        persons[date] = (name, family)

if persons:
    print(*persons[max(persons)])

else:
    print('Дни рождения не планируются')
