import random
import string

letters = string.ascii_uppercase
numbers = string.digits

def generate_index():
    return f'{random.choice(letters)}{random.choice(letters)}{random.choice(numbers)}_{random.choice(numbers)}{random.choice(letters)}{random.choice(letters)}'

print(generate_index())