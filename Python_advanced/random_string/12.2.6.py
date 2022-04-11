import random

numbers = random.sample(range(1,76), 24)
midpoint = len(numbers)//2

numbers = numbers[0:midpoint] + [0] + numbers[midpoint:]

for i in range(0, len(numbers), 5):
    for item in numbers[i:i+5]:
        print(str(item).ljust(3), end='')
    print()