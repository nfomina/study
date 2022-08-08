from datetime import datetime, timedelta


start_date = datetime.strptime(input(), '%d.%m.%Y')
end_date = datetime.strptime(input(), '%d.%m.%Y')

while start_date <= end_date:
    if (start_date.day + start_date.month) % 2 == 1:
        if start_date.isoweekday() != 1 and start_date.isoweekday() != 4:
            print(start_date.strftime('%d.%m.%Y'))
        start_date = start_date + timedelta(days=3)
        break
    start_date = start_date + timedelta(days=1)

while start_date <= end_date:
    if start_date.isoweekday() != 1 and start_date.isoweekday() != 4:
        print(start_date.strftime('%d.%m.%Y'))
    start_date = start_date + timedelta(days=3)

# Программа должна из указанного диапазона, включая концы, вывести, начиная с даты,
# у которой сумма дня и месяца нечетная,
# каждую третью дату, только если она не понедельник и не четверг. Даты должны быть расположены каждая на отдельной строке, в формате DD.MM.YYYY.