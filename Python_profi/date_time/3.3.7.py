from datetime import datetime, date

def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

def is_available_date(booked_dates, date_for_booking):
    booked_date = []
    for date_ in booked_dates:
        if len(date_) == 10:
            booked_date.append(datetime.strptime(date_, '%d.%m.%Y'))
        else:
            start, end = date_.split('-')
            for d in get_date_range(datetime.strptime(start, '%d.%m.%Y'), datetime.strptime(end, '%d.%m.%Y')):
                booked_date.append(datetime.combine(d, datetime.min.time()))
    if len(date_for_booking) == 10:
        if datetime.strptime(date_for_booking, '%d.%m.%Y')not in booked_date:
            return True
    else:
        booking_dates = []
        start, end = date_for_booking.split('-')
        for d in get_date_range(datetime.strptime(start, '%d.%m.%Y'), datetime.strptime(end, '%d.%m.%Y')):
            booking_dates.append(datetime.combine(d, datetime.min.time()))
        if len(set(booking_dates) - set(booked_date)) == len(booking_dates):
            return True
    return False

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '15.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '17.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))


#  smart
# from datetime import date, time, datetime
# def is_available_date(booked_dates, date_for_booking):
#     ord_booked_dates = []
#     for d in booked_dates:
#         dates = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in d.split('-')]
#         ord_booked_dates.extend(range(dates[0], dates[-1] + 1))
#     dt = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in date_for_booking.split('-')]
#     date_f_b = range(dt[0], dt[-1] + 1)
#     return(all([i not in ord_booked_dates for i in date_f_b]))