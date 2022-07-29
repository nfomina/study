from datetime import date

def get_min_max(dates):
    if dates:
        return min(dates), max(dates)
    return ()

dates = [date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5)]

print(get_min_max(dates))