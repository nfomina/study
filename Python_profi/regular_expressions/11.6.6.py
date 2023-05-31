from re import search, I


if search(r'^Здравствуйте|^Доброе утро|^Добрый день|^Добрый вечер', input(), I):
    print('True')
else:
    print('False')
