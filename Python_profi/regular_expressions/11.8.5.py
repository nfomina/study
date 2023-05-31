import re


def multiply(obj):
    a, b, c, d = obj.groups()
    return a + int(b) * c + d


string = input()
while re.search('\(', string):
    string = re.sub(r"([a-z]*)(\d+)\((\w+)\)(.*)", multiply, string)
print(string)
