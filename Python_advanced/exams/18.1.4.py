
with open('words.txt') as file:
    words = file.read().split()
    max_len = len(max(words, key=len))
    for item in [word for word in words if len(word)==max_len]:
        print(item)
