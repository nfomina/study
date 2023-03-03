def number_of_frogs(year):
    if year == 1:
        return 77
    else:
        year -= 1
        return 3 * (number_of_frogs(year)-30)


print(number_of_frogs(2))
print(number_of_frogs(10))
print(number_of_frogs(1))
