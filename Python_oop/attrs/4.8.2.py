from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(bool)
    @staticmethod
    def _from_bool(data):
        return not data

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _from_digit(data: int | float) -> int | float:
        return data*(-1)


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

try:
    Negator.neg('number')
except TypeError as e:
    print(e)
