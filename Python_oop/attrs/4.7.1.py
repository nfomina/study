class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


circle = Circle(5)

print(circle.radius)

circle = Circle.from_diameter(10)

print(circle.radius)

# TEST_3:
circle1 = Circle(51.5)
circle2 = Circle.from_diameter(45)

print(circle1.radius)
print(circle2.radius)

# TEST_4:
array = [473, 474, 75, 182, 51, 491, 493, 494, 347, 305, 290, 381, 170, 355, 326, 97, 183, 120, 216, 475, 66, 306, 193,
         257, 482, 200, 350, 236, 471, 468]

for diameter in array:
    circle = Circle.from_diameter(diameter)
    print(circle.radius)

# TEST_5:
circle = Circle.from_diameter(120)
print(hasattr(circle, 'radius'))

