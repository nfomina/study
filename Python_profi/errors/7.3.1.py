import calendar

month = input()

try:
    number_month = int(month)
    if number_month >= 1 and number_month <= 12:
        print(calendar.month_name[number_month])
    else:
        print('Введено число из недопустимого диапазона')
except:
    print('Введено некорректное значение')


# from calendar import month_name
#
# try:
#     print(dict(enumerate(month_name[1:], 1))[int(input())])
# except KeyError:
#     print('Введено число из недопустимого диапазона')
# except:
#     print('Введено некорректное значение')