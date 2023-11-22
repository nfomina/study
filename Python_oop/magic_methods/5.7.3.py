import math
from functools import total_ordering


def integer_to_roman(int_number):
    romans_dict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }

    div = 1
    while int_number >= div:
        div *= 10
    div /= 10
    res = ""
    while int_number:
        last_num = int(int_number / div)

        if last_num <= 3:
            res += (romans_dict[div] * last_num)
        elif last_num == 4:
            res += (romans_dict[div] +
                    romans_dict[div * 5])
        elif 5 <= last_num <= 8:
            res += (romans_dict[div * 5] +
                    (romans_dict[div] * (last_num - 5)))
        elif last_num == 9:
            res += (romans_dict[div] +
                    romans_dict[div * 10])

        int_number = math.floor(int_number % div)
        div /= 10
    return res


def roman_to_int(roman_number):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(roman_number):
        if i + 1 < len(roman_number) and roman_number[i:i + 2] in roman:
            num += roman[roman_number[i:i + 2]]
            i += 2
        else:
            num += roman[roman_number[i]]
            i += 1
    return num


@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number
        self.int_number = roman_to_int(self.number)

    def __str__(self):
        return self.number

    def __int__(self):
        return self.int_number

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.int_number == other.int_number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.int_number < other.int_number
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(integer_to_roman(self.int_number + other.int_number))
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(integer_to_roman(self.int_number - other.int_number))
        else:
            return NotImplemented


number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))

number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))

a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)