from collections import Counter

with open('pythonzen.txt') as file:
    for item in sorted(Counter([letter for letter in file.read().lower() if letter.isalpha()]).items()):
        print(f'{item[0]}: {item[1]}')
