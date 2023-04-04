def non_negative_even(numbers):
    if all([True if i % 2 == 0 and i >= 0 else False for i in numbers]):
        return True
    return False


print(non_negative_even([0, 2, 4, 8, 16]))
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
print(non_negative_even([0, 0, 0, 0, 0]))

# short
# def non_negative_even(numbers):
#     return all(i >= 0 and i % 2 == 0 for i in numbers)
