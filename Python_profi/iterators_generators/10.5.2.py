def alternating_sequence(count=None):
    if count:
        for number in range(1, count + 1):
            if number % 2 == 0:
                yield number*(-1)
            else:
                yield number
    else:
        number = 1
        while True:
            if number % 2 == 0:
                yield number*(-1)
            else:
                yield number
            number += 1


generator = alternating_sequence()

print(next(generator))
print(next(generator))

generator = alternating_sequence(10)

print(*generator)

# so smart
# def alternating_sequence(count=None):
#   n = 0
#   while n != count:
#     n += 1
#     sign = [-1, 1][n % 2]
#     yield n * sign
