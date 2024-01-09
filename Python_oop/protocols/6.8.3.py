class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self.times = times
        self._count = 0

    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            self._count += 1
            if self._count > self.times:
                raise MaxCallsException('Превышено количество доступных обращений')
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value

