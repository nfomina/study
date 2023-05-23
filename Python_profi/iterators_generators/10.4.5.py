class PowerOf:
    def __init__(self, number):
        self.number = number
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        return pow(self.number, self.start)



power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
