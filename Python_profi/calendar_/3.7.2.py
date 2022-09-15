import calendar

year, month = input().split()
mapping = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12}
print(calendar.month(int(year), mapping.get(month)))

# beauty
# from calendar import prmonth
# from datetime import datetime
#
# dt = datetime.strptime(input() + ' 1', '%Y %b %d')
#
# prmonth(dt.year, dt.month)