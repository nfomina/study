class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return SuperString(self.string[:len(self.string)//other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other > len(self.string):
                return SuperString('')
            return SuperString(self.string[:len(self.string)-other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other > len(self.string):
                return SuperString('')
            return SuperString(self.string[other:])
        return NotImplemented


s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)

s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)

s = SuperString('beegeek')

print(s << 4)
print(s >> 3)

# TEST_4:
s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)

# TEST_5:
s = SuperString('beegeek')
for i in range(9):
    print(f'{s} >> {i} =', s >> i)

# TEST_6:
names = ['Карп', 'Фотий', 'Любосмысл', 'Клавдия', 'Милован', 'Светлана', 'Александра', 'Ираида', 'Трифон', 'Добромысл',
         'Евпраксия', 'Радим', 'Эдуард', 'Аристарх', 'Ульяна', 'Ираклий', 'Юлия', 'Марк', 'Демид', 'Творимир', 'Орест',
         'Феоктист', 'Тимур', 'Филипп', 'Аверьян', 'Эраст', 'Осип', 'Станислав', 'Адриан', 'Милан', 'Парфен', 'Велимир',
         'Филимон', 'Ратибор', 'Элеонора', 'Феофан', 'Ирина', 'Кузьма', 'Панфил', 'Венедикт', 'Парамон', 'Влас',
         'Надежда', 'Фрол', 'Мартьян', 'Моисей', 'Леонид', 'Мариан', 'Марина', 'Филарет', 'Валентина', 'Севастьян',
         'Светозар', 'Родион', 'Ростислав', 'Капитон', 'Герман', 'Геннадий', 'Иосиф', 'Гостомысл', 'Епифан', 'Гордей',
         'Ферапонт', 'Януарий', 'Денис', 'Галина', 'Аггей', 'Харлампий', 'Акулина', 'Климент', 'Автоном', 'Никанор',
         'Фортунат', 'Сила', 'Федосий', 'Виктор', 'Арсений', 'Дементий', 'Спартак', 'Евгений', 'Феликс', 'Ананий',
         'Нинель', 'Стоян', 'Остромир', 'Никифор', 'Клавдий', 'Чеслав', 'Афанасий', 'Наум', 'Рубен', 'Азарий',
         'Виктория', 'Синклитикия', 'Тимофей', 'Фёкла', 'Нонна', 'Ким', 'София']

for name in names:
    person = SuperString(name)
    print(person * 2, 2 * person, person / 2)

# TEST_7:
s = SuperString('beegeek')
for i in range(1, 9):
    print(f'{s} / {i} =', s / i)

# TEST_8:
superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))