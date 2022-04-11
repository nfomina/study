from fractions import Fraction
from math import factorial

n = int(input())

result = 0
for i in range(1, n + 1):
    result += Fraction(1, factorial(i))

print(result)