
def convert(string):
    count_low = 0
    count_up = 0
    for i in string:
        if i.islower():
            count_low += 1
        elif i.isupper():
            count_up += 1
    if count_low >= count_up:
        return string.lower()
    else:
        return string.upper()

print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
print(convert('ABCDEF'))
print(convert('abcdef'))
print(convert('12345!?'))
print(convert('PI31415!'))
print(convert('ABCdef'))
print(convert('ABCdef123'))
print(convert('AbCdEf12345'))
print(convert('dEfAbC'))


# smart enough
# def convert(string):
#     if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()