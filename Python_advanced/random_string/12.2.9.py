import random
import string

letters = string.ascii_letters
digits = string.digits
letters = letters.translate({ord(c): '' for c in 'lIoO'})
digits = digits.translate({ord(c): '' for c in '01'})
symbols = letters + digits

def has_numbers(string):
    return any(char.isdigit() for char in string)

def has_lower(string):
    return any(char.islower() for char in string)

def has_upper(string):
    return any(char.isupper() for char in string)

def generate_password(length):
    while True:
        password = ''.join(random.sample(symbols, length))
        if has_numbers(password) and has_lower(password) and has_upper(password):
            return password

def generate_passwords(count, length):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords

n, m = int(input()), int(input())

for item in generate_passwords(n,m):
    print(item)