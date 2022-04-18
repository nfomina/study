from random import choice

with open('first_names.txt') as file:
    names = file.readlines()

with open('last_names.txt') as file:
    families = file.readlines()

for _ in range(3):
    print(f'{choice(names)[:-1]} {choice(families)[:-1]}')