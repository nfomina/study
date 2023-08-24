from functools import singledispatchmethod
from datetime import date, datetime


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @singledispatchmethod
    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date
        self.age = self._age()

    @singledispatchmethod
    @__init__.register(str)
    def _from_str(self, birth_date):
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        self.age = self._age()

    @singledispatchmethod
    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_tuple(self, birth_date):
        self.birth_date = date(year=birth_date[0], month=birth_date[1], day=birth_date[2])
        self.age = self._age()

    def _age(self):
        if date.today().month > self.birth_date.month:
            return date.today().year - self.birth_date.year
        elif date.today().month == self.birth_date.month:
            if date.today().day >= self.birth_date.day:
                return date.today().year - self.birth_date.year
            else:
                return date.today().year - self.birth_date.year - 1
        else:
            return date.today().year - self.birth_date.year - 1


birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)

birthday = date(2020, 9, 18)
today = date.today()
birthinfo = BirthInfo(birthday)
true_age = 3

print(birthinfo.age == true_age)

# TEST_3:
birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(type(birthinfo1.birth_date))
print(type(birthinfo2.birth_date))
print(type(birthinfo3.birth_date))

# TEST_4:
birthday = date(2023, 3, 6)
today = date.today()
birthinfo = BirthInfo(birthday)
true_age = 0

print(birthinfo.age == true_age)

# TEST_5:
errors = [20200918, True, {1: 'one'}, {1, 2, 3}, 100.9]

for obj in errors:
    try:
        BirthInfo(obj)
    except TypeError as e:
        print(e)

# TEST_6:
from datetime import timedelta
today = date.today()
for day in range(10):
    birthday = (today + timedelta(days=day)).replace(year=2000)
    print(birthday)

    birthinfo = BirthInfo(birthday)
    print(birthinfo.age)
    true_age = 22
    print(birthinfo.age == true_age)
