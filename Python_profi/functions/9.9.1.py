from functools import partial


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address}u сказано следующее: {text}'


to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')

send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на'
                                              ' языке Python. тутут....')


# TEST_1:
print(to_Timur('когда курс?'))

# TEST_2:
print(to_Timur('Тимур, привет, я на егэ, помоги решить 13 задачу'))

# TEST_3:
print(to_Timur('хочу курс по искусственным интеллектам и криптовалютам бесплатно и завтра'))

# TEST_4:
try:
    to_Timur()
except:
    print('ok')

# TEST_5:
try:
    to_Timur('первое', 'второе')
except:
    print('ok')

# TEST_6:
try:
    to_Timur('первое', 'второе', 'третье')
except:
    print('ok')

# TEST_7:
try:
    to_Timur('beegeek')
    print('ok')
except:
    print('ne ok')

# TEST_8:
print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))

# TEST_9:
try:
    print(send_an_invitation("Тимур"))
except:
    print("Ошибка, и где же? Хм-м-м")

# TEST_10:
print(to_Timur('Здравствуйте! Я Таня из компании Орифлэйм. Хочу предложить вам новую линейку курсов от Поколения Python'))

# TEST_11:
print(to_Timur('This is... Requiem. What you are seeing is indeed the truth.'))
