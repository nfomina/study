def get_pow(a, n):
    if n == 0:
        return 1
    else:
        return a * get_pow(a, n-1)


print(get_pow(1, 1))
print(get_pow(2, 7))
print(get_pow(4, 0))
print(get_pow(5, 2))
print(get_pow(2, 10))
