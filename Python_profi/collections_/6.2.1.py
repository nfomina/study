# x = {'а': '0', 'б': '1', 'в': '2', 'г': '3', 'д': '4',
#         'е': '5', 'и': '6', 'к': '7', 'л': '8', 'о': '9'}
# str = 'таблицу преобразования символов'
# tbl = str.maketrans(x)
# str.translate(tbl)

string = input()
dictionary = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '',
              'f': '', 'g': '', 'h': '', 'i': '', 'j': '',
              'k': '', 'l': '', 'm': '', 'n': '', 'o': '',
              'p': '', 'q': '', 'r': '', 's': '', 't': '',
              'u': '', 'v': '', 'w': '', 'x': '', 'y': '',
              'z': ''}

for i, letter in enumerate(dictionary):
    dictionary[letter] = string[i]

new_string = input()
new_string = new_string.lower()
trans_table = new_string.maketrans(dictionary)
print(new_string.translate(trans_table))

# genius
# from string import ascii_letters
#
# translator = str.maketrans(ascii_letters, input() * 2)
#
# print(input().translate(translator))
