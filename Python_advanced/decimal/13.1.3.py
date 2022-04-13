from decimal import *
num = Decimal(input())
digits = num.as_tuple().digits
if str(abs(num)).startswith('0'):
    min = 0
else:
    min = min(digits)

print(min + max(digits))
