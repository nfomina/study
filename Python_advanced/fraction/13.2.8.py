from fractions import Fraction

n = int(input())

all_fractions = set()
for i in range(1, n):
    for j in range(1, n+1):
        if i < j:
            all_fractions.add((Fraction(i, j)))
for item in sorted(all_fractions):
    print(item)

# so beauty
# from fractions import Fraction
#
# numbers = set()
#
# for i in range(2, int(input()) + 1):
#     for j in range(1, i):
#         numbers.add(Fraction(j, i))
#
# print(*sorted(numbers), sep='\n')