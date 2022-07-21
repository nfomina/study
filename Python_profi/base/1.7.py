
def likes(names):
    count = len(names)
    if count == 0:
        return 'Никто не оценил данную запись'
    elif count == 1:
        return f'{names[0]} оценил(а) данную запись'
    elif count == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    elif count == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        return f'{names[0]}, {names[1]} и {count - 2} других оценили данную запись'


print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))

print(likes(['Дима', 'Алиса']))
print(likes(['Эндрю', 'Тоби', 'Том']))
print(likes([]))
print(likes(['Том']))
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур', 'Тимур']))
print(likes(['Артур', 'Тимур', 'Руслан', 'Анри', 'Дима', 'Алиса']))
names = [str(i) * 3 for i in range(100)]
print(likes(names))