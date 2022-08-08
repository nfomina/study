from datetime import datetime, timedelta

start = datetime(1, 1, 13)
end = datetime(9999, 12, 13)
count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}

while start <= end:
    if start.day == 13:
        count[start.isoweekday()] += 1
    start += timedelta(days=1)
for item in count:
    print(count[item])


#  faster
# from datetime import date
# from collections import Counter
#
# weekdays = Counter([date(year=i, month=j, day=13).isoweekday() for i in range(1, 10000) for j in range(1, 13)])
#
# for i in range(1, 8):
#     print(weekdays[i])