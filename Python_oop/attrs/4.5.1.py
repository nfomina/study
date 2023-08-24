class Rectangle:
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)

rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)

rectangle = Rectangle(20, 20)
array = [(39, 48), (64, 36), (80, 56), (79, 60), (47, 30), (26, 27), (47, 69), (77, 22), (28, 78), (33, 75)]
for length, width in array:
    rectangle.length = length
    rectangle.width = width
    print(f'Периметр = {rectangle.perimeter}, Площадь = {rectangle.area}')
