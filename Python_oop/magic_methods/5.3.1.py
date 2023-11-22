class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector) or (isinstance(other, tuple) and all(isinstance(v, int | float) for v in other)):
            return (self.x, self.y) == other
        return NotImplemented


a = Vector(1, 2)
b = Vector(1, 2)

print(a == b)
print(a != b)

a = Vector(1, 2)
pair1 = (1.0, 2.0)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)

# TEST_6:
a = Vector(0, 1)
not_supported = [[1, 2], True, (1, 2, 3, 4), 'beegeek', {'name': 'Grace Hopper'}, {18, 22}]

for item in not_supported:
    print(a == item)

# TEST_7:
a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)

# TEST_8:
vector = Vector(0, 1)

print(vector.__eq__(1))
print(vector.__ne__(1.1))
print(vector.__gt__(range(5)))
print(vector.__lt__([1, 2, 3]))
print(vector.__ge__({4, 5, 6}))
print(vector.__le__({1: 'one'}))
