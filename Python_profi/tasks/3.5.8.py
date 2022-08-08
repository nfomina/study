from datetime import datetime

def choose_plural(amount, declensions):
    n = amount % 100
    if n >= 11 and n <= 19:
        s = declensions[2]
    else:
        i = n % 10
        if i == 1:
            s = declensions[0]
        elif i in [2, 3, 4]:
            s = declensions[1]
        else:
            s = declensions[2]
    return f'{amount} {s}'


date_x = datetime(2022, 11, 8, 12)
date_now = datetime.strptime(input(), '%d.%m.%Y %H:%M')

delta = date_x-date_now

days = delta.days
hours = delta.seconds//3600
minutes  = (delta.seconds - hours*3600)//60

if days < 0 or (days == 0 and hours == 0 and minutes == 0):
    print('Курс уже вышел!')
elif days == 0 and hours == 0:
    print(f'До выхода курса осталось: {choose_plural(minutes, ("минута", "минуты","минут"))}')
elif days == 0:
    if minutes == 0:
        print(f'До выхода курса осталось: {choose_plural(hours, ("час", "часа","часов"))}')
    else:
        print(f'До выхода курса осталось:'
              f' {choose_plural(hours, ("час", "часа","часов"))} и'
              f' {choose_plural(minutes, ("минута", "минуты","минут"))}')
else:
    if hours == 0:
        print(f'До выхода курса осталось: {choose_plural(days, ("день", "дня","дней"))}')
    else:
        print(f'До выхода курса осталось:'
              f' {choose_plural(days, ("день", "дня","дней"))}'
              f' и {choose_plural(hours, ("час", "часа", "часов"))}')

