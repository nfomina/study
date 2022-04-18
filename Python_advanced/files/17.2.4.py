with open('numbers.txt') as file:
    text = file.readlines()
print(int(text[0]) + int(text[1]))