def my_pow(number):
    return sum(pow(int(element), index+1) for index, element in enumerate(str(number)))


print(my_pow(139))
print(my_pow(123))
print(my_pow(0))
