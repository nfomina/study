numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

max = abs(numbers[0])
item_max = numbers[0]
for item in numbers:
    if abs(item) > max:
        max = abs(item)
        item_max = item

print(item_max)
print(max)

# smart
# print(max(numbers, key=abs))
# print(abs(max(numbers, key=abs)))