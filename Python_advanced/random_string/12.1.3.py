import random

length = int(input())    # длина пароля

letters = []
for _ in range(65, 91):
    letters.append(chr(_))
for _ in range(97, 123):
    letters.append(chr(_))

for _ in range(length):
    print(random.choice(letters), end='')