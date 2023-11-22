class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if type(value) in (float, int):
                setattr(self, key, abs(value))
            else:
                setattr(self, key, value)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)


point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)

point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)