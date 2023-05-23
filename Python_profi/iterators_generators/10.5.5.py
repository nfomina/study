from datetime import date, timedelta


def dates(start, count=None):
    n = 0
    while n != count:
        n += 1
        yield start
        if start != date(9999, 12, 31):
            start = start + timedelta(1, 0, 0)
        else:
            return StopIteration


generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))

generator = dates(date(2022, 3, 8), 5)

print(*generator)

# TEST_6:
generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')

