class TypeChecked:
    def __init__(self, *args):
        self.args = args

    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if type(value) in self.args:
            obj.__dict__[self._attr] = value
        else:
            raise TypeError('Некорректное значение')


class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

print(student.name)

class Student:
    name = TypeChecked(str)

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)

class Student:
    age = TypeChecked(int, float)

student = Student()

student.age = 18
print(student.age)

student.age = 18.5
print(student.age)