from datetime import date

def saturdays_between_two_dates(start, end):
    saturdays = 0
    if start > end:
        start, end = end, start
    while start <= end:
        if start.weekday() == 5:
            saturdays += 1
        start = start.toordinal() + 1
        start = date.fromordinal(start)
    return saturdays

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2010, 6, 13)
date2 = date(2011, 7, 14)
print(saturdays_between_two_dates(date1, date2))

date1 = date(2012, 7, 11)
date2 = date(2011, 8, 16)
print(saturdays_between_two_dates(date1, date2))

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 5)
print(saturdays_between_two_dates(date1, date2))

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 6)
print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 14)
date2 = date(2018, 7, 14)
print(saturdays_between_two_dates(date1, date2))

# another cheat
# def saturdays_between_two_dates(start, end):
#     if start > end:
#         start, end = end, start
#
#     return sum(date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), end.toordinal() + 1))