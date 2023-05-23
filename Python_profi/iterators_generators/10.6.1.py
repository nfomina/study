def cubes_of_odds(iterable):
    for cube in (number ** 3 for number in iterable if number % 2):
        yield cube


print(*cubes_of_odds([1, 2, 3, 4, 5]))

evens = [2, 4, 6, 8, 10]

print(list(cubes_of_odds(evens)))

# short
# def cubes_of_odds(iterable):
#     yield from (number**3 for number in iterable if number%2)
