import re


string = input()
word = input()
print(len(re.findall(f"\W{word}\W|^{word}\W|\W{word}$", string)))
