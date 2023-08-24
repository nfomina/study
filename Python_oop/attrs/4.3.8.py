class Numbers:
    def __init__(self):
        self.even = []
        self.odd = []

    def add_number(self, n):
        if n % 2 == 0:
            self.even.append(n)
        else:
            self.odd.append(n)

    def get_even(self):
        return self.even.copy()

    def get_odd(self):
        return self.odd.copy()


numbers = Numbers()

print(numbers.get_even())
print(numbers.get_odd())

numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())

numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())

# TEST_4:
numbers = Numbers()

numbers.add_number(2)
numbers.add_number(2)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())

# TEST_5:
numbers = Numbers()

numbers.add_number(1)
numbers.add_number(2)
numbers.add_number(3)
numbers.add_number(4)

even = numbers.get_even()
odd = numbers.get_odd()
print(numbers.get_even())
print(numbers.get_odd())

even.append(None)
odd.append(None)
print(numbers.get_even())
print(numbers.get_odd())

# TEST_6:
numbers = Numbers()

for n in range(1, 100, 2):
    numbers.add_number(n)

print(numbers.get_even())
print(numbers.get_odd())

# TEST_7:
numbers = Numbers()

for n in range(0, 100, 2):
    numbers.add_number(n)

print(numbers.get_even())
print(numbers.get_odd())
