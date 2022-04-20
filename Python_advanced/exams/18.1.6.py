import re
with open('forbidden_words.txt') as file:
    forbidden_words = file.read().split()

with open(input()) as file:
    string = file.read()
    for word in forbidden_words:
        string = re.sub(word, '*'*len(word), string, flags=re.IGNORECASE)

print(string)
