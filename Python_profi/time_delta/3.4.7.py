from datetime import datetime, timedelta

start_date = datetime.strptime(input(), '%d.%m.%Y')
for i in range(1, 11):
    print(start_date.strftime('%d.%m.%Y'))
    start_date = start_date + timedelta(days=i+1)


# 20.12.2021
# 22.12.2021
# 25.12.2021
# 29.12.2021
# 03.01.2022
# 09.01.2022
# 16.01.2022
# 24.01.2022
# 02.02.2022
# 12.02.2022