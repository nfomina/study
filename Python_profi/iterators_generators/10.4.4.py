class Fibonacci:
    def __init__(self):
        self.fib_1 = -1
        self.fib_2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.fib_1 == -1 or self.fib_1 == 0:
            self.fib_1 += 1
            return 1
        else:
            res = self.fib_1 + self.fib_2
            self.fib_1 = self.fib_2
            self.fib_2 = res
            return res




fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

fibonacci = Fibonacci()

for _ in range(76):
    next(fibonacci)

next(fibonacci)
next(fibonacci)
next(fibonacci)
next(fibonacci)

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

fibonacci = Fibonacci()

for _ in range(100):
    next(fibonacci)

print(next(fibonacci))

# simple is beauty
# class Fibonacci:
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
