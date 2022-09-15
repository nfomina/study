import calendar
from datetime import date, timedelta

def get_all_mondays(year):
    res = []
    d = date(year, 1, 1)
    if calendar.weekday(d.year, d.month, d.day) != 0:
        while calendar.weekday(d.year, d.month, d.day) != 0:
            d += timedelta(days = 1)
    while d.year == year:
        res.append(d)
        d += timedelta(days=7)
    return res


print(get_all_mondays(1353))

# beauty
# def get_all_mondays(year):
#     mondays = []
#     for month in range(1, 13):
#         for week in calendar.monthcalendar(year, month):
#             monday = week[0]
#             if monday:
#                 mondays.append(date(year, month, monday))
#     return mondays