def to_binary(number):
    if number == 0 or number == 1:
        return number
    else:
        return str(to_binary(number//2)) + str(number % 2)


print(to_binary(15))
# 1111
print(to_binary(0))
print(to_binary(1))
print(to_binary(2))
print(to_binary(3))
print(to_binary(4))
print(to_binary(5))

