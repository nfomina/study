numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}

new_numbers = set()
for item in numbers:
    new_numbers.add(item*item)

print(sum(new_numbers))


# in one line
# print(sum(num * num for num in numbers))