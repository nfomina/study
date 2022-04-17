from functools import reduce

def product_of_odds(data):   # data - список целых чисел
    return reduce(lambda num1, num2: num1 * num2, list(filter(lambda a: a% 2 == 1, data)), 1)

print(product_of_odds([]))

