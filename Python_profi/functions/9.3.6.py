def verification(login, password, success, failure):
    text = ''
    new_password = ''
    for letter in password:
        if letter.isascii() or letter.isdigit():
            new_password += letter
    password = new_password
    if password.isdigit():
        text = 'в пароле нет ни одной буквы'
    elif password.islower() is True:
        text = 'в пароле нет ни одной заглавной буквы'
    elif password.isupper() is True:
        text = 'в пароле нет ни одной строчной буквы'
    elif any(char.isdigit() for char in password) is False:
        text = 'в пароле нет ни одной цифры'
    if text:
        failure(login, text)
    else:
        success(login)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпароль123', success, failure)

# without bicycle
# def verification(login, password, success, failure):
#     vd = {str.isalpha: 'в пароле нет ни одной буквы',
#           str.islower: 'в пароле нет ни одной строчной буквы',
#           str.isupper: 'в пароле нет ни одной заглавной буквы',
#           str.isdigit: 'в пароле нет ни одной цифры'}
#     for f in vd:
#         if not any(f(i) for i in password):
#             return failure(login, vd[f])
#     success(login)
