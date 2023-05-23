from datetime import date, timedelta


def years_days(year):
    day = date(year, 1, 1)
    yield day
    while day < date(year, 12, 31):
        day += timedelta(1)
        yield day


dates = years_days(2022)

print(list(dates))
