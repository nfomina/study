from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.area = pi * pow(self.radius, 2)


circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)
