def polynom(x):
    polynom.values.add(x*x+1)
    return x*x + 1


polynom.values = set()

# polynom(1)
# polynom(2)
# polynom(3)
#
# print(*sorted(polynom.values))

for _ in range(10):
    polynom(10)

print(polynom.values)

# smart
# def polynom(x):
#     polynom.__dict__.setdefault('values', set())
#     value = x**2 + 1
#     polynom.values.add(value)
#     return value
