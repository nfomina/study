import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

def get_weekday(number):
    if not type(number) is int:
        raise TypeError('Аргумент не является целым числом')
    elif number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return calendar.day_name[number-1]


try:
    print(get_weekday('4'))
except Exception as err:
    print(err)
    print(type(err))
