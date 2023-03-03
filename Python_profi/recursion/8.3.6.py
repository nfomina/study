def get_fast_pow(a, n):
    if n == 0:
        return 1
    else:
        return a * get_fast_pow(a, n//2) * get_fast_pow(a, (n-1)//2)


print(get_fast_pow(5, 2))
print(get_fast_pow(2, 100))

#       1267650600228229401496703205376


# Пусть a = 2,   n = 5.
#
# 2**5 = (2**4) * (2**1)
#
# 2**4 = (2**2) * (2**2)
#
# 2**2 = (2**1) * (2**1)
#
# 2**1 = 2 * (2**0)
#
# 2**0 - базовый случай и равен 1.
#
# То есть get_fast_pow(a, n // 2) * get_fast_pow(a, n // 2) это тоже самое, что
#
# get_fast_pow(a * a, n // 2)
