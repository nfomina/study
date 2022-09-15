import calendar

year = int(input())

c = calendar.Calendar(firstweekday=calendar.THURSDAY)
third_thursday = []

for month in range(1, 13):
    monthcal = c.monthdatescalendar(year, month)
    third_thursday.append([day for week in monthcal for day in week if \
                           day.weekday() == calendar.THURSDAY and \
                           day.month == month][2])
for item in third_thursday:
    print(item.strftime("%d.%m.%Y"))
