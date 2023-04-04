from datetime import date


def date_formatter(country_code):
    d = {'ru': '%d.%m.%Y',
         'us': '%m-%d-%Y',
         'ca': '%Y-%m-%d',
         'br': '%d/%m/%Y',
         'fr': '%d.%m.%Y',
         'pt': '%d-%m-%Y', }
    return lambda a: a.strftime(d.get(country_code))


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))
# 25.01.2022

date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))
# 01-05-2025

date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))
# 2015-12-07
