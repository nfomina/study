from datetime import datetime, timedelta

time = datetime.strptime(input(), '%H:%M:%S')
n = int(input())

print(datetime.strftime(time+timedelta(seconds=n), '%H:%M:%S'))