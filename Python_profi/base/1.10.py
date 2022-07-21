
def choose_plural(amount, declensions):
    n = amount % 100
    if n >= 11 and n <= 19:
        s = declensions[2]
    else:
        i = n % 10
        if i == 1:
            s = declensions[0]
        elif i in [2, 3, 4]:
            s = declensions[1]
        else:
            s = declensions[2]
    return f'{amount} {s}'



print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))
