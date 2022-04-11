import random

numbers = []

while len(numbers) < 7:
    i = random.randint(1, 49)
    if i not in numbers:
        numbers.append(i)

print(*sorted(numbers))