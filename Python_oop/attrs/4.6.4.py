class Color:
    def __init__(self, color):
        self._r, self._g, self._b = color[0:2], color[2:4], color[4:6]

    @property
    def r(self):
        return int(self._r, base=16)

    @property
    def g(self):
        return int(self._g, base=16)

    @property
    def b(self):
        return int(self._b, base=16)

    @property
    def hexcode(self):
        return self._r + self._g + self._b

    @hexcode.setter
    def hexcode(self, color):
        self._r, self._g, self._b = color[0:2], color[2:4], color[4:6]


color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
