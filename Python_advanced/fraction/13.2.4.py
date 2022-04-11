from fractions import Fraction
a = input()
b = input()
first = Fraction(a)
second = Fraction(b)

print(f'{a} + {b} = {first + second}')
print(f'{a} - {b} = {first - second}')
print(f'{a} * {b} = {first * second}')
print(f'{a} / {b} = {first / second}')