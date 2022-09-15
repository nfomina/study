import calendar

year, month, day = input().split('-')
print(calendar.day_name[calendar.weekday(int(year), int(month), int(day))])