import calendar
from datetime import date

def get_days_in_month(year, month):
    month = list(calendar.month_name).index(month)
    last_day = calendar.monthrange(int(year), month)[1]
    return [date(year, month, i) for i in range(1, last_day+1)]

print(get_days_in_month(2021, 'February'))