from datetime import date

florida_hurricane_dates = [date(1950, 1, 1), date(1953, 10, 10), date(1960, 12, 17), date(1958, 4, 12), date(1999, 1, 7),
                           date(1957, 10, 1), date(1998, 2, 13), date(1950, 1, 12), date(2017, 1, 1)]


# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)