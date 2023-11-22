from datetime import datetime, date

_data = {
        "ru": r"%d.%m.%Y",
        "us": r"%m-%d-%Y",
        "ca": r"%Y-%m-%d",
        "br": r"%d/%m/%Y",
        "fr": r"%d.%m.%Y",
        "pt": r"%d-%m-%Y"
    }


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        return datetime.strftime(d, _data.get(self.country_code))


ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))

us_format = DateFormatter('us')

print(us_format(date(2022, 11, 7)))

ca_format = DateFormatter('ca')

print(ca_format(date(2022, 11, 7)))