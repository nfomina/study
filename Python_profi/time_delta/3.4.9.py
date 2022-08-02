from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    res = []
    dates = [datetime.strptime(item, '%d.%m.%Y') for item in dates]
    if dates:
        min_date = min(dates)
        max_date = max(dates)
        while min_date <= max_date:
            res.append(min_date.strftime('%d.%m.%Y'))
            min_date = min_date + timedelta(days=1)
    return res


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))

dates = []

print(fill_up_missing_dates(dates))