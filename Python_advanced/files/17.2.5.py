with open('nums.txt') as file:
    text = file.read().split()
print(int(text[0]) + int(text[1]))