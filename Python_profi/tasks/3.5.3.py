from datetime import timedelta, datetime

schedule = {
    1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    5: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    7: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }

date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
delta = timedelta(hours=date.hour, minutes=date.minute)
if schedule.get(date.isoweekday())['start'] > delta or schedule.get(date.isoweekday())['end'] <= delta:
    print('Магазин не работает')
else:
    print(int((schedule.get(date.isoweekday())['end'] - delta).total_seconds()//60))