class Versioned:
    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr][-1]

    def __set__(self, obj, value):
        if self._attr not in obj.__dict__:
            obj.__dict__[self._attr] = []
        obj.__dict__[self._attr].append(value)

    def get_version(self, obj, n):
        if len(obj.__dict__[self._attr]) >= n:
            return obj.__dict__[self._attr][n - 1]

    def set_version(self, obj, n):
        if len(obj.__dict__[self._attr]) >= n:
            self.__set__(obj, self.get_version(obj, n))


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19

print(student.age)


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))

class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
Student.age.set_version(student, 1)
print(student.age)