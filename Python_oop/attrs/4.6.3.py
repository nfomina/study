class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @property
    def x1(self):
        if self._b * self._b - 4 * self._a * self._c < 0:
            return None
        return (-self._b-(pow(self._b*self._b - 4 * self._a * self._c, 0.5)))/(2 * self._a)

    @property
    def x2(self):
        if self._b * self._b - 4 * self._a * self._c < 0:
            return None
        return (-self._b + (pow(self._b * self._b - 4 * self._a * self._c, 0.5))) / (2 * self._a)

    @property
    def view(self):
        res = f'{self._a}x^2'
        if self._b >= 0:
            res += ' + ' + str(self._b) + 'x'
        else:
            res += ' - ' + str(abs(self._b)) + 'x'
        if self._c >= 0:
            res += ' + ' + str(self._c)
        else:
            res += ' - ' + str(abs(self._c))
        return res

    @property
    def coefficients(self):
        return self._a, self._b, self._c

    @coefficients.setter
    def coefficients(self, coefficients):
        self._a, self._b, self._c = coefficients


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

# TEST_4:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_5:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_6:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, 0, -9)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_7:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 0, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_8:
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

# TEST_9:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
