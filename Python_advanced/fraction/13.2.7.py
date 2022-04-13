from fractions import Fraction
n = int(input())

fractions = []

for i in range(1, n):
    for j in range(1, n):
        if i + j == n and i < j:
            if str(Fraction(i, j)) == f'{i}/{j}':
                fractions.append(Fraction(i, j))

print(max(fractions))


# smart
# from fractions import Fraction as F
# from math import gcd
#
# n = int(input())
# a = n // 2
# b = n - a
# while gcd(a, b) != 1:
#     a -= 1
#     b += 1
# print(F(a, b))