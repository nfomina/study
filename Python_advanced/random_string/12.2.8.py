import random
import string

letters = string.ascii_letters
digits = string.digits
letters = letters.translate({ord(c): '' for c in 'lIoO'})
digits = digits.translate({ord(c): '' for c in '01'})
symbols = letters + digits

def generate_password(length):
    return ''.join(random.sample(symbols, length))

def generate_passwords(count, length):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords

n, m = int(input()), int(input())

for item in generate_passwords(n,m):
    print(item)