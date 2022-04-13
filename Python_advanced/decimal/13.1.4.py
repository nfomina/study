from decimal import *

d = Decimal(input())
print(Decimal.exp(d) + Decimal.ln(d) + Decimal.log10(d) + Decimal.sqrt(d))

#  short
# from decimal import Decimal
#
# d = Decimal(input())
#
# print(d.exp() + d.ln() + d.log10() + d.sqrt())