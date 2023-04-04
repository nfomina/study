def power(degree):
    def power_degree(x):
        return pow(x, degree)
    return power_degree


square = power(2)
print(square(5))

print(power(3)(3))

result = power(4)(2)
print(result)

# with lambda
# def power(degree):
#     return lambda x: x ** degree
