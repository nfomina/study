class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._tp = (self.x, self.y, self.z)

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from self._tp


point = Point(1, 2, 3)

print(list(point))

point = Point(1, 2, 3)
x, y, z = point

print(x, y, z)

points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
print(points)
