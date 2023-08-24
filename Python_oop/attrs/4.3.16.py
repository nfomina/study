class User:
    def check_name(self, name):
        if type(name) is not str or name == '' or all(c.isalpha() for c in name) is False:
            raise ValueError('Некорректное имя')
        else:
            self._name = name

    def check_age(self, age):
        if type(age) is not int or int(age) < 0 or int(age) > 110:
            raise ValueError('Некорректный возраст')
        else:
            self._age = age

    def __init__(self, name, age):
        self._name = ''
        self._age = 0
        self.check_name(name)
        self.check_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self.check_name(new_name)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self.check_age(new_age)


user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())

user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())

# TEST_3:
user = User('Меган', 37)

invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)

# TEST_4:
user = User('Меган', 37)

invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)

# TEST_5:
invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user = User(name, 37)
    except ValueError as e:
        print(e)

# TEST_6:
invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50)
for age in invalid_ages:
    try:
        user = User('Меган', age)
    except ValueError as e:
        print(e)

# TEST_7:
try:
    user = User('Gvido_1956', '67')
except ValueError as e:
    print(e)
