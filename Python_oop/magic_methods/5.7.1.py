class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return True if self.x | self.y != 0 else False

    def __int__(self):
        return int(pow(self.x**2 + self.y**2, 0.5))

    def __float__(self):
        return float(pow(self.x ** 2 + self.y ** 2, 0.5))

    def __complex__(self):
        return complex(self.x, self.y)


vector = Vector(3, 4)

print(vector)
print(int(vector))
print(float(vector))
print(complex(vector))

print(bool(Vector(1, 2)))
print(bool(Vector(1, 0)))
print(bool(Vector(0, 1)))
print(bool(Vector(0, 0)))