class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return pow((self.x * self.x + self.y * self.y), 0.5)


vector = Vector()

print(vector.x, vector.y)
print(vector.abs())

vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())
