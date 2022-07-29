from datetime import date

def print_good_dates(dates):
    beauty_dates = []
    for date_ in dates:
        if date_.year == 1992 and date_.month + date_.day == 29:
            beauty_dates.append(date_)
    if beauty_dates:
        for item in sorted(beauty_dates):
            print(item.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)

print_good_dates([])

dates = [date(1992, 5, 24), date(1000, 1, 1), date(2000, 2, 2), date(3000, 3, 3)]
print_good_dates(dates)

dates = [date(1257, 8, 22), date(1765, 8, 23), date(1999, 9, 9), date(1992, 6, 23)]
print_good_dates(dates)

dates = [date(1992, 9, 20), date(1992, 8, 21), date(1992, 7, 22), date(1992, 10, 19)]
print_good_dates(dates)

dates = [date(1257, 12, 12), date(1992, 6, 23), date(1284, 11, 2)]
print_good_dates(dates)

print(print_good_dates([]))

# short
# def print_good_dates(dates):
#     for d in sorted(filter(lambda d: d.year == 1992 and d.month + d.day == 29, dates)):
#         print(d.strftime('%B %d, %Y'))