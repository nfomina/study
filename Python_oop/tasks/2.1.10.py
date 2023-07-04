def is_decimal(string):
    try:
        float(string)
        return True
    except:
        return False


print(is_decimal('100'))
print(is_decimal('199.1'))
print(is_decimal('-0.2'))
print(is_decimal('.-95'))
print(is_decimal('-.95'))
print(is_decimal('.10'))
