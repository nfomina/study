class HourClock:
    def __init__(self, hour):
        self.hour = self.set_hours(hour)

    def set_hours(self, hour):
        if isinstance(hour, int) and 0 < hour <= 12:
            self._hour = hour
        else:
            raise ValueError('Некорректное время')

    def get_hours(self):
        return self._hour

    hours = property(get_hours, set_hours)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)

# TEST_2:
time = HourClock(7)

try:
    time.hours = 15
except ValueError as e:
    print(e)

# TEST_3:
try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)

# TEST_4:
try:
    HourClock(0)
except ValueError as e:
    print(e)

# TEST_5:
try:
    HourClock('ten o`clock')
except ValueError as e:
    print(e)

# TEST_6:
time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)

# TEST_7:
time = HourClock(1)
print(hasattr(HourClock, 'hours'))
