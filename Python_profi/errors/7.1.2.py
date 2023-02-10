def get_max_index(numbers):
    max_index = 0
    max_value = numbers[0]

    for index, value in enumerate(numbers, 0):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index


print(get_max_index([1, 8, 15]))
print(get_max_index([8, 1, 2]))
print(get_max_index([8, 12, 2]))
