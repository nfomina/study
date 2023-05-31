import re


string = input()
word = input()
res = re.findall(f"\B{word}\B", string)
print(len(res))
