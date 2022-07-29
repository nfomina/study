from datetime import date

def get_date_range(start, end):
    res = []
    while start <= end:
        res.append(start)
        start = start.toordinal() + 1
        start = date.fromordinal(start)
    return res


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 6)

print(get_date_range(date1, date2))

date1 = date(2019, 6, 5)
date2 = date(2022, 6, 6)
print(len(get_date_range(date1, date2)))


date1 = date(2025, 6, 5)
date2 = date(2022, 6, 6)
print(len(get_date_range(date1, date2)))

# short
# def get_date_range(start, end):
#     return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]


