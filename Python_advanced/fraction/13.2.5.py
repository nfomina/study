from fractions import Fraction

n = int(input())

result = 0
for i in range(1, n + 1):
    result += Fraction(1, i**2)

print(result)