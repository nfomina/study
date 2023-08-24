from functools import singledispatchmethod


mapping = {int: 'Целое число',
           float: 'Вещественное число',
           tuple: 'Элементы кортежа',
           list: 'Элементы списка',
           dict: 'Пары словаря'}


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')


    @format.register(int)
    @format.register(float)
    @staticmethod
    def _from_data(data: int | float) -> str:
        print(f'{mapping.get(type(data))}: {data}')

    @format.register(tuple)
    @format.register(list)
    @staticmethod
    def _from_data(data: tuple | list) -> str:
        print(f'{mapping.get(type(data))}: ', end='')
        print(*data, sep=", ")

    @format.register(dict)
    @staticmethod
    def _from_data(data: dict) -> str:
        print(f'{mapping.get(type(data))}: ', end='')
        print(*data.items(), sep=", ")


Formatter.format(1337)
Formatter.format(20.77)

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})

try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
