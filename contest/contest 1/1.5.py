
symbols = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~1234567890'

input_string = input()
new_string = ''
for item in input_string:
    if item not in symbols:
        new_string += item


def f(new_string, i, j):
    while i < j:
        if new_string[i] != new_string[j]:
            return False
        i += 1
        j -= 1
    return True

i = 0
j = len(new_string) - 1

if f(new_string, i, j):
    print('True')
    exit()

while i < j:
    if new_string[i] != new_string[j]:
        if f(new_string, i, j - 1):
            print('True')
            exit()
        if f(new_string, i + 1, j):
            print('True')
            exit()
        print('False')
        exit()
    i = i + 1
    j = j - 1

# Genius
# def isAlmostPalindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[-1 - i] and s[i + 1] != s[-i - 1] and s[i] != s[-i - 2]:
#             return False
#     return True
# s = ''.join(filter(str.isalpha, input()))
# print(isAlmostPalindrome(s))