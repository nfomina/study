my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

for key, values in my_dict.items():
    new_numbers = []
    for number in values:
        if number <= 20:
            new_numbers.append(number)
    my_dict[key] = new_numbers
print(my_dict)
