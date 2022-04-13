
def print_products(*args):
    i = 1
    for arg in args:
        if type(arg) == str and arg != '':
            print(f'{i}) {arg}')
            i += 1
    if i == 1:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')