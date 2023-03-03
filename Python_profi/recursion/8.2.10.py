def print_digits(number):
    if str(number):
        print_digits(str(number)[:-1])
        print(str(number)[-1])


print_digits(12345)
print()
print_digits(7)
print()
print_digits(76)
