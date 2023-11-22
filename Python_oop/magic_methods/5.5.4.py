class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = self.converter(minutes, hours)

    def converter(self, _minutes, _hours):
        delta = 0
        if _minutes >= 60:
            delta = _minutes//60
            _minutes = _minutes % 60
        if _hours >= 24:
            _hours = _hours % 24
        _hours += delta
        return _hours, _minutes

    def __str__(self):
        return f'{self.hours:>02}:{self.minutes:>02}'

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.minutes += other.minutes
            self.hours += other.hours
            self.hours, self.minutes = self.converter(self.minutes, self.hours)
            return self
        return NotImplemented


time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)

time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)

time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)

# TEST_7:
t = Time(40, 80)
print(t.__add__([]))
print(t.__iadd__('bee'))

# TEST_8:
t = Time(22, 0)
t += Time(3, 0)
print(t)

# TEST_9:
t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)
