from datetime import datetime


def num_of_sundays(year):
    start = datetime(year=year, month=1, day=1)
    end = datetime(year=year, month=12, day=31)
    num_weeks, remainder = divmod( (end-start).days+1, 7)
    if (7 - start.isoweekday()) % 7 < remainder:
        return num_weeks + 1
    else:
        return num_weeks


print(num_of_sundays(2021))

year = 2000
print(num_of_sundays(year))

print(num_of_sundays(768))

print(num_of_sundays(1944))

print(num_of_sundays(2022))

print(num_of_sundays(2050))
