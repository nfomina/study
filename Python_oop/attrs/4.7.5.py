class StrExtension:
    def __init__(self):
        pass

    @staticmethod
    def remove_vowels(string):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        for item in string:
            if item.lower() in vowels:
                string = string.replace(item, '')
        return string

    @staticmethod
    def leave_alpha(string):
        for item in string:
            if item.isalpha() is False:
                string = string.replace(item, '')
        return string

    @staticmethod
    def replace_all(string, chars, char):
        for item in string:
            if item in chars:
                string = string.replace(item, char)
        return string


print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
# Pthn
# Stpk
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
# Python
# Stepik
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
