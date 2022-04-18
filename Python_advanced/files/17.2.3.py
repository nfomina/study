import random

with open('lines.txt') as file:
    text = file.readlines()
print(text[random.randint(0, len(text))])
