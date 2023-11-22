class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, value):
        celsius = (5 / 9) * (value - 32)
        return cls(celsius)

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def __bool__(self):
        if self.temperature > 0:
            return True
        return False

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


t = Temperature(5.5)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())

t1 = Temperature(1)
t2 = Temperature(0)
t3 = Temperature(-1)

print(bool(t1))
print(bool(t2))
print(bool(t3))


t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())