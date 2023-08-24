from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(str)
    @staticmethod
    def _from_str(data):
        return data.upper()

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_digit(data: int | float) -> int | float:
        return data * 2

    @process.register(list)
    @staticmethod
    def _from_list(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(data):
        return tuple(sorted(data))


print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))

try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)
