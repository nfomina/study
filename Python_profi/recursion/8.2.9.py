def print_digits(number):
    def rec(step):
        if step < len(str(number)):
            rec(step + 1)
            print(str(number)[step])
    rec(0)


print_digits(12345)
print()
print_digits(7)
print()
print_digits(76)

# genius
# def print_digits(number):
#     if str(number):
#         print(str(number)[-1])
#         print_digits(str(number)[:-1])
