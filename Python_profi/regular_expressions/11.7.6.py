import re


def abbreviate(text):
    res = ''
    letters = re.findall('\s(\w)|([A-Z])|(^\w)', text, re.M)
    for item in letters:
        for i in item:
            if i:
                res += i.upper()
    return res


print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))
print(abbreviate('gaveOver GameStarted happyEnd happyend'))

# smart
# def abbreviate(phrase):
#     return ''.join(re.findall(r'[A-Z]|\b\w',phrase)).upper()
