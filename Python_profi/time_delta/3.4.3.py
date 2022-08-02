from datetime import datetime, timedelta

current_day = datetime.strptime(input(), '%d.%m.%Y')

print((current_day - timedelta(days=1)).strftime('%d.%m.%Y'))
print((current_day + timedelta(days=1)).strftime('%d.%m.%Y'))
