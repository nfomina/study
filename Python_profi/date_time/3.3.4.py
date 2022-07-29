from datetime import date, time, datetime

dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]

datetimes = []
for i in range(len(dates)):
    datetimes.append(datetime.combine(dates[i], times[i]))

datetimes.sort(key = lambda x: x.second)
for item in datetimes:
    print(item)

# beauty
# datetimes = [datetime.combine(d, t) for d, t in zip(dates, times)]
#
# print(*sorted(datetimes, key=lambda dt: dt.second), sep='\n')