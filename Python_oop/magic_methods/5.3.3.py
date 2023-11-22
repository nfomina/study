from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.month == other.month and self.year == other.year
        elif isinstance(other, tuple) and len(other) == 2:
            return self.month == other[1] and self.year == other[0]
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return self.year < other.year or (self.year == other.year and self.month < other.month)
        elif isinstance(other, tuple) and len(other) == 2:
            return self.year < other[0] or (self.year == other[0] and self.month < other[1])
        return NotImplemented


print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(min(months))
print(max(months))

# TEST_6:
print(Month(1999, 12) == (1999, 12))
print(Month(1999, 12) < (2000, 1))
print(Month(1999, 12) > (2000, 1))
print(Month(1999, 12) <= (1999, 12))
print(Month(1999, 12) >= (2000, 1))

# TEST_7:
month = Month(2023, 4)

print(month.__eq__(1))
print(month.__ne__(1.1))
print(month.__gt__(range(5)))
print(month.__lt__([1, 2, 3]))
print(month.__ge__({4, 5, 6}))
print(month.__le__({1: 'one'}))

# TEST_4:
month = Month(2023, 4)
not_supported = ['04.2023', 4.0, 2023, True, {2023: 4}, {4, 2023}, False, (2023, 4, 'dont know')]
for obj in not_supported:
    print(month == obj)

# beauty
# from functools import total_ordering
#
#
# @total_ordering
# class Month:
#     def __init__(self, year, month):
#         self.year = year
#         self.month = month
#
#     def __str__(self):
#         return f'{self.year}-{self.month}'
#
#     def __repr__(self):
#         return f"Month({self.year}, {self.month})"
#
#     def __eq__(self, other):
#         if isinstance(other, Month):
#             return (self.year, self.month) == (other.year, other.month)
#         elif isinstance(other, tuple):
#             return (self.year, self.month) == other
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Month):
#             return (self.year, self.month) < (other.year, other.month)
#         elif isinstance(other, tuple):
#             return (self.year, self.month) < other
#         return NotImplemented
