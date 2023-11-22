class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def __repr__(self):
        return f'ColoredPoint({self._x}, {self._y}, \'{self._color}\')'

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._x == other._x and self._y == other._y and self._color == other._color
        return NotImplemented

    def __hash__(self):
        return hash((self._x, self._y, self._color))

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_color(self):
        return self._color

    color = property(get_color)
    x = property(get_x)
    y = property(get_y)


point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))

points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

print(points)

point = ColoredPoint(1, 2, 'white')

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')
